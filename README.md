Project Overview

This project focuses on building a Machine Learning model to help telecom companies such as Jio, BSNL, Airtel, and Vodafone Idea (VI) identify customers who are likely to churn.

Telecom companies provide services such as:

Mobile calls

Internet / mobile data

SMS services

Broadband (Wi-Fi)

TV / cable bundles

These companies earn revenue through customer subscription plans, including monthly and yearly packages.

When a customer stops using the service or switches to another provider, it results in revenue loss for the company. This situation is known as customer churn.

The objective of this project is to build a machine learning model that can predict churn early, allowing companies to take proactive actions such as:

providing retention offers

improving customer support

offering better subscription plans

to retain customers and reduce revenue loss.

Dataset

For this project, the Telecom Customer Churn dataset was collected from Google Dataset Search.

The dataset contains information about telecom customers including:

demographic details

subscription services

billing information

service usage patterns

churn status

Work Completed So Far
1. Data Collection

Collected the Telecom Customer Churn dataset from an online dataset source.

2. Data Loading

Loaded the dataset into Python using the Pandas library.

import pandas as pd

pd_df = pd.read_csv("Telecom_dataset.csv")
3. Data Inspection

Performed an initial understanding of the dataset.

The following checks were performed:

dataset shape

column names

data types

first and last rows

statistical summary

missing values

duplicate rows

Data inspection helps in understanding the structure and quality of the dataset before performing further preprocessing.

4. Data Cleaning

Performed several preprocessing steps to make the dataset suitable for analysis and modeling:

Removed data leakage columns such as Churn Reason and Churn Category

Handled missing values

Checked and removed duplicate rows

Verified data types

Removed irrelevant features such as location-based columns

Performed feature consistency checks

These steps help ensure the dataset is accurate, consistent, and ready for analysis.

5. Exploratory Data Analysis (EDA)

EDA was performed to understand patterns and distributions within the dataset.

So far the following analyses have been completed:

Target Analysis

Analyzed the distribution of the Churn variable

Observed that the dataset is moderately imbalanced

Univariate Analysis

Analyzed individual features to understand their distributions and characteristics.

Both numerical and categorical features were explored using:

statistical summaries

histograms

count plots

Insights were generated for important features such as:

Age

Monthly Charges

Tenure in Months

Number of Referrals

Total Revenue

Internet usage features

Next Steps

The following stages will be implemented next:

Bivariate Analysis

Multivariate Analysis

Feature Engineering

Machine Learning Model Training

Model Evaluation
