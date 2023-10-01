from sec_edgar_downloader import Downloader
import json
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
for i in cik_list:
    try:
        print("{} downloading".format(i))
        dl.get("DEF 14A", i, after="2021-01-01", before="2021-12-31", query="CEO Pay Ratio", download_details=False)
        print("{} downloaded".format(i))
        count += 1
        print("{} / {} ".format(count, len(cik_list)))
    except:
        print("error in {}".format(i))