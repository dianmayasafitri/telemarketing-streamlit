# Predictive Leads Scoring for Bank Term Deposit Campaigns

## 1. Project Overview

This project focuses on improving the effectiveness of telemarketing campaigns for term deposits in Portugal by leveraging data-driven insights and predictive modeling. Banks face low conversion rates despite attractive deposit offers, high operational costs, and inefficient targeting. This project applies exploratory data analysis (EDA) and machine learning to predict which customers are most likely to convert, enabling smarter resource allocation and maximizing campaign ROI.

---

## 2. Background

Portugal’s term deposit campaigns rely heavily on telemarketing.

* Despite attractive interest rates, only ~11% of contacted customers convert
* Large datasets contain information on demographics, past interactions, and macroeconomic indicators
* The key challenge is identifying patterns in customer behavior to predict high-potential leads and reduce wasted effort and cost

**Key Stakeholders**:

* **Marketing / Telemarketing Division** – executes campaigns
* **Sales Agents** – convert leads into deposits
* **Finance / CFO** – monitors costs, ROI, and CPA

---

## 3. Problem Statement

Low conversion rates indicate the need for better targeting.

**Key Questions**:

* How do demographics, contact history, and macroeconomic factors affect customer responses?
* Which age or generational segments have higher conversion potential?
* How effective are communication channels, call frequency, and call duration?
* How can we predict conversion probability using historical data to prioritize leads?

---

## 4. Data Overview

* **Source**: UCI Machine Learning Repository
* **Period**: 2014
* **Records**: 41,188 telemarketing calls
* **Features**: 20 columns including demographics, campaign information, and economic indicators
* **Target Variable**: `y` (binary — `1` = customer subscribed, `0` = not subscribed)

**Key Feature Notes**:

* `duration` excluded from predictive modeling to avoid data leakage
* `pdays = 999` indicates customer never contacted before → mapped to `-1`
* Derived features include **generation** based on age for marketing segmentation

---

## 5. Exploratory Data Analysis (EDA) Insights

* **Age**: wide range; marketing strategies should be tailored by segment
* **Call Duration**: optimal conversion between **2–5 minutes**
* **Contact Frequency**: highest conversion within the first **1–3 calls**, with diminishing returns afterward
* **First Contact vs Re-contact**: prior interactions greatly increase conversion rates (**63.8% vs 9.3%**)
* **Channel Effectiveness**: mobile channels outperform landlines
* **Economic Conditions**: macroeconomic indicators influence customers’ propensity to deposit

**Business Insights**:

* Focus on first-touch campaigns for new customers
* Prioritize previously contacted customers
* Optimize call frequency and duration to maximize engagement

---

## 6. Modelling Approach

**Models Used**:

* Random Forest
* Bagging Classifier
* Voting Classifier
* XGBoost
* LightGBM

**Preprocessing Steps**:

* Separate numeric, ordinal, and categorical features
* Impute missing values and scale numeric features using `RobustScaler`
* Encode categorical and ordinal features
* Handle class imbalance using **SMOTE**

**Evaluation Metrics**:

* **Primary**: Recall (minimizing False Negatives)
* **Secondary**: F2 Score, Precision, Accuracy

**Cross-Validation**:

* Stratified 5-fold cross-validation with SMOTE

---

## 7. Key Findings and Model Performance

* **Random Forest** outperformed other models in Recall and F2 score
* **Recall achieved**: **84.7%**, capturing most interested customers
* Cost-benefit analysis shows a **net positive impact of EUR 9,460** by prioritizing high-value leads
* Threshold tuning and feature selection optimized to minimize False Negatives (lost conversion opportunities)

---

## 8. Business Recommendations

### Priority Leads Strategy

* Contact customers with prior interactions first (`pdays ≠ -1`)
* Use predictive scores to rank leads by conversion probability

### Operational Efficiency Strategy

* Limit contacts per customer to **3–4 calls per campaign**
* Focus on optimal call duration (**150–300 seconds**)
* Prioritize mobile channels for higher conversion rates

### Model Integration Strategy

* Deploy **Random Forest** as a daily scoring system
* Provide sales agents with ranked lead lists to maximize ROI
