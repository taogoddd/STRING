import os
import csv

def ratio_find_cik(data, ratio):
    for i in data:
        if i[-1] == str(ratio) + ":1" or i[-1] == str(ratio) + ":1.0" or i[-1] == str(int(ratio)) + ":1" or i[-1] == str(int(ratio)) + ":1.0":
            return i[1]

def median_find_cik(data, median):
    for i in data:
        if i[-2] == str(median) or i[-2] == str(int(median)):
            return i[1]

def eliminate_extreme_value(data, cut_size):
    return data[cut_size:len(data)-cut_size]

with open("./test3.csv", 'r') as f:
    csv_reader = csv.reader(f)
    line = 0
    data = []
    for row in csv_reader:
        if row[0] != "Ticker":
            data.append(row)
with open("./test4.csv", "w", newline=""):
    
ceo = []
median = []
ratio = []
for i in data:
    if i[3] != '':
        ceo.append(float(i[3]))
    if i[4] != '' :
        median.append(float(i[4]))
    if i[5] != '' :
        if ":" in i[5]:
            ratio.append(float(i[5][:i[5].find(":")]))
        else:
            ratio.append(float(i[5]))
sorted_ceo = sorted(ceo)
sorted_median = sorted(median)
sorted_ratio = sorted(ratio)
print("First 20 median:",sorted_median[:20])
print("Last 20 median:",sorted_median[len(sorted_median)-20:])
print(sorted_ratio[len(sorted_ratio)-20:])
processed_ceo = eliminate_extreme_value(sorted_ceo, 0)
processed_median = eliminate_extreme_value(sorted_median, 0)
processed_ratio = eliminate_extreme_value(sorted_ratio, 4)
print("Average:", round(sum(processed_ceo)/len(processed_ceo),0), round(sum(processed_median)/len(processed_median),0), round(sum(processed_ratio)/len(processed_ratio),0))

print("first 20 medians: ")
for i in sorted_median[:20]:
    print("cik:", median_find_cik(data, i), "median", i)
print("last 20 medians: ")
for i in sorted_median[len(sorted_median)-20:]:
    print("cik:", median_find_cik(data, i), "median", i)
