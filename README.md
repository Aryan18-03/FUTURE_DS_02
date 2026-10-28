# 📊 Customer Retention & Churn Analysis Dashboard
### Turning Customer Data into Actionable Insights 🚀

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---



## 🚀 Live Dashboard

🔗 **[View Interactive Customer Churn Dashboard](https://futureds02-fspddyqyn24796tatf2wuf.streamlit.app/)**

Explore customer churn patterns, retention metrics, contract types, payment methods, and key business insights through an interactive dashboard.



## 📌 Project Overview
Customer churn occurs when customers stop using a company's products or services. Understanding customer behavior helps businesses identify retention risks and make informed decisions.

This project analyzes the Telco Customer Churn dataset using Python, Pandas, and Plotly. An interactive Streamlit dashboard presents important customer churn patterns and retention insights.

## 🎯 Project Objectives
- 📉 Measure customer churn and retention rates.
- 📄 Compare churn across contract types.
- ⏳ Analyze the relationship between tenure and churn.
- 💳 Explore churn patterns across payment methods.
- 🌐 Compare churn across internet service categories.
- 📊 Present findings through interactive visualizations.

## 🛠️ Tools & Technologies
| Technology | Purpose |
|---|---|
| 🐍 Python | Data analysis and processing |
| 🐼 Pandas | Data cleaning and manipulation |
| 📓 Jupyter Notebook | Exploratory data analysis |
| 📊 Plotly | Interactive visualizations |
| 🚀 Streamlit | Interactive dashboard |

## 📂 Project Structure
```text
FUTURE_DS_02/
├── app.py
├── Customer_Churn_Analysis.ipynb
├── Telco-Customer-Churn.csv
├── requirements.txt
└── README.md
```

## 📈 Key Findings

1. **📉 Overall Customer Churn:** Out of 7,032 customers in the cleaned dataset, 1,869 had left the service. This represents a churn rate of **26.58%**, while **73.42%** of customers stayed.

2. **📄 Contract Type and Churn:** Month-to-month customers had a churn rate of **42.71%**, compared with **11.28%** for one-year contracts and **2.85%** for two-year contracts. This shows a clear relationship between contract type and customer churn.

3. **⏳ Customer Tenure:** Customers who left had a median tenure of **10 months**, whereas customers who stayed had a median tenure of **38 months**. This suggests that retaining customers during the early stages of their relationship is particularly important.

4. **💰 Monthly Charges:** Customers who left paid an average monthly charge of **74.44**, compared with **61.31** for customers who stayed. Pricing and perceived service value may be worth investigating.

5. **💳 Payment Methods:** Electronic-check users had the highest churn rate among payment methods at **45.29%**, compared with **15.25%** for customers using automatic credit card payments.

6. **🌐 Internet Service:** Approximately **41.9%** of fiber optic customers left the service, compared with **19.0%** of DSL customers and **7.4%** of customers without internet service.

7. **👥 Senior Citizens:** The churn rate was **41.68%** among senior citizens and **23.65%** among non-senior citizens. This difference highlights a customer group whose service experience may deserve further attention.

8. **🔎 Combined Risk Factors:** Customers with both month-to-month contracts and fiber optic internet had a churn rate of approximately **54.6%** in the analyzed dataset. Examining multiple customer characteristics together can reveal patterns that may not be obvious when considering each factor separately.

## 💡 Recommendations

1. **📄 Focus on Month-to-Month Customers:** Offer suitable long-term plans, loyalty benefits, or special offers to encourage these customers to stay.

2. **🤝 Pay More Attention to New Customers:** Regularly check whether new customers are satisfied and help them resolve problems early.

3. **💳 Investigate Electronic-Check Payments:** Explore whether billing issues, payment difficulties, or other concerns are associated with the higher churn rate among electronic-check users.

4. **🌐 Improve the Fiber Optic Customer Experience:** Review feedback about pricing, internet quality, and technical support to better understand why more customers in this group are leaving.

5. **👥 Make Support Easier for Senior Customers:** Provide clear billing information and accessible customer support so customers can get help when they need it.

6. **📊 Monitor Customer Churn Regularly:** Track churn rate, retention rate, contract types, tenure, payment methods, and internet services to identify changes in customer behavior.

7. **🧪 Test Retention Strategies:** Collect customer feedback and test different retention offers to determine which actions are most effective at encouraging customers to stay.

## 🚀 How to Run the Dashboard

**Step 1: Clone the repository**
```bash
git clone https://github.com/Aryan18-03/FUTURE_DS_02.git
```

**Step 2: Open the project folder**
```bash
cd FUTURE_DS_02
```

**Step 3: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Launch the dashboard**
```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to explore the dashboard.

## 📁 Dataset
The project uses the Telco Customer Churn dataset, which contains customer information, subscribed services, billing details, contract types, and churn status.

## 👨‍💻 About Me
Hi! I'm Aryan, an aspiring Data Analyst pursuing a BCA in Data Science.

I'm developing practical skills in Python, SQL, Excel, Power BI, Tableau, and data visualization. I enjoy exploring datasets, identifying patterns, and turning data into meaningful business insights.

This project is part of my Data Science & Analytics learning journey with Future Interns.

## 🔗 Connect With Me
- 💼 **LinkedIn:** https://www.linkedin.com/in/aryan-data-analyst183/
- 🐙 **GitHub:** https://github.com/Aryan18-03

⭐ If you find this project useful, consider giving the repository a star!

---

### 🌱 Learning • Building • Improving

*Note: These findings describe patterns in the analyzed dataset. They do not independently establish the causes of customer churn or guarantee that the recommended actions will improve retention.*
