# Prediction of Successful Billing for Transactions
## Capstone project for Udacity nanodegree


## Domain Background
Subscription-based businesses have become increasingly popular across industries, including entertainment, software, fitness, and e-commerce. However, one major challenge these businesses face is churn due to billing failures. Billing failures can occur for various reasons, such as expired payment methods, insufficient funds, or technical errors, and often lead to unintended subscription cancellations. According to industry reports, involuntary churn due to billing issues accounts for up to 20-40% of total subscription cancellations, representing a significant revenue loss for businesses. [1]
Academic research supports the application of ML in addressing billing-related issues. Studies in predictive analytics and churn modeling demonstrate how machine learning techniques, such as classification algorithms and time-series analysis, can enhance customer retention strategies [2]. 
This project proposes using ML predictions to address the problem of stopped subscriptions due to billing failures
##  Problem Statement
Billing failures in subscription-based models lead to significant revenue loss. Identifying which transactions are likely to recover after an initial billing failure is crucial for minimizing churn. The challenge was to develop a machine learning model that accurately predicts recovery likelihood, optimizing billing retries and reducing unnecessary operational costs.

##  Datasets and Inputs
The primary dataset for this project is the Bank Customer Churn Dataset [3], which provides information about customer demographics, account behavior, and churn status. While the dataset is designed to predict customer churn in banking, it was adapted to represent a subscription context by modifying the target variable to indicate recovery outcomes after billing failure.
This table summarizes the input features, dropped fields, and synthesized fields used in the transaction billiing prediction project. It highlights the actions taken to prepare the dataset to align with real-world constraints.

## Metrics
This project is a `binary classification` problem aimed at predicting the likelihood of a transaction recovery following a failed billing attempt. The following techniques were used to evaluate model performance


[View  Full text](Report.pdf)


## Solution architecture

![Capstone1 drawio](https://github.com/user-attachments/assets/06a09369-c1da-4e5f-8a07-ddb4873345b7)



## Resources
[1] [Understanding Involuntary Churn and How to Address It](https://optimizedpayments.com/insights/recurring/involuntary-churn-and-how-to-address-it/)  
[2] [Classifying variety of customer's online engagement for churn prediction with mixed-penalty logistic regression](https://arxiv.org/abs/2105.07671)  
[3] [Bank Customer Churn Dataset](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset?resource=download)


