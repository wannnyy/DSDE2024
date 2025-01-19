import pandas as pd
from sklearn.model_selection import train_test_split

"""
    ASSIGNMENT 2 (STUDENT VERSION):
    Using pandas to explore Titanic data from Kaggle (titanic_to_student.csv) and answer the questions.
    (Note that the following functions already take the Titanic dataset as a DataFrame, so you don’t need to use read_csv.)

"""


def Q1(df):
    """
        Problem 1:
            How many rows are there in the "titanic_to_student.csv"?
    """
    # TODO: Code here
    return df.shape[0]


def Q2(df):
    '''
        Problem 2:
            Drop unqualified variables
            Drop variables with missing > 50%
            Drop categorical variables with flat values > 70% (variables with the same value in the same column)
            How many columns do we have left?
    '''
    # TODO: Code here
    tmp = df.isnull().sum()/df.shape[0]
    df = df.drop(columns = tmp[tmp > 0.5].index)
    for col in df.columns:
        if(df[col].dtype == 'object'):
            proportions = df[col].value_counts(normalize=True, dropna=True)
            # print(proportions)
            if any(proportions > 0.7):
                # print(col)
                df.drop(columns=[col],inplace=True)
    return df.shape[1]

def Q3(df):
    '''
       Problem 3:
            Remove all rows with missing targets (the variable "Survived")
            How many rows do we have left?
    '''
    # TODO: Code here
    return df[~df['Survived'].isnull()].shape[0]


def Q4(df):
    '''
       Problem 4:
            Handle outliers
            For the variable “Fare”, replace outlier values with the boundary values
            If value < (Q1 - 1.5IQR), replace with (Q1 - 1.5IQR)
            If value > (Q3 + 1.5IQR), replace with (Q3 + 1.5IQR)
            What is the mean of “Fare” after replacing the outliers (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here

    col = 'Fare'

    # print(df[col].mean())

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1   

    idx = df[df[col] > q3 + 1.5*iqr].index

    df.loc[idx,col] = q3 + 1.5*iqr

    idx = df[df[col] < q1 - 1.5*iqr].index

    df.loc[idx,col] = q1 - 1.5*iqr

    return round(df[col].mean(),2)


def Q5(df):
    '''
       Problem 5:
            Impute missing value
            For number type column, impute missing values with mean
            What is the average (mean) of “Age” after imputing the missing values (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here

    col = 'Age'
    idx = df[col].isnull()

    df.loc[idx,col] = df[col].mean()
    return round(df.loc[idx,col].mean(),2)


def Q6(df):
    '''
        Problem 6:
            Convert categorical to numeric values
            For the variable “Embarked”, perform the dummy coding.
            What is the average (mean) of “Embarked_Q” after performing dummy coding (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    dummies = pd.get_dummies(df['Embarked'], prefix='Embarked')

    df['Embarked_Q'] = dummies['Embarked_Q']

    return round(df['Embarked_Q'].mean(),2)



def Q7(df):
    '''
        Problem 7:
            Split train/test split with stratification using 70%:30% and random seed with 123
            Show a proportion between survived (1) and died (0) in all data sets (total data, train, test)
            What is the proportion of survivors (survived = 1) in the training data (round 2 decimal points)?
            Hint: Use function round(_, 2), and train_test_split() from sklearn.model_selection, 
            Don't forget to impute missing values with mean.
    '''
    # print(df['Survived'])
    # df.drop(index=df[df['Survived'].isnull()].index,inplace=True)
    # df = df.dropna(subset=['Survived'])
    train, test = train_test_split(df, test_size=0.3, random_state=123,stratify=df['Survived'])

    # train['Survived'].sum()/train.shape[0]
    return round(train['Survived'].value_counts()[1]/train.shape[0],2)
 