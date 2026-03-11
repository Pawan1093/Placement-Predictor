import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle


print("Loading Dataset")

df = pd.read_csv("dataset.csv")
print(f"Total students: {len(df)}")
print(df.head())

features = ['cgpa', 'aptitude_score', 'communication_score', 
            'projects_done', 'internship']
X = df[features]
y_placement = df['placed']
y_salary = df['salary_lpa']

X_train, X_test, y_train_p, y_test_p = train_test_split(
    X, y_placement, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train_p)


y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test_p, y_pred)
print(f"KNN Accuracy: {accuracy * 100:.2f}%")


X_train_lr, X_test_lr, y_train_s, y_test_s = train_test_split(
    X, y_salary, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train_lr, y_train_s)

lr_score = lr.score(X_test_lr, y_test_s)
print(f"Linear Regression R2 Score: {lr_score:.2f}")


print("Saving models...")

with open('knn_model.pkl', 'wb') as f:
    pickle.dump({'model': knn, 'scaler': scaler}, f)

with open('lr_model.pkl', 'wb') as f:
    pickle.dump(lr, f)

print("knn_model.pkl saved!")
print("lr_model.pkl saved!")
print("Training complete!")