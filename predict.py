import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the data
df=pd.read_csv("student_info.csv")
print(df)
# check the null value
print(df.isnull())

# sum of the null value of each column
print(df.isnull().sum().reset_index())
# define shape 
print(df.shape)
# drop the row that contan null values
df.dropna(inplace=True)
print(df)

x=df.groupby("study_hours")["student_marks"].mean().round().reset_index()
print(x)

z=x[["study_hours"]]
y=x["student_marks"]
# call the model
model = LinearRegression()
# train the model
model.fit(z,y)
# give data to predict
n=int(input("enter the study_hours of student"))
new=pd.DataFrame({"study_hours":[n]})
# give prediction 
prediction=model.predict(new)
print(prediction[0])
print(model.score(z,y))