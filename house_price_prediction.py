# House Price Prediction using Linear Regression

# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
import os
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "kc_house_data.csv")

df = pd.read_csv(csv_path)

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Select required features
features = [
    'bedrooms',
    'bathrooms',
    'sqft_living',
    'floors',
    'waterfront',
    'view',
    'condition',
    'grade',
    'sqft_above',
    'sqft_basement',
    'yr_built',
    'zipcode'
]

# Convert location (zipcode) into numerical values
df = pd.get_dummies(df, columns=['zipcode'], drop_first=True)

# Update feature list after one-hot encoding
encoded_features = [col for col in df.columns if col.startswith("zipcode_")]
X = df.drop(columns=[
    'id',
    'date',
    'price',
    'lat',
    'long',
    'sqft_lot',
    'sqft_living15',
    'sqft_lot15',
    'yr_renovated'
], errors='ignore')

# Target variable
y = df['price']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("\nModel Performance")
print("------------------------")
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Predict the price of the first test sample
sample = X_test.iloc[[0]]
predicted_price = model.predict(sample)

print("\nPredicted House Price:", predicted_price[0])
print("Actual House Price:", y_test.iloc[0])