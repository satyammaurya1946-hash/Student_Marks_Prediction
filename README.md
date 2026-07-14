# Student Marks Prediction

A simple Machine Learning project that predicts a student's marks based on the number of hours they studied, using Linear Regression.

---

## Project Overview

The goal of this project is to build a regression model that predicts a student's marks from their study hours. The data is read from a CSV file, cleaned (missing values handled), and used to train a scikit-learn Linear Regression model.

---

## Repository Contents

| File | Description |
|---|---|
| `predict.py` | Loads `student_info.csv`, checks and drops missing values, groups the data by study hours (averaging marks), trains a `LinearRegression` model, and predicts marks for a study-hours value entered by the user. |
| `Student_marks_predict.ipynb` | Notebook version of the same workflow — loading data, inspecting it (`df.info()`, null checks), cleaning it, training the model, and generating predictions. |
| `student_info.csv` | Dataset with 200 rows and two columns: `study_hours` and `student_marks` (some rows have missing `study_hours` values). |

---

## Machine Learning Workflow

1. Load the dataset (`student_info.csv`) with pandas
2. Check for and drop missing values
3. Group by `study_hours` and average the corresponding `student_marks`
4. Split into features (`study_hours`) and target (`student_marks`)
5. Train a `LinearRegression` model on the data
6. Predict marks for a new study-hours input
7. Print the model's R² score

---

## Model Used

- **Linear Regression** (`sklearn.linear_model.LinearRegression`)

Suitable for predicting a continuous value (marks) from a single numeric feature (study hours).

---

## Requirements

```bash
pip install pandas scikit-learn
```

(Use `jupyter` as well if you want to run the notebook: `pip install jupyter`)

---

## Usage

Clone the repository:

```bash
git clone https://github.com/satyammaurya1946-hash/Student_Marks_Prediction.git
cd Student_Marks_Prediction
```

Run the script (it will prompt you to enter study hours):

```bash
python predict.py
```

Or explore the workflow step-by-step in the notebook:

```bash
jupyter notebook Student_marks_predict.ipynb
```

---

## Future Improvements

- Add data visualization (e.g., scatter plot of hours vs. marks)
- Add proper train/test split and evaluation metrics (MAE, MSE, R²)
- Save the trained model for reuse
- Add a `requirements.txt`

---

## Author

**Satyam Maurya**
GitHub: [@satyammaurya1946-hash](https://github.com/satyammaurya1946-hash)
