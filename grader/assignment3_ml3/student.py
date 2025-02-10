import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd

class Clustering:
    def __init__(self, file_path):  # DO NOT modify this line
        # Add other parameters if needed
        self.file_path = file_path
        self.df = None  # Parameter for loading CSV

        self.scaler = StandardScaler()
        self.mean_imp = SimpleImputer(strategy="mean")
        self.centroids = None  # Fixed typo

    def Q1(self):  # DO NOT modify this line
        """
        Step1-4
            1. Load the CSV file.
            2. Choose edible mushrooms only.
            3. Only the variables below have been selected to describe the distinctive
               characteristics of edible mushrooms:
               'cap-color-rate','stalk-color-above-ring-rate'
            4. Provide a proper data preprocessing as follows:
                - Fill missing with mean
                - Standardize variables with Standard Scaler
        """
        df = pd.read_csv(self.file_path)
        df = df[df["label"] == "e"]
        df = df[["cap-color-rate", "stalk-color-above-ring-rate"]]

        # Fill missing values with mean
        df = pd.DataFrame(self.mean_imp.fit_transform(df), columns=df.columns)

        # Standardize features
        df = pd.DataFrame(self.scaler.fit_transform(df), columns=df.columns)

        self.df = df  # Store for later use

        return df.shape

    def Q2(self):  # DO NOT modify this line
        """
        Step5-6
            5. K-means clustering with 5 clusters (n_clusters=5, random_state=0, n_init='auto')
            6. Show the maximum centroid of 2 features ('cap-color-rate' and 'stalk-color-above-ring-rate') in 2 digits.
        """
        if self.df is None:
            self.Q1()

        kmeans = KMeans(n_clusters=5, random_state=0, n_init="auto")
        kmeans.fit(self.df)

        self.centroids = kmeans.cluster_centers_

        return np.round(self.centroids.max(axis=0), 2)

    def Q3(self):  # DO NOT modify this line
        """
        Step7
            7. Convert the centroid value to the original scale, and show the minimum centroid of 2 features in 2 digits.
        """
        if self.centroids is None:
            self.Q2()

        org_centroids = self.scaler.inverse_transform(self.centroids)

        return np.round(org_centroids.min(axis=0), 2)
