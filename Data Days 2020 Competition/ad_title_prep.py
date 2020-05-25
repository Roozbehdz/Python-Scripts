
import pandas as pd


ad_title = pd.read_csv(r'D:\datadays2020_contest_public_dataset\ad_title.csv')

wordId_list = list(sorted(set(ad_title['wordId'])))

columns = [('word_'+(str(x))) for x in wordId_list]

adId_list = list(sorted(set(ad_title['adId'])))

dictionary = dict(zip(columns, wordId_list))

columns = ['adId'] + columns

new_ad_title = pd.DataFrame(columns=columns)

# function to return key for any value
def get_key(val):
    for key, value in dictionary.items():
         if val == value:
             return key

    return "key doesn't exist"


for adId in adId_list:
    
    words_in_ad = list(sorted(ad_title[ad_title['adId'] == adId]['wordId']))
    
    temp_dict = {"adId": adId}
    
    for word in words_in_ad:
        temp_dict.update([(str(get_key(word)), True)])

    new_ad_title = new_ad_title.append(temp_dict,ignore_index=True)

new_ad_title.fillna(False, inplace=True)
new_ad_title.to_csv('new_ad_title.csv')
