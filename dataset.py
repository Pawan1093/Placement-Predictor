import pandas as pd 
import numpy as np

np.random.seed(42)
n = 200

cgpa = np.round(np.random.uniform(5.0 , 10.0 , n) , 2)

aptitude_score = np.random.randint(40 , 100 , n)
communication_score = np.random.randint(40 , 100 , n)
projects_done = np.random.randint(0 , 6 , n)

internship = np.random.randint(0,2,n)

placement_score = (
    cgpa * 5 +
    aptitude_score * 0.3 +
    communication_score * 0.3 +
    projects_done * 2 +
    internship * 10 +
    np.random.normal(0, 5, n)
)

placed = (placement_score > 72).astype(int)

salary = (
    cgpa * 40000 +
    aptitude_score * 1000 +
    communication_score * 800 +
    projects_done * 15000 +
    internship * 50000 +
    np.random.normal(0, 20000, n)
)


salary = np.round(np.clip(salary , 25000 , 1800000) , -3)

salary_lpa = np.round(salary/100000 , 2)


df = pd.DataFrame({
    'cgpa': cgpa,
    'aptitude_score': aptitude_score,
    'communication_score': communication_score,
    'projects_done': projects_done,
    'internship': internship,
    'placed': placed,
    'salary_lpa': salary_lpa
})

df.to_csv('dataset.csv', index=False)

print("Dataset created successfully!")
print(df.head())

