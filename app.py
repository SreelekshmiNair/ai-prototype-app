import streamlit as st
import pandas as pd

# --- Simulated database ---
data = {
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "role": ["Engineer", "Designer", "Manager", "Intern"],
    "salary": [70000, 65000, 90000, 40000]
}
df = pd.DataFrame(data)

st.title("AI Data Assistant Prototype")
st.write("This prototype lets you ask questions about our dataset!")

user_input = st.text_input("Ask me something about the data:")

if user_input:
    user_input_lower = user_input.lower()
    
    if "who" in user_input_lower and "highest" in user_input_lower:
        highest_paid = df.loc[df['salary'].idxmax()]
        answer = f"The highest paid employee is {highest_paid['name']} with a salary of ${highest_paid['salary']}."
    elif "average" in user_input_lower and "salary" in user_input_lower:
        avg_salary = df['salary'].mean()
        answer = f"The average salary is ${avg_salary:.2f}."
    else:
        answer = "Sorry, I can only answer questions about salaries or highest paid employees in this prototype."

    st.write(answer)

if st.checkbox("Show data table"):
    st.dataframe(df)
