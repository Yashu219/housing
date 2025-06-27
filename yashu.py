import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv(r"E:\internship\task3\Housing.csv")
  # Use your actual filename
print(df.head())
print(df.info())

# Convert categorical variables (like yes/no)
df.replace({'yes': 1, 'no': 0}, inplace=True)

# Select features and target
X = df[['area', 'bedrooms', 'bathrooms']]  # Multiple regression
y = df['price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Plotting
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted")
plt.grid(True)
plt.show()

# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
