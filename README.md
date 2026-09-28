# Bank Marketing Campaign Prediction

## 📌 Project Overview

The **Bank Marketing Campaign Prediction System** is a machine learning
classification project that predicts whether a bank customer will
subscribe to a **term deposit** based on customer, financial, and
marketing-campaign information.

The project follows a complete end-to-end machine learning workflow:

> **Problem Definition → EDA → Data Preprocessing → Feature Engineering
> → Model Building → Model Evaluation → Model Improvement → Deployment**

The goal is not only to build a prediction model, but also to understand
the complete ML development process and create a model that can be
deployed for practical use.

------------------------------------------------------------------------

## 🎯 Problem Statement

Banks conduct marketing campaigns to contact customers and promote
term-deposit products. Contacting every customer equally can consume
significant time and resources.

This project aims to build a machine learning system that predicts
whether a customer is likely to subscribe to a term deposit.

### Target Variable

The target column is:

-   `y = yes` → Customer subscribed to the term deposit
-   `y = no` → Customer did not subscribe

This is a **binary classification problem**.

------------------------------------------------------------------------

## 💼 Business Objective

The model can help a bank:

-   Identify customers who are more likely to subscribe.
-   Improve marketing campaign targeting.
-   Reduce unnecessary customer contacts.
-   Support data-driven campaign decisions.
-   Improve the efficiency of telemarketing campaigns.

------------------------------------------------------------------------

## 📊 Dataset

The project uses two CSV files:

-   `train.csv`
-   `test (1).csv`

### Dataset Size

  Dataset        Rows   Columns
  ---------- -------- ---------
  Training     45,211        17
  Testing       4,521        17

The dataset contains **16 input features and 1 target variable**.

The CSV files are semicolon-separated (`;`).

### Target Distribution in Training Data

  Target      Count   Approx. Percentage
  -------- -------- --------------------
  `no`       39,922               88.30%
  `yes`       5,289               11.70%

The target is therefore **imbalanced**, so model evaluation should not
rely on accuracy alone.

------------------------------------------------------------------------

## 🧾 Features

### Customer Information

  Feature       Description
  ------------- -----------------
  `age`         Customer age
  `job`         Type of job
  `marital`     Marital status
  `education`   Education level

### Financial Information

  Feature     Description
  ----------- --------------------------------------------
  `default`   Whether the customer has credit in default
  `balance`   Average yearly balance
  `housing`   Whether the customer has a housing loan
  `loan`      Whether the customer has a personal loan

### Campaign Information

  Feature      Description
  ------------ --------------------------------------
  `contact`    Contact communication type
  `day`        Day of the month of the last contact
  `month`      Month of the last contact
  `duration`   Duration of the last contact

### Campaign History

  -----------------------------------------------------------------------
  Feature                             Description
  ----------------------------------- -----------------------------------
  `campaign`                          Number of contacts performed during
                                      the current campaign

  `pdays`                             Number of days since the customer
                                      was previously contacted

  `previous`                          Number of contacts performed before
                                      the current campaign

  `poutcome`                          Outcome of the previous marketing
                                      campaign
  -----------------------------------------------------------------------

### Target

  Feature   Description
  --------- ---------------------------------------------------
  `y`       Whether the customer subscribed to a term deposit

------------------------------------------------------------------------

## 🛠️ Technologies Used

### Programming Language

-   Python

### Data Analysis

-   Pandas
-   NumPy

### Data Visualization

-   Matplotlib
-   Seaborn

### Machine Learning

-   Scikit-learn

### Model Persistence

-   Joblib

### Deployment

-   Streamlit

------------------------------------------------------------------------

## 🔄 Machine Learning Workflow

### 1. Problem Definition

Define the business problem and identify the target variable.

**Objective:** Predict whether a customer will subscribe to a term
deposit.

------------------------------------------------------------------------

### 2. Exploratory Data Analysis (EDA)

EDA is performed to understand:

-   Dataset structure
-   Data types
-   Missing values
-   Duplicate records
-   Numerical distributions
-   Categorical distributions
-   Outliers
-   Target distribution
-   Relationships between features and target
-   Class imbalance
-   Correlations among numerical features



------------------------------------------------------------------------

### 3. Data Preprocessing

The preprocessing stage includes:

-   Separating features and target
-   Converting the target from `yes/no` to `1/0`
-   Identifying numerical and categorical features
-   Handling missing values where required
-   Standardizing numerical features
-   One-hot encoding categorical features

A `ColumnTransformer` and `Pipeline` are used so that preprocessing is
applied consistently during training and prediction.

------------------------------------------------------------------------

### 4. Feature Engineering

Additional meaningful features can be created from existing variables.

Examples include:

-   `age_group`
-   `balance_category`
-   `previously_contacted`
-   `campaign_intensity`
-   `previous_contact_intensity`

Feature engineering is used to represent useful business patterns in a
form that machine learning algorithms can learn.

------------------------------------------------------------------------

## ⚠️ Data Leakage Consideration

The `duration` feature represents the duration of the last contact.

If the system is intended to predict whether a customer should be
contacted **before the marketing call**, `duration` should not be used
because it is only known after/during the call.

Therefore, the primary pre-call prediction workflow can exclude
`duration`.

If the prediction is intended to be made after the call, the feature can
be considered.

------------------------------------------------------------------------

## 🤖 Model Building

Multiple classification algorithms can be evaluated:

1.  Logistic Regression
2.  K-Nearest Neighbors (KNN)
3.  Decision Tree
4.  Random Forest
5.  Gradient Boosting

The models are compared using the same training and testing strategy.

------------------------------------------------------------------------

## 📈 Model Evaluation

Because the target variable is imbalanced, multiple evaluation metrics
are considered.

### Accuracy

Measures the proportion of total predictions that are correct.

### Precision

Measures how many customers predicted as positive actually subscribed.

### Recall

Measures how many actual subscribers were correctly identified.

### F1-Score

Provides a balance between precision and recall.

### ROC-AUC

Measures how well the model separates positive and negative classes
across different classification thresholds.

### Confusion Matrix

Used to analyze:

-   True Positives
-   True Negatives
-   False Positives
-   False Negatives

------------------------------------------------------------------------

## 🔧 Model Improvement

Model improvement can include:

-   Cross-validation
-   Class weighting
-   Hyperparameter tuning
-   GridSearchCV
-   RandomizedSearchCV
-   Threshold tuning
-   Feature engineering
-   Model comparison

### Example Hyperparameters

For Random Forest:

-   `n_estimators`
-   `max_depth`
-   `min_samples_split`
-   `min_samples_leaf`
-   `max_features`

For KNN:

-   `n_neighbors`
-   `metric`

------------------------------------------------------------------------

## 🔍 Model Selection

The final model should be selected based on:

-   Cross-validation performance
-   Test-set performance
-   Precision
-   Recall
-   F1-score
-   ROC-AUC
-   Business requirements


Accuracy should not be used as the only selection criterion because the
dataset contains a significant class imbalance.

------------------------------------------------------------------------

## 🚀 Deployment

The trained model can be saved using Joblib:

``` python
joblib.dump(best_model, "bank_marketing_model.pkl")
```

A Streamlit application can then load the saved model and accept
customer information from the user.

### Example Application Flow

``` text
Customer Information
        ↓
Feature Engineering
        ↓
Preprocessing Pipeline
        ↓
Trained ML Model
        ↓
Prediction
        ↓
Subscription Probability
```

The application can display:

-   Predicted class
-   Subscription probability
-   Customer-level prediction result

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Bank_Marketing_Project/
│
├── train.csv
├── test (1).csv
├── Bank_Marketing_Project.ipynb
├── bank_marketing_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## ▶️ How to Run the Project

### 1. Clone the repository

``` bash
git clone <your-github-repository-url>
```

### 2. Open the project directory

``` bash
cd Bank_Marketing_Project
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Run the notebook

Open:

``` text
Bank_Marketing_Project.ipynb
```

and execute the workflow from data loading through model evaluation.

### 5. Run the Streamlit application

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 📦 Requirements

Example `requirements.txt`:

``` text
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
streamlit
```

------------------------------------------------------------------------

## 🔮 Future Improvements

Possible future improvements include:

-   Advanced ensemble models
-   Better probability calibration
-   Cost-sensitive classification
-   More detailed threshold optimization
-   Explainable AI using SHAP
-   Model monitoring after deployment
-   Automated retraining
-   Customer segmentation
-   Campaign ROI analysis

------------------------------------------------------------------------

## 👨‍💻 Author

**Yogeeswar Reddy**

Computer Science \| Data Science & Machine Learning

------------------------------------------------------------------------

## 📌 Key Learning Outcomes

Through this project, the following concepts are demonstrated:

-   Python for machine learning
-   Pandas and NumPy
-   Exploratory Data Analysis
-   Data preprocessing
-   Categorical encoding
-   Feature scaling
-   Feature engineering
-   Classification algorithms
-   Model evaluation
-   Class imbalance
-   Cross-validation
-   Hyperparameter tuning
-   Model selection
-   Model persistence
-   Streamlit deployment
