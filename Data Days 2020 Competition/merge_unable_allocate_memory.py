import pandas as pd

df1 = pd.read_csv("all_data.csv")
df2 = pd.read_csv("new_ad.csv")
df2_key = df2.adId

# creating a empty bucket to save result
df_result = pd.DataFrame(columns=(df1.columns.append(df2.columns)).unique())
df_result.to_csv("df3.csv", index_label=False)

# save data which only appear in df1 # sorry I was doing left join here. no need to run below two line.
# df_result = df1[df1.Colname1.isin(df2.Colname2)!=True]
# df_result.to_csv("df3.csv",index_label=False, mode="a")

# deleting df2 to save memory
del(df2)


def preprocess(x):
    df2 = pd.merge(df1, x, left_on="adId", right_on="adId")
    df2.to_csv("df3.csv", mode="a", header=False, index=False)


# chunksize depends with you colsize
reader = pd.read_csv("new_ad.csv", chunksize=1000)

[preprocess(r) for r in reader]
