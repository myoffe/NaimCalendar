import scrapy

from NaimCalendar.items import CalendarItem

class CalendarSpider(scrapy.Spider):
    name = "calendar"
    start_urls = [
        'http://tazman.co.il/templates/schedule.php?width=800&height=800&id=511&client_side=1&location_id=0&month=3&teacher=0&categories=0&multiselect=1&lang=he&css=6&js=1&iframeId=tazmanframe2&iframeDomain=http://www.naim.org.il'
    ]

    def parse(self, response):
        """
        lesson = sel[3]/div[@class='white_title_sub']/span[@class='right']/a
        teacher = sel[3]/div[@class='white_title_sub']/span[@class='right']/span[@class='teacher']
        location = sel[3]/div[@class='specifications']/div[@class='specific'][2]/span[@class='sp_left']
        hours = sel[3]/div[@class='specifications']/div[@class='specific'][1]/span[@class='sp_left']
        """

        for sel in response.xpath("/html/body/div[@id='wrapper']/div[@class='specifications_hours']/div[@class='sub_sub_entry']"):
            item = CalendarItem()
            item['lesson'] = sel.xpath("string(div[@class='white_title_sub']/span[@class='right'])").extract()[0]
            item['teacher'] = sel.xpath("string(div[@class='white_title_sub']/span[@class='right']/span[@class='teacher'])").extract()[0]
            item['location'] = sel.xpath("string(div[@class='specifications']/div[@class='specific'][2]/span[@class='sp_left'])").extract()[0]

            hours = sel.xpath("div[@class='specifications']/div[@class='specific'][1]/span[@class='sp_left']/text()").extract()[0]
            start, end = hours.replace(' ', '').split('-')
            item['start_time'] = start
            item['end_time'] = end

            item['date'] = sel.xpath("/html/body/div[@id='wrapper']/div[@class='schedule-top']/div[@class='desktop-only']/div/text()")\
                .re('\d{2}/\d{2}/\d{4}')[0]
            yield item
