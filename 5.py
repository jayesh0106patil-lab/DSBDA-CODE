# Practical-5: Logistic Regression on Social_Network_Ads Dataset

# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Step 2: Load Dataset
df = pd.read_csv('Social_Network_Ads.csv')

# Display dataset summary
print("--- Dataset Statistical Summary ---")
print(df.describe())

# Step 3: Data Preprocessing
# Selecting Features (Age, EstimatedSalary) and Target (Purchased)
X = df.iloc[:, [2, 3]].values
y = df.iloc[:, 4].values

# Splitting dataset into Training and Testing (75% train, 25% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print("Data Preprocessing and Scaling Complete.")

# Step 4: Train Logistic Regression Model
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Step 5: Prediction
y_pred = classifier.predict(X_test)

# Step 6: Confusion Matrix & Metrics
cm = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = cm.ravel()

accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Step 7: Display Results
print("\n--- Confusion Matrix ---")
print(f"True Positives (TP): {TP}")
print(f"False Positives (FP): {FP}")
print(f"True Negatives (TN): {TN}")
print(f"False Negatives (FN): {FN}")

print("\n--- Performance Metrics ---")
print(f"Accuracy: {accuracy:.4f}")
print(f"Error Rate: {error_rate:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
