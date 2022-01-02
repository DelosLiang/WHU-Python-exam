"""
爬取中国两岸四地最好大学排名
ZhangHua @20190707
"""
import requests
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(univ_list, html_doc):
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            univ_list.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivRanking(univ_list, num):
    print('{:3}{:20}{:6}{:6}'.format('排名','学校','地区','总分'))
    for i in range(num):
        univ = univ_list[i]
        name = ('{:11}'.format(univ[1])).replace(' ', '  ')
        loc = ('{:4}'.format(univ[2])).replace(' ', '  ')
        print('{:5}{:11}{:4}{:8}'.format(univ[0], name, loc, univ[3]))


def main():
    univ_list = []
    url = 'http://www.zuihaodaxue.cn/Greater_China_Ranking2018_0.html'
    html_doc = getHTMLText(url)
    fillUnivList(univ_list, html_doc)
    printUnivRanking(univ_list, 25)


if __name__ == '__main__':
    main()
