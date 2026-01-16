🏠 House Prices Data Cleaning & Missing Value Handling
📌 Project Overview

This project focuses on data cleaning and missing value handling using the House Prices dataset.
The goal is to prepare a high-quality dataset suitable for data analysis and machine learning by identifying, visualizing, and handling missing values effectively.

🛠️ Tools & Technologies

Python 3

Pandas

NumPy

Matplotlib

Jupyter Notebook

📂 Dataset

Dataset Name: House Prices Dataset

Source: Kaggle (House Prices – Advanced Regression Techniques)

Input File: train (1).csv

Output File: house_prices_cleaned.csv

🧹 Data Cleaning Steps

Load Dataset

Loaded CSV file using Pandas.

Inspected structure using head(), tail(), and info().

Identify Missing Values

Used isnull().sum() to count missing values.

Calculated percentage of missing values per column.

Visualize Missing Data

Plotted bar charts to understand missing value distribution.

Feature Type Separation

Numerical columns (int64, float64)

Categorical columns (object)

Handle Missing Values

Numerical Features: Median imputation

Categorical Features: Mode imputation

Remove Highly Incomplete Columns

Dropped columns with more than 40% missing values.

Validation

Verified zero missing values after cleaning.

Compared dataset shape before and after cleaning.

Export Cleaned Dataset

Saved final dataset as house_prices_cleaned.csv.

📁 Project Structure
House-Prices-Data-Cleaning/
│
├── House_Prices_Data_Cleaning.ipynb
├── house_prices_cleaned.csv
├── train (1).csv
└── README.md

✅ Deliverables

✔ Cleaned Dataset File – house_prices_cleaned.csv

✔ Jupyter Notebook with Cleaning Steps – House_Prices_Data_Cleaning.ipynb

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/your-username/House-Prices-Data-Cleaning.git


Open the notebook:

jupyter notebook House_Prices_Data_Cleaning.ipynb


Run all cells to reproduce the results.

📊 Results

All missing values successfully handled.

Reduced dataset size by removing highly incomplete features.

Final dataset is clean, consistent, and analysis-ready.
