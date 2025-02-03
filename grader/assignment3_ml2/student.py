
import pandas as pd #e.g. pandas, sklearn, .....
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
import warnings # DO NOT modify this line
from sklearn.exceptions import ConvergenceWarning # DO NOT modify this line
warnings.filterwarnings("ignore", category=ConvergenceWarning) # DO NOT modify this line


class BankLogistic:
    def __init__(self, data_path): # DO NOT modify this line
        self.data_path = data_path
        self.df = pd.read_csv(data_path, sep=',')
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def Q1(self): # DO NOT modify this line
        """
        Problem 1:
            Load ‘bank-st.csv’ data from the “Attachment”
            How many rows of data are there in total?

        """
        # TODO: Paste your code here

        BankLogistic('bank-st.csv')
        return self.df.shape[0]

    def Q2(self): # DO NOT modify this line
        """
        Problem 2:
            return the tuple of numeric variables and categorical variables are presented in the dataset.
        """
        # TODO: Paste your code here
        # pass  
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        categorical_cols = self.df.select_dtypes(exclude=['number']).columns
        return (len(numeric_cols), len(categorical_cols))
    
    def Q3(self): # DO NOT modify this line
        """
        Problem 3:
            return the tuple of the Class 0 (no) followed by Class 1 (yes) in 3 digits.
        """
        # TODO: Paste your code here
        cnt_no = self.df['y'].value_counts()[0] 
        cnt_yes = self.df['y'].value_counts()[1]    
        total = cnt_no + cnt_yes

        return (round(cnt_no/total,3).item(), round(cnt_yes/total,3).item())
      
    

    def Q4(self): # DO NOT modify this line
        """
        Problem 4:
            Remove duplicate records from the data. What are the shape of the dataset afterward?
        """
        # TODO: Paste your code here
        
        # pass  
        self.df.drop_duplicates(inplace=True)
        return self.df.shape

        

    def Q5(self): # DO NOT modify this line
        """
        Problem 5:
            5. Replace unknown value with null
            6. Remove features with more than 99% flat values. 
                Hint: There is only one feature should be drop
            7. Split Data
            -	Split the dataset into training and testing sets with a 70:30 ratio.
            -	random_state=0
            -	stratify option
            return the tuple of shapes of X_train and X_test.

        """
        # TODO: Paste your code here

        self.Q4()

        self.df.replace('unknown', None, inplace=True)
        # norm = self.df.count() / self.df.shape[0]

        dp = []
        for col in self.df.columns:     
            norm = self.df[col].value_counts(normalize=True).max()
            if norm > 0.99:
                dp.append(col)

        self.df.drop(columns=dp, inplace=True)

        # return self.df.shape
        X = self.df.drop(columns='y')
        y = self.df['y']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
        return tuple(self.X_train.shape), tuple(self.X_test.shape)
        
       
    def Q6(self): 
        """
        Problem 6: 
            8. Impute missing
                -	For numeric variables: Impute missing values using the mean.
                -	For categorical variables: Impute missing values using the mode.
                Hint: Use statistics calculated from the training dataset to avoid data leakage.
            9. Categorical Encoder:
                Map the ordinal data for the education variable using the following order:
                education_order = {
                    'illiterate': 1,
                    'basic.4y': 2,
                    'basic.6y': 3,
                    'basic.9y': 4,
                    'high.school': 5,
                    'professional.course': 6,
                    'university.degree': 7} 
                Hint: Use One hot encoder or pd.dummy to encode ordinal category
            return the shape of X_train.

        """
        # TODO: Paste your code here
        
        self.Q5()
        # pass  
        for col in self.X_train.columns:
            if self.df[col].dtype == 'object':
                self.X_train[col].fillna(self.X_train[col].mode()[0], inplace=True)
                self.X_test[col].fillna(self.X_test[col].mode()[0], inplace=True)
                # self.y_train[col].fillna(self.y_train[col].mode()[0], inplace=True)
            else:
                self.X_train[col].fillna(self.X_train[col].mean(), inplace=True)
                self.X_test[col].fillna(self.X_test[col].mean(), inplace=True)
                # self.y_train[col].fillna(self.y_train[col].mean(), inplace=True)

        education_order = {
            'illiterate': 1,
            'basic.4y': 2,
            'basic.6y': 3,
            'basic.9y': 4,
            'high.school': 5,
            'professional.course': 6,
            'university.degree': 7
        }

        self.X_train['education'] = self.X_train['education'].map(education_order)
        self.X_test['education'] = self.X_test['education'].map(education_order)

        self.X_train = pd.get_dummies(self.X_train)
        self.X_test = pd.get_dummies(self.X_test)

        return self.X_train.shape
    
    def Q7(self):
        ''' Problem7: Use Logistic Regression as the model with 
            random_state=2025, 
            class_weight='balanced' and 
            max_iter=500. 
            Train the model using all the remaining available variables. 
            What is the macro F1 score of the model on the test data? in 2 digits
        '''
        # TODO: Paste your code here
        
        pass  
        


   