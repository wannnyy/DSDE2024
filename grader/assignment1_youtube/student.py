import pandas as pd
import json

"""
    ASSIGNMENT 1 (STUDENT VERSION):
    Using pandas to explore youtube trending data from GB (GBvideos.csv and GB_category_id.json) and answer the questions.
"""

def Q1():
    """
        1. How many rows are there in the GBvideos.csv after removing duplications?
        - To access 'GBvideos.csv', use the path '/data/GBvideos.csv'.
    """
    file = '/data/GBvideos.csv'
    vdo_df = pd.read_csv(file)

    # Drop duplicates
    # inplace=True will modify the DataFrame in place rather than returning a new DataFrame.
    vdo_df.drop_duplicates(inplace=True)

    return vdo_df.shape[0]

def Q2(vdo_df):
    '''
        2. How many VDO that have "dislikes" more than "likes"? Make sure that you count only unique title!
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    condition = vdo_df['dislikes'] > vdo_df['likes']

    # vdo_df[condition][0]
    # nunique() is used to count the number of unique values in a Series.
    return vdo_df[condition]['title'].nunique()

def Q3(vdo_df):
    '''
        3. How many VDO that are trending on 22 Jan 2018 with comments more than 10,000 comments?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - The trending date of vdo_df is represented as 'YY.DD.MM'. For example, January 22, 2018, is represented as '18.22.01'.
    '''
   
    condition = (vdo_df['trending_date'] == '18.22.01') & (vdo_df['comment_count'] > 10000)
    return vdo_df[condition].shape[0]

def Q4(vdo_df):
    '''
        4. Which trending date that has the minimum average number of comments per VDO?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    # vdo_df.groupby('trending_date')['comment_count'].mean().idxmin()

    # idxmin() is used to get the index of the first minimum value.
    return vdo_df.groupby('trending_date')['comment_count'].mean().idxmin() 

def Q5(vdo_df):
    '''
        5. Compare "Sports" and "Comedy", how many days that there are more total daily views of VDO in "Sports" category than in "Comedy" category?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - You must load the additional data from 'GB_category_id.json' into memory before executing any operations.
            - To access 'GB_category_id.json', use the path '/data/GB_category_id.json'.
    '''
    # TODO:  Paste your code here

    jn = '/data/GB_category_id.json'
    with open(jn) as f:
        data = json.load(f)
    
    cat_list = []
    for d in data['items']:
        cat_list.append((int(d['id']), d['snippet']['title'])) 

    cat_df = pd.DataFrame(cat_list, columns=['id', 'category'])

    # print(cat_df.head(1))
    vdo_df_withcat = vdo_df.merge(cat_df, left_on='category_id', right_on='id')

    vdp_df_withcat = vdo_df_withcat.groupby(['trending_date', 'category'])['views'].sum()

    vdp_df_withcat = vdp_df_withcat.groupby(['trending_date']) 

    cnt = 0
    for a in vdp_df_withcat:
        if(a[1][a[0]]['Sports'] > a[1][a[0]]['Comedy']):
            cnt += 1
    return cnt