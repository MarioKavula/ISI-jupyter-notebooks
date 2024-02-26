# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression

# Part 1: Data Loading
wine_data = pd.read_csv('data/winequality-red.csv')

# Display the first 5 rows of the dataset
print(wine_data.head())

# Part 2: Data Exploration
wine_data.info()
plt.figure(figsize=(10, 6))
sns.countplot(x='quality', data=wine_data)
plt.title('Distribution of Wine Quality')
plt.show()

# Part 3: Data Preprocessing
# Check for missing values
print(wine_data.isnull().sum())

# No missing values in this dataset, but if there were, you would handle them here

# Feature Scaling
X = wine_data.drop('quality', axis=1)
y = wine_data['quality']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Part 4: Splitting the Dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Part 5: Model Training (Random Forest)
model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train, y_train)

# Training score
print("Training Accuracy (Random Forest):", model_rf.score(X_train, y_train))

# Part 6: Model Evaluation (Random Forest)
y_pred_rf = model_rf.predict(X_test)
print("Accuracy (Random Forest):", accuracy_score(y_test, y_pred_rf))
print("\nClassification Report (Random Forest):\n", classification_report(y_test, y_pred_rf))

# Part 7: Experimentation and Conclusion
# Trying another model for comparison: Logistic Regression
model_lr = LogisticRegression(max_iter=10000, random_state=42)
model_lr.fit(X_train, y_train)

# Training score
print("Training Accuracy (Logistic Regression):", model_lr.score(X_train, y_train))

# Model Evaluation (Logistic Regression)
y_pred_lr = model_lr.predict(X_test)
print("Accuracy (Logistic Regression):", accuracy_score(y_test, y_pred_lr))
print("\nClassification Report (Logistic Regression):\n", classification_report(y_test, y_pred_lr))

# Conclusion: Compare the performance of the two models and document findings