## Page 1

Practical Lab: Data Handling and Preprocessing for Machine
Learning
Part 0: Setup
Import the required libraries.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
Part 1: Load and Explore the Dataset
data = {
"median_income": [3.2, 5.1, 2.8, 7.3, 4.0],
"total_rooms": [880, 7099, 1467, 1274, 1627],
"housing_median_age": [15, 25, 8, 12, 30],
"ocean_proximity": ["NEAR BAY", "INLAND", "INLAND", "NEAR OCEAN", "ISLAND"]
}
df = pd.DataFrame(data)
df
Part 2: Ordinal Encoding
ordinal_encoder = OrdinalEncoder()
df["ocean_encoded"] = ordinal_encoder.fit_transform(df[["ocean_proximity"]])
df
Part 3: One-Hot Encoding
onehot_encoder = OneHotEncoder(sparse=True)
encoded = onehot_encoder.fit_transform(df[["ocean_proximity"]])
encoded.toarray()
Part 4: Feature Scaling
X = df.drop("median_income", axis=1)
y = df["median_income"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X[["total_rooms", "housing_median_age"]])
X_scaled
Part 5: Pipelines

## Page 2

num_features = ["total_rooms", "housing_median_age"]
cat_features = ["ocean_proximity"]
num_pipeline = Pipeline([
("scaler", StandardScaler())
])
cat_pipeline = Pipeline([
("onehot", OneHotEncoder())
])
full_pipeline = ColumnTransformer([
("num", num_pipeline, num_features),
("cat", cat_pipeline, cat_features)
])
X_prepared = full_pipeline.fit_transform(X)
X_prepared
Part 6: Custom Transformer
class RoomsPerAgeAdder(BaseEstimator, TransformerMixin):
def __init__(self, add_feature=True):
self.add_feature = add_feature
def fit(self, X, y=None):
return self
def transform(self, X):
if not self.add_feature:
return X
rooms_per_age = X[:, 0] / X[:, 1]
return np.c_[X, rooms_per_age]
Part 7: Avoiding Data Leakage
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train_prepared = full_pipeline.fit_transform(X_train)
X_test_prepared = full_pipeline.transform(X_test)
