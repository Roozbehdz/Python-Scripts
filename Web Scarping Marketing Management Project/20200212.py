#Import libraries
import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
base_url = 'https://www.sitejabber.com/reviews/uber.com'


    



def review_extractor(URL):

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    reviews_container = soup.find("review__container")
    reviews = reviews_container.select(".review__content")

    reviews = [pt.get_text('\n') for pt in reviews]
    return reviews


# print(review_extractor(URL))

reviews_1 = list()

for i in range(1,1):
    print(i)
    # url = base_url + '?page=' + str(i) + '#sort=recent&filter=none'
    url = base_url
    reviews_1 = reviews_1 + review_extractor(url)

print(((reviews_1)))
reviews_1 = pd.DataFrame(reviews_1)
reviews_1.to_csv('file2.csv')

