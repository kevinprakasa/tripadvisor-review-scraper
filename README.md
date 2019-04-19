# tripadvisor-review-scraper

![alt text](https://3rxg9qea18zhtl6s2u8jammft-wpengine.netdna-ssl.com/wp-content/uploads/2017/06/tripadvisor-logo-e1526649519797.png "Trip Advisor")
![alt text](https://imgur.com/RMomBm2.png "Occassion reviews")

## What is this repo?
Thanks to my academical course which forced me to find a way to scrap reviews from an occassion from tripadvisor.com. I found it hard and no one has built and shared their code on internet, so I think it's good to share my way that worked for me.
This repo is a python Selenium based script to scrape certain link on tripadvisor 

## How to setup and run this project?
1. Clone this project
2. Setup virtual env (optional)
```bash
virtualenv env
```
3. Activate env if you do the step two
```bash
source env/bin/activate
```
4. Install needed python package
```bash
pip install -r requirements.txt
```
5. Comment sample url on **crawler.py** and fill urls with your trip advisor occasion url, 
```python
urls = {
  "<key_that_will_be_file_txt_name>": "occassion_url_where_we_scrape_reviews",
  "<key_that_will_be_file_txt_name1>": "occassion_url_where_we_scrape_reviews1"
}
```
6. Run crawler.py 
```bash 
python crawler.py
```
7. Voila! just wait selenium running to scrape the reviews from page one till the end of page of its pagination
8. Scrape result can be seen on the same path with **crawler.py** and on the .txt format file

## What will you get from the crawler?
You will get a txt file which have all the reviews from certain url or occasion link. 
Name of the file will be the key name that you set on **urls** variable.
The txt file will have the reviews separated by 
```
=============<no,pageNo,rating> <1,1,40>===============
```
1. no: is number of the review on its page (page can be 1,2,3,4,5, based from total reviews)
2. pageNo: is the number of page where its review belong
3. rating: is the number of its review rating

## Conclusion
Thanks for reading my repo, any issues, pull request, questions, and whatever are welcomed! Hope this repo can help you and can guide me to contribute in this open source world! Thankyou! 
