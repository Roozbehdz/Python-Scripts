import pandas as pd

ad_image = pd.read_csv(r'D:\datadays2020_contest_public_dataset\ad_image.csv')

columns = ['adId']+[('imageFeature'+str(x)) for x in range(1, 513)]
new_ad_image = pd.DataFrame(columns=columns)

for i in range(len(ad_image)):

    my_string = ad_image['imageFeatures'][i]
    newstr = my_string.replace("[", "")
    newstr = newstr.replace("]", "")

    result = [x.strip() for x in newstr.split(',')]
    result = [float(x) for x in result]


    result.insert(0, ad_image['adId'][i])

    dictionary = dict(zip(columns, result))

    temp_ad_image = pd.DataFrame(dictionary, columns= columns, index=[0])

    new_ad_image = new_ad_image.append(temp_ad_image, ignore_index=True)

new_ad_image.to_csv('new_ad_image.csv')

