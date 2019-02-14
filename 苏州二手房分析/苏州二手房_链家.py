import requests
from lxml import etree
import time
import csv

class LianjiaSpider:
    def __init__(self):
        self.baseurl='https://su.lianjia.com/ershoufang/pg'
        self.headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
    
    #获取页面
    def getPage(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        parseHtml = etree.HTML(html)
        tlist = parseHtml.xpath('//div[@class="info clear"]//div[@class="title"]//a//@href')
        # print(tlist)
        for tlink in tlist:
            self.parsePage(tlink)
    
    #解析并保存页面
    def parsePage(self,tlink):
        res = requests.get(tlink, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        parseHtml = etree.HTML(html)
        tprice=parseHtml.xpath('//div[@class="price "]//span[@class="total"]//text()')[0]
        tunit=parseHtml.xpath('//div[@class="price "]//span[@class="unit"]//text()')[0]
        uprice=parseHtml.xpath('//div[@class="price "]//div[@class="unitPrice"]//text()')[0]
        uunit=parseHtml.xpath('//div[@class="price "]//div[@class="unitPrice"]//text()')[1]
        room=parseHtml.xpath('//div[@class="room"]//text()')[0]
        louceng=parseHtml.xpath('//div[@class="room"]//text()')[1].split('/')[0]
        direction=parseHtml.xpath('//div[@class="houseInfo"]//div[@class="type"]//text()')[0]
        area=parseHtml.xpath('//div[@class="houseInfo"]//div[@class="area"]//text()')[0]
        year = parseHtml.xpath('//div[@class="houseInfo"]//div[@class="area"]//text()')[1].split('/')[0]
        communityname=parseHtml.xpath('//div[@class="communityName"]//a[1]//text()')[0]
        areaName=parseHtml.xpath('//div[@class="areaName"]//span[@class="info"]//a[1]//text()')[0]
        areaName2 = parseHtml.xpath('//div[@class="areaName"]//span[@class="info"]//a[2]//text()')[0]
        r = [communityname.strip(),tprice.strip(),tunit.strip(),uprice.strip(),uunit.strip(),room.strip(),louceng.strip(),direction.strip(),area.strip(),year.strip(),areaName.strip(),areaName2.strip()]

        #写入csv文件
        with open("house.csv", "a", newline="", encoding="gb18030") as f:
            # 创建写入对象
            writer = csv.writer(f)
            # 调用witerow()方法
            writer.writerow(r)
            
    #主函数
    def workOn(self):
        n=int(input("请输入页数："))
        for pg in range(1,n+1):
            #拼接url
            url=self.baseurl+str(pg)
            self.getPage(url)
            print("第%d页爬取成功"%pg)
            # time.sleep(0.1)
    
if __name__=="__main__":
    spider=LianjiaSpider()
    spider.workOn()