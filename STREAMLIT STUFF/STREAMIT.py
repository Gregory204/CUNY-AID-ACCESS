import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample synthetic dataset
df = 'https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv_2024-04-18.zip'

print(df.head(5))

# # Convert categorical data to numeric
# df_encoded = pd.get_dummies(df.drop('Recommended Job', axis=1))
# labels = df['Recommended Job']

# # Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(df_encoded, labels, test_size=0.2, random_state=42)

# # Train a Decision Tree Classifier
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# # Streamlit UI
# st.title("CUNY Bot Career Recommendation")

# st.header("Enter Your Details")

# major = st.selectbox("Select Your Major", df['Major'].unique())
# skills = st.selectbox("Select Your Skills", df['Skills'].unique())
# interests = st.selectbox("Select Your Interests", df['Interests'].unique())
# work_environment = st.selectbox("Preferred Work Environment", df['Preferred Work Environment'].unique())

# if st.button("Find Recommended Career"):
#     new_student = {
#         'Major': major,
#         'Skills': skills,
#         'Interests': interests,
#         'Preferred Work Environment': work_environment
#     }
    
#     new_student_encoded = pd.DataFrame([new_student])
#     new_student_encoded = pd.get_dummies(new_student_encoded).reindex(columns=X_train.columns, fill_value=0)
    
#     predicted_job = model.predict(new_student_encoded)
    
#     st.write(f"Recommended Job: {predicted_job[0]}")

#     # Model accuracy
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     st.write(f"Model Accuracy: {accuracy * 100:.2f}%")