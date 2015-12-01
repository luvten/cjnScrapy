__author__ = 'cuijianing'
import scrapy
from tutorial.items import ZhihuItem
from BeautifulSoup import *

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    handle_httpstatus_list = [404, 500]
    user_list=[]
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        "http://www.zhihu.com/people"
    ]

    def parse(self, response):
        for usrname in range(10000):
            url = self.start_urls[0]+'/'+str(usrname)
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        print self.user_list

    def parse_dir_contents(self, response):
        if response.status in self.handle_httpstatus_list:
            pass
        else:
            item = ZhihuItem()
            #item['title'] = response.xpath('/head/title').extract()
            #print item['title']
            soup = BeautifulSoup(response.body)
            f=open('zhihuyonghu','a')
            f.write(str(soup.title.string))
            f.close()
            print soup.title



'''
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
'''