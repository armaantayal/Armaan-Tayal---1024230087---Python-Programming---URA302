# Worksheet 6 – Pandas Solutions (Q1–Q8)
import pandas as pd

# Q1: Pandas basics
print(pd.__version__)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Q2: Series
S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)
print(S1.iloc[1], S1.iloc[3])

S2 = pd.Series([10, 20, 30, 40, 50])
print(S1 + S2)

# Q3: DataFrame basics
print(df[["Name", "City"]])

df["Salary"] = [50000, 60000, 70000]
print(df)

print("Average Age:", df["Age"].mean())
print("Total Salary:", df["Salary"].sum())

# Q4: Filtering and indexing
print(df[df["Age"] > 28])

df_indexed = df.set_index("Name")
print(df_indexed)
print(df_indexed.reset_index())

# Q5: CSV data (employees.csv should exist)
emp_df = pd.read_csv("employees.csv")
print(emp_df)

filtered = emp_df[emp_df["Salary"] > 55000]
print(filtered[["Name", "Department"]])

# Q6: Grouping and aggregation
print(emp_df.groupby("Department")["Salary"].mean())
print(emp_df.groupby("Department")["Salary"].agg(["min", "max"]))

# Q7: Merging DataFrames
df1 = pd.DataFrame({
    "Name": ["John", "Jane", "Emily"],
    "Department": ["Sales", "Marketing", "HR"]
})
df2 = pd.DataFrame({
    "Name": ["John", "Jane", "Emily"],
    "Experience (Years)": [5, 7, 3]
})

merged = pd.merge(df1, df2, on="Name")
print(merged)

# Q8: Sorting
sorted_df = merged.sort_values(by="Experience (Years)", ascending=False)
print(sorted_df)
