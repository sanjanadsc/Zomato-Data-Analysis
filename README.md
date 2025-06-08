# 🍽️ Zomato Data Analysis Project

## 📌 Objective
The aim of this project is to perform **Exploratory Data Analysis (EDA)** on Zomato's Bangalore restaurant dataset to derive insights into customer behavior, restaurant types, cost trends, and rating patterns.

## 🧰 Libraries Used
- **pandas** – Data manipulation and analysis  
- **numpy** – Numerical computations  
- **matplotlib** – Data visualization  
- **seaborn** – Statistical data visualization

## 🗂️ Dataset Details
- **Source**: Zomato Bangalore Restaurant Data  
- **Format**: CSV  
- **Key Columns**:
  - `rate`: Average rating of the restaurant
  - `votes`: Total votes received
  - `online_order`: Online order availability (Yes/No)
  - `approx_cost(for two people)`: Estimated cost for two
  - `listed_in(type)`: Type of restaurant

## 🔄 Data Preprocessing
- Converted rating strings like `"4.1/5"` into float  
- Handled missing values and checked data types  
- Verified structure using `.info()` and `.head()`

## 📊 Visualizations
- **Count Plot**: Frequency of restaurant types  
- **Line Plot**: Total votes across restaurant types  
- **Histogram**: Rating distribution  
- **Boxplot**: Online order vs. Ratings  
- **Cost Analysis**: Distribution of restaurant pricing

## 🧠 Insights
- Casual Dining and Quick Bites are the most common types  
- Online order availability slightly correlates with higher ratings  
- Most restaurants are rated between 3.5 and 4.5  
- Price for two usually ranges from ₹200 to ₹800

## ✅ Technologies
- Python  
- Jupyter Notebook  
- Data Visualization Libraries

#by Sanjana Singh
