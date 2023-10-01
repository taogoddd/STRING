from sec_edgar_downloader import Downloader
import json
from threading import Thread, Event

stop_event = Event()

with open("./tickers.json", 'r') as f:
    dic = json.load(f)
    companies = []
    for i in range(0,11611):
        companies.append(dic[str(i)])
cik = [i["cik_str"] for i in companies]
cik_set = set(cik)
cik_list = list(cik_set)
dl = Downloader("./data_2021")
count = 0
def download():
    for i in cik_list:
        if stop_event.is_set():
            continue
        try:
            print("{} downloading".format(i))
            print("{} downloaded".format(i))
            dl.get("DEF 14A", i, after="2021-01-01", before="2021-12-31", query="CEO Pay Ratio", download_details=False)
            count += 1
            print("{} / {} ".format(count, len(cik_list)))
        except:
            print("error")

if __name__ == '__main__':
    # We create another Thread
    action_thread = Thread(target=download)
 
    # Here we start the thread and we wait 5 seconds before the code continues to execute.
    action_thread.start()
    action_thread.join(timeout=5)
 
    # We send a signal that the other thread should stop.
    stop_event.set()


import re
import csv
import json
import os

def getFileNames(dir):
    filenames = os.listdir(dir)
    return filenames

def findMedian(slice):
    slice = slice.lower()
    results = re.findall(r'(\$\d+([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?)', slice)
    check_end = re.search('(\$\d+([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?([^0-9|,|.])|([,|.][^0-9|,|.]))$', slice)
    if "median" in slice and "compensation" in slice and len(results) > 0 and (check_end != None) :
        for i in results:
            if slice.find(i[0]) < slice.find("median"):
                results.remove(i)
        if len(results)>0:
            return results
        else:
            return None
    else:
        return None

def extractMedian(data):
    data_size = len(data)
    window_size = 100 #try for times
    flag = False
    for j in range(3):
        for i in range(data_size-window_size-j*100):
            results = findMedian(data[i:i+window_size+j*100])
            if results != None:
                flag = True
                res = results[0][0].replace("$", "").replace(",", "")
                if float(res) < 1000 or float(res) > 1000000: # prevent extract the wrong place
                    for k in results: #[('$22,791,276', ',791', ',276', '', ''), ('$19,177', ',177', '', '', '')]
                        k_res = k[0].replace("$", "").replace(",", "")
                        if float(k_res) >1000 and float(k_res) < 1000000:
                            return (k_res, data[i:i+window_size+j*100]) 
                    continue
                else:
                    return (res, data[i:i+window_size+j*100])
    if not flag:
        return None

def findCEO(slice):
    slice = slice.lower()
    results = re.findall(r'(\$\d+([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?)', slice)
    check_end = re.search('(\$\d+([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?([^0-9|,|.])|([,|.][^0-9|,|.]))$', slice)
    if ("ceo" in slice or "chiefexecutiveofficer" in slice) and "compensation" in slice and len(results) > 0 and "median" not in slice and (check_end != None):
        if slice.find("ceo") == -1:
            bar = slice.find("chiefexecutiveofficer")
        elif slice.find("chiefexecutiveofficer") == -1:
            bar = slice.find("ceo")
        else:
            bar = min(slice.find("chiefexecutiveofficer"), slice.find("ceo"))
        for i in results:
            if slice.find(i[0]) < bar:
                results.remove(i)
        if len(results)>0:
            return results
        else:
            return None
    else:
        return None

def extractCEO(data):
    data_size = len(data)
    window_size = 100 #try for times
    flag = False
    for i in range(data_size-window_size):
        results = findCEO(data[i:i+window_size])
        if results != None:
            flag = True
            if median!= None and float(results[0][0].replace("$", "").replace(",", "")) <= float(median):
                continue
            else:
                return results[0][0].replace("$", "").replace(",", "")
        
    if not flag:
        return None

def findRatio(slice):
    slice = slice.lower()
    results = re.findall(r'(\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?\d+([,\.]\d+)?)|(\d+([,\.]\d+)?(\s|-)?times)|(\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?one)', slice)
    check_end = re.search('((\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?\d+([,\.]\d+)?([^0-9|,|.])|([,|.][^0-9|,|.]))$)|((\d+([,\.]\d+)?(\s|-)?times)$)|((\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?one)$)', slice)
    if ("ratio" in slice or "times" in slice)and "compensation" in slice and  ("median" in slice or "ceo" in slice or "chiefexecutiveofficer" in slice) and len(results) > 0 and (check_end != None):
        for i in results:
            if i[0] != "" and slice.find(i[0]) < slice.find("ratio"):
                results.remove(i)
        if len(results)>0:
            res = results[0][0]
            if res == "":
                for i in results[0]:
                    if i != "":
                        res = i
                        break
            if "times" in res: # e.g. 49 times
                res = res.replace("times","").replace(" ","").replace(",","")
                return res
            if "one" in res:
                res = res[:res.find("one")]+"1"
            if "-" in res:
                res = res.replace("-","")
            if "to" in res:
                res = res.replace("to",":")
            res = res.replace(" ","").replace(",","")
            if res[res.find(":")+1:] == "1" :
                return res[:res.find(":")]
            if res[res.find(":")+1:] == "1.0":
                return res[:res.find(":")]
            if res[:res.find(":")] =="1":
                return res[res.find(":")+1:]
            return None
        else:
            return None
    else:
        return None

def extractRatio(data):
    data_size = len(data)
    window_size = 100 #try for times
    flag = False
    for j in range(5):
        for i in range(data_size-window_size-j*100):
            results = findRatio(data[i:i+window_size+j*100])
            if results != None and float(results)<=5000 and float(results)>0.1:
                flag = True
                return (results, data[i:i+window_size+j*100])
    return None



with open("./tickers.json", 'r') as f:
    dic = json.load(f)
    companies = []
    for i in range(0,11611):
        companies.append(dic[str(i)])

all_companies = getFileNames("./data_2021/sec-edgar-filings")

header = ["Ticker","CIK","Title","CEO", "Median", "Ratio", "Median Source", "Ratio Source"]

with open('output_2021.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    #write the header
    writer.writerow(header)
    rows = []
    count = 0
    for i in companies:
        flag1, flag2 = False, False
        median, ceo, ratio = None, None, None
        medianS, ratioS = "", "" #median source text and ration source text
        if count < 10000:
            avai_cik = getFileNames("./data_2021/sec-edgar-filings/")
            if str(i["cik_str"]).zfill(10) in avai_cik:
                code_list = getFileNames("./data_2021/sec-edgar-filings/"+str(i["cik_str"]).zfill(10)+"/DEF 14A")
                if len(code_list) == 0:
                    ceo, median, ratio = "not found", "not found", "not found"
                    break
                code = code_list[0]
                with open("./data_2021/sec-edgar-filings/"+str(i["cik_str"]).zfill(10)+"/DEF 14A/"+code+"/full-submission.txt", encoding="utf-8") as f:
                    print(i["cik_str"],"is being extracted.")
                    count += 1
                    str_html_content = str(f.read())
                    cut_pos = str_html_content.find("<PDF>")
                    str_html_content = str_html_content[:cut_pos]
                    reg = re.compile('<[^>]*>')
                    str_no_html_content = reg.sub('',str_html_content).replace("\n","") # no html tag
                    pay_ratio_pos = [substr.start() for substr in re.finditer("pay ratio" , str_no_html_content.lower())]
                if len(pay_ratio_pos) == 0:
                    medianS, ratioS = "Refer to original file", "Refer to original file"
                for j in pay_ratio_pos: # since this is a for loop, so there might also be text even if the data is extracted correctly
                    temp = extractMedian(str_no_html_content[j-2000:j+4000])
                    if temp != None:
                        data = temp[0]
                        text = temp[1]
                        median = data
                        medianS = text
                    if median != None:
                        break
                for k in pay_ratio_pos:
                    temp = extractRatio(str_no_html_content[k-2000:k+4000])
                    if temp != None:
                        data = temp[0]
                        text = temp[1]
                        ratio = data
                        ratioS = text
                    if ratio != None:
                        break
                ''' if median == None or ratio == None:
                    pay_median_pos = [substr.start() for substr in re.finditer("median" , str_no_html_content.lower())]
                    if median == None:
                        for m in pay_median_pos:
                            median = extractMedian(str_no_html_content[m-4000:m+4000])
                    if ratio == None:
                        for n in pay_median_pos:
                            ratio = extractRatio(str_no_html_content[n-4000:n+4000]) '''
                try:
                    ceo = float(ratio[:ratio.find(":")])*float(median)
                except:
                    ceo = None
                data = [i["ticker"], i["cik_str"], i["title"], ceo, median, ratio, medianS, ratioS]
            else:
                continue
            #rows.append(data)
            writer.writerow(data)
            for i in data:
                print(i)
            print("number of files extracted now :", count)