#!/usr/bin/env python
from selenium import webdriver
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReviewCrawler:
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        self.file = open('kuta-stay.txt','w')
        self.currentPageNumber = 1
        self.start_request()
    
    def start_request(self):
        urls = {
            'kuta_stay': 'https://www.tripadvisor.com/Hotel_Review-g297697-d9842370-Reviews-Kuta_Beach_Stay-Kuta_Kuta_District_Bali.html',
            'seminyak': 'https://www.tripadvisor.com/Attraction_Review-g469404-d1111882-Reviews-Seminyak_Beach-Seminyak_Kuta_District_Bali.html',
            'kuta': 'https://www.tripadvisor.com/Attraction_Review-g297697-d1772185-Reviews-Kuta_Beach_Bali-Kuta_Kuta_District_Bali.html'
        }

        for url in urls:
            self.currentPageNumber = 1
            self.file = open('{}.txt'.format(url),'w')
            page = self.driver.get(urls[url])
            logger.info('Start crawling %s' % urls[url])
            self.parse()

    def parse(self):
        try:
            taLnk = self.driver.find_elements_by_css_selector('span.taLnk.ulBlueLinks')
            if (len(taLnk) != 0):
                time.sleep(1)
                taLnk[0].click()
                time.sleep(1)
            reviews = self.driver.find_elements_by_css_selector('p.partial_entry')
            ratings = [rating.get_attribute('class').split(' ')[1].split('_')[1] for rating in self.driver.find_elements_by_css_selector('div.ui_column.is-9  span.ui_bubble_rating')]
            counter = 1
            logger.info('Write reviews on page %d' % self.currentPageNumber)
            for review,rating in zip(reviews,ratings):
                self.file.write('=============<no,pageNo,rating> <%d,%d,%s>===============  \n' % (counter,self.currentPageNumber,rating))
                self.file.write((review.text).encode('utf-8'))
                self.file.write('\n')
                counter += 1
            navNextPage = self.driver.find_elements_by_css_selector('a[data-page-number="%d"]'%(self.currentPageNumber+1))
            if (len(navNextPage) != 0):
                navNextPage[0].click()
                self.currentPageNumber += 1
                time.sleep(1)
                self.parse()
            else:
                logger.info('Crawling finished!')
        except Exception as e:
            logger.warning('Error Caught!')
            logger.warning(e)
            self.parse()

        

    def __del__(self):
        self.driver.close()

if __name__ == "__main__":
    crawler = ReviewCrawler()
    del crawler

ReviewCrawler()