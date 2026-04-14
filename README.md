# Customer Churn Prediction System

## Project Overview
This project focuses on predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to leave a service, enabling businesses to take proactive retention measures.

The project emphasizes not only model building but also **model evaluation and threshold optimization based on real-world business requirements**.

---

## Objective
- Predict whether a customer will churn or not  
- Minimize **False Negatives (missed churn customers)**  
- Optimize model performance based on business impact  

---

## Dataset
- Telecom customer dataset  
- Includes customer demographics, services, and account information  
- Target variable: **Churn (Yes/No)**  

---

## Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib, Seaborn  

---

## Project Workflow

### 1. Data Preprocessing
- Handled missing values  
- Encoded categorical variables  
- Scaled numerical features  

---

### 2. Model Building
Trained multiple models:
- Perceptron  
- Logistic Regression  
- Random Forest  
- SVM  
- XGBoost  

---

### 3. Model Evaluation
- Confusion Matrix  
- Accuracy, Precision, Recall, F1-score  
- ROC-AUC  

---

### 4. Threshold Optimization

#### ROC-Based Threshold
- Used **Youden’s J statistic (TPR - FPR)**  
- Provides balanced trade-off between False Positives and False Negatives  

#### Precision-Recall Based Threshold
- Selected threshold based on:
  - **High Recall (≥ 80%)**
  - Controlled Precision  
- Final threshold chosen based on business requirements  

---

## Model Performance Summary

### Best Model: XGBoost

---

### Default Threshold (0.5)


 Accuracy - 84.81% 
 Precision - 74.39% 
 Recall - 65.24% 
 F1 Score - 69.52% 

**Confusion Matrix:**
[[951 84]
[130 244]]

**Observation:**
- High precision  
- Lower recall → missing churn customers  

---

### ROC-Based Threshold (0.17)


 Accuracy -  81.83% 
 Precision - 61.01% 
 Recall - 87.43% 
 F1 Score - 71.87% 

**Confusion Matrix:**

[[826 209]
[ 47 327]]

**Observation:**
- Very high recall (excellent churn detection)  
- Increased false positives  

---

### Precision-Recall Based Threshold (0.26)  **


 Accuracy - 82.97% 
 Precision - 64.38% 
 Recall - 80.21% 
 F1 Score - 71.43% 

**Confusion Matrix:**

[[869 166]
[ 74 300]]


**Observation:**
- Balanced trade-off between precision and recall  
- Reduced false positives compared to ROC threshold  
- Maintains strong churn detection  

---

## Final Decision

The **Precision-Recall based threshold (0.26)** was selected as the final model configuration because:

- It maintains **high recall (~80%)** to reduce missed churn customers  
- Controls false positives better than ROC-based threshold  
- Aligns with **business objective of customer retention**

---

## Key Insight
Final model selection was based on business-driven threshold optimization using precision-recall trade-offs rather than relying solely on default model predictions.

## Future Improvements
- Hyperparameter tuning (GridSearch / Optuna)
