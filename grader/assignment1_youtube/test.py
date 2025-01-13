import pandas as pd
import json

file = 'USvideos.csv'
vdo_df = pd.read_csv(file)

vdo_df.drop_duplicates(inplace=True)
# count non-NA cells for each columnn or row
print(vdo_df.count())

condition = (vdo_df['trending_date'] == '18.22.01') & (vdo_df['comment_count'] > 10000)


# Q3
print(vdo_df[condition].count()[0])


# Q4
print(vdo_df.groupby('trending_date')['comment_count'].mean().idxmin())


# Q5


jn = 'US_category_id.json'
with open(jn) as f:
    data = json.load(f)

cat_list = []
for d in data['items']:
   cat_list.append((int(d['id']), d['snippet']['title'])) 

cat_df = pd.DataFrame(cat_list, columns=['id', 'category'])

# print(cat_df.head(1))
vdo_df_withcat = vdo_df.merge(cat_df, left_on='category_id', right_on='id')

vdp_df_withcat = vdo_df_withcat.groupby(['trending_date', 'category'])['views'].sum()

print(vdp_df_withcat.head(5))
print(";----------'")

vdp_df_withcat = vdp_df_withcat.groupby(['trending_date'])

print(vdp_df_withcat.head(5))

cnt = 0
for a in vdp_df_withcat:
    # print(a[1].keys())
    # print(a[1][a[0]]['Sports'])
    # print(a[1].values())
    if(a[1][a[0]]['Sports'] > a[1][a[0]]['Comedy']):
        cnt += 1

print(cnt)
