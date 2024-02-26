# Predicting Wine Quality
In this exercise, we'll explore how to use machine learning to predict the quality of wine based on its chemical properties. We'll cover essential steps in the machine learning workflow, including data loading, preprocessing, model training, and evaluation.

## Part 1: Data Loading
First, we need to load our dataset. We'll use the Wine Quality dataset, which contains chemical properties of wine and a quality rating.

```python
import pandas as pd

# Load the dataset
wine_data = pd.read_csv('winequality-red.csv')
```

Task: Display the first 5 rows of the dataset to understand its structure. Use wine_data.head().

## Part 2: Data Exploration
Before we proceed with preprocessing, let's explore our dataset a bit.

```python
# Display basic information about the dataset
wine_data.info()
```

Task: Plot the distribution of the 'quality' variable to see how wine quality is distributed. Use libraries like matplotlib or seaborn for visualization.

## Part 3: Data Preprocessing
### Handling Missing Values
First, check for missing values and handle them if any.

```python
# Check for missing values
wine_data.isnull().sum()

# If there are any missing values, you might fill them with the mean or median of the column
# Example: wine_data['column_name'].fillna(wine_data['column_name'].mean(), inplace=True)
```

### Feature Scaling
Many machine learning models perform better when numerical input variables are scaled or normalized.

```python
from sklearn.preprocessing import StandardScaler

# Define the features and the target
X = wine_data.drop('quality', axis=1)
y = wine_data['quality']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Task: Scale the features and verify by displaying the first 5 rows of the scaled features.

## Part 4: Splitting the Dataset
Split the dataset into a training set and a testing set.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

## Part 5: Model Training
We'll use a Random Forest model to predict wine quality.

```python
from sklearn.ensemble import RandomForestClassifier

# Initialize the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)
```

Task: Train the model and print the training score.

## Part 6: Model Evaluation
Finally, let's evaluate our model on the test set.

```python
from sklearn.metrics import accuracy_score, classification_report

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

Task: Evaluate the model's performance and consider experimenting with different models or preprocessing techniques to see if you can improve the accuracy.

## Part 7: Experimentation and Conclusion
Try different machine learning models, preprocessing techniques, or feature engineering methods to improve the model's performance.

Task: Choose at least one new model to train and compare its performance with the Random Forest model. Document your findings and conclusions.
