import os
import re
filenames = os.listdir("./data/sec-edgar-filings")

reg = re.compile('<[^>]*>')
html = '''<p Style='page-break-before:always'>
<HR  SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">


<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:arial; font-size:9pt" ALIGN="center">

<TR>
<TD WIDTH="100%"></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8" BGCOLOR="#478faa"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:arial; font-size:9pt">
<TD VALIGN="top" STYLE="BORDER-BOTTOM:2.00pt solid #ffffff" BGCOLOR="#478faa"> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:9pt; font-family:arial" ALIGN="right"><FONT COLOR="#fdfdfe">&nbsp;&nbsp;2018 NOTICE OF MEETING AND PROXY
STATEMENT&nbsp;&nbsp;</FONT></P> <P STYLE="font-size:6pt; margin-top:0pt; margin-bottom:1pt" align="left">&nbsp;</P></TD></TR></TABLE> <P STYLE="font-size:6pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P>
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:arial" ALIGN="center"><B><A NAME="toc543804_40"></A>CHIEF EXECUTIVE OFFICER PAY RATIO </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:5%; font-size:10pt; font-family:arial">For 2017: </P> <P STYLE="font-size:3pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:arial; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="1%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top">the annual total compensation for the median employee of the Company (other than our Chief Executive Officer) was $89,909; and </TD></TR></TABLE> <P STYLE="font-size:3pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:arial; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="1%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top">the annual total compensation of our Chief Executive Officer was $10,894,821<SUP STYLE="font-size:85%; vertical-align:top">(1)</SUP>. </TD></TR></TABLE>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:5%; font-size:10pt; font-family:arial">Based on this information, for 2017 the ratio of the annual total compensation of our Chief Executive Officer to the annual total compensation of the
median employee was 121 to 1. This ratio is a reasonable estimate calculated in a manner consistent with Item 402(u) of Regulation <FONT STYLE="white-space:nowrap">S-K</FONT> under the Securities Exchange Act of 1934. </P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:5%; font-size:10pt; font-family:arial">As permitted by SEC rules, to identify our median employee, we selected &#147;total estimated compensation&#148; which we calculated as annual base pay
plus the estimated bonus for 2017 plus the grant value of stock awards, as the compensation measure to be used to compare the total compensation of our employees in our seven largest countries of employment as of December&nbsp;1, 2017 (which
consisted of approximately 8,965 individuals or 97.1% of our total employee population&#151;see the below table for a full list of included and excluded countries). We annualized base pay and estimated bonus for any regular employees who commenced
work during 2017 and did not annualize these amounts for temporary and seasonal employees. Using this approach, we determined that our median employee was a Design Engineer based in the United States. </P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:arial" ALIGN="center"><B>Included and Excluded Countries for Selection of Median Employee </B></P>  <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
'''
result = reg.sub('',html).replace("\n","").replace(" ","")
email = "jldwjalksdj 18 115 : 1"
ret1 = re.findall('([0-9]{1,5}\s?(to|:)\s?[0-9]{1,5})', email)
'(\$\d+([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?([,\.]\d+)?)'

a = "For 2017, the ratio of the annual total compensation of Mr. Sadlowski, our CEO who was serving in such capacity on November 30, 2017 (“CEO Compensation”), to the median of the annual total compensation of all our employees and those of our consolidated subsidiaries (other than Mr. Sadlowski) (“Median Annual Compensation”), was 26 to 1."
a = a.replace(" ","")
def getFileNames(dir):
    filenames = os.listdir(dir)
    return filenames
all_companies = getFileNames("./data/sec-edgar-filings")


''' from sec_edgar_downloader import Downloader
dl = Downloader("./test")
dl.get("DEF 14A", "320193", after="2018-01-01", before="2019-12-31", query="CEO Pay Ratio", download_details=False) 
try:
    float("1.2.3")
except:
    print("error") '''


results = re.findall(r'(\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?\d+([,\.]\d+)?)|(\d+([,\.]\d+)?(\s|-)?times)|(\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?one)', '''CEO pay to the pay of the Corporation’s median employee for 
fiscal year 2017 is 186 to one''')
check_end = re.search('((\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?\d+([,\.]\d+)?([^0-9|,|.])|([,|.][^0-9|,|.]))$)|((\d+([,\.]\d+)?(\s|-)?times)$)|((\d+([,\.]\d+)?(\s|-)?(to|:)(\s|-)?one)$)', '''CEO pay to the pay of the Corporation’s median employee for 
fiscal year 2017 is 186 to one''')
def process(results):
    for i in results:
        if len(results)>0:
            res = results[0][0]
            if res == "":
                for i in results[0]:
                    if i != "":
                        res = i
                        break
            if "times" in res: # e.g. 49 times
                res = res.replace("times", ":").replace(" ","").replace(",","")
                res+="1"
                return res
            if "one" in res:
                res = res[:res.find("one")]+"1"
            if "-" in res:
                res.replace("-","")
            if "to" in res:
                res = res.replace("to",":")
            res = res.replace(" ","").replace(",","")
            if res[res.find(":")+1:] == "1" or res[res.find(":")+1:] == "1.0":
                return res
            if res[:res.find(":")] =="1":
                return res[res.find(":")+1:]+":"+res[:res.find(":")]
            return None
        else:
            return None
res = process(results)
print(res)
print(check_end)
a = '''Following is a description of the relationship of the total annual compensation of our employees and the total annual compensation of our CEO, Dr. Byrne. The pay ratio included in this information is a reasonable estimate calculated in a manner consistent with Item 402(u) of Regulation S-K.

34

Table of Contents

        For 2017, our last completed fiscal year:

•
the median of the annual total compensation of all of our employees (other than our CEO), determined as described below, was $56,806; and

•
the annual total compensation of our CEO, as reported in the Summary Compensation Table included in this proxy statement, was $444,576.
        Based on this information, for 2017 the ratio of the annual total compensation of Dr. Byrne, our CEO, to the median of the annual total compensation of all employees was 7.83 to 1.

        To identify the median of the annual total compensation of all our employees, as well as to determine the annual total compensation of the "median employee," the methodology and the material assumptions, adjustments and estimates that we used were as follows:

•
We determined that, as of October 1, 2017, our employee population consisted of approximately 1,834 individuals working at Overstock.com, Inc. and its consolidated subsidiaries, with 97.2% of these individuals located in the United States, 1.3% located in Ireland, 1.47% located in Colombia, and 0.05% located in China. Our employee population, after taking into consideration the adjustments permitted by SEC rules (as described below), consisted of approximately 1,782 individuals. As permitted by SEC rules, because our non-U.S. employees account for 5% or less of our total employees, we elected to exclude all of our non-U.S. employees. We used our existing internal payroll records to determine that non-U.S. employees accounted for 5% or less of our total employees as of October 1, 2017. The jurisdictions from which we have excluded employees under Item 402(u)(4)(ii) of Regulation S-K, and the approximate number of employees excluded from each such jurisdiction under that rule, are as follows:
Country	 	Approximate No. of Excluded Employees	 
Ireland	 	 	24	 
Colombia	 	 	27	 
China	 	 	1	 
        The total number of our U.S. and non-U.S. employees irrespective of any exemption permitted by SEC rules was 1,834, and the total number of our U.S. and non-U.S. employees used for our de minimis calculation set forth above was 1,782.

        To identify the "median employee" from our employee population, we used our internal records, which track annualized wages and salaries for all of our employees as well as additional pay components such as overtime, paid time off, bonuses, and other benefits provided by the Company to come up with total compensation for each of the 1,782 employees.

        Using this methodology, we determined that our "median employee" was a full-time, salaried employee located in Salt Lake City, Utah, with a salary for the 12-month period ended December 31, 2017 in the amount of $51,838. '''
b = "median employee, we identified and calculated the elements of such employee's compensation for the year ended December 31, 2017 in accordance with the requirements of Item 402(c)(2)(x) of Regulation S-K, resulting in annual total compensation of $56,806."
c = '''n accordance with SEC rules, we are providing the ratio of the annual total compensation of our CEO to the annual total compensation 
of our median associate, which is a reasonable estimate calculated in a manner consistent with SEC rules and is based on our payroll and 
employment records and the methodology described below. In calculating this ratio, SEC rules allow companies to adopt a variety of 
methodologies, apply certain exclusions, and make reasonable estimates and assumptions refle ting their unique employee populations. 
As discussed on pages 45-47 above, our company is unique because we are significa tly larger than most of our peer group companies in 
terms of revenue, market capitalization, and the size and scope of our worldwide associate population. Therefore, our reported pay ratio 
may not be comparable to that reported by other companies due to differences in industries, scope of international operations, business 
models and scale, as well as the different estimates, assumptions, and methodologies applied by other companies in calculating their 
respective pay ratios. 
Considered Population. As of December 31, 2017, we employed approximately 2,306,496 associates worldwide, other than our CEO. As 
permitted by SEC rules, in order to determine our median associate, we excluded approximately 3.9% of our total associate population or 
approximately 89,951 associates outside of the U.S. from the following countries: Argentina (12,737); Bangladesh (95); Botswana (864); Costa 
Rica (16,390); El Salvador (4,314); France (2); Ghana (164); Guatemala (10,299); Holland (2); Honduras (3,997); Hong Kong (7); India (5,529); 
Indonesia (11); Ireland (22); Italy (2); Kenya (69); Lesotho (173); Luxembourg (2); Malawi (141); Morocco (3); Mozambique (519); Namibia 
(272); Nicaragua (4,021); Nigeria (370); Pakistan (23); Peru (6); South Africa (29,089); Spain (20); Sri Lanka (52); Swaziland (46); Tanzania (67); 
Thailand (4); Turkey (75); Uganda (78); Vietnam (25); and Zambia (461). Therefore, an aggregate associate population of approximately 
2,216,545 was considered (the “considered population”) in determining our median associate.
Identifying our Median Associate. In determining our median associate, we used calendar year 2017 gross earnings – meaning total 
amounts paid before deductions or adjustments, including wages, overtime, bonuses, and the value of any equity awards that vested and 
were paid to an associate during calendar year 2017. Adjustments were made to annualize the gross earnings of all newly hired permanent 
associates in the considered population who did not work for the entire calendar year 2017. From the considered population, we then used 
statistical sampling to identify a group of associates who were paid within a range of 0.5% above or below what we estimated to be our 
median gross earnings amount (the “median population”). We then reviewed recent historical taxable wage data of the median population, 
and for those associates within the median population with stable wages, we calculated each of their fiscal 2018  otal compensation in 
the same way as we calculated our CEO’s fiscal 2018  otal compensation as set forth in the Summary Compensation table on page 66 and 
identified the median  ompensated associate from this group.
Based upon the estimates, assumptions, and methodology described above, the fiscal 2018 annual  otal compensation of our CEO  
was $22,791,276, the fiscal 2018 annual  otal compensation of our median associate was $19,177, and the ratio of these amounts  
was 1,188:1.
'''
print(len(c))