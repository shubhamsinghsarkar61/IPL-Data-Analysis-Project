# 🏏 IPL Match Data Analysis using Python

## 📌 Project Overview

This project performs an in-depth analysis of **Indian Premier League (IPL)** match data using Python.
The goal is to explore historical IPL datasets and extract meaningful insights about **team performance, scoring patterns, and player contributions**.

The project follows a complete **data analytics workflow** including:

* Data cleaning
* Exploratory Data Analysis (EDA)
* Data visualization

---

## 📊 Dataset Information

The project uses two datasets:

* **matches.csv** → Match-level information (season, teams, venue, winner)
* **deliveries.csv** → Ball-by-ball data for every IPL match

### 📦 Dataset Size

* **~180,000 ball-by-ball records**
* **~11,000 match-level records**

---

## 🧰 Tools & Technologies

* 🐍 **Python**
* 📊 **Pandas**
* 🔢 **NumPy**
* 📉 **Matplotlib**
* 📓 **Jupyter Notebook**

---

## 🧹 Data Cleaning & Preprocessing

The following data preparation steps were performed:

* Removed irrelevant columns (such as umpire details)
* Handled missing values in important columns such as
  **city, winner, and player_of_match**
* Verified dataset consistency after cleaning
* Created cleaned datasets for analysis

---

## 📊 Exploratory Data Analysis

Several analyses were performed to understand IPL trends:

### 🏆 Top 5 Teams with Most Wins

Identifies the most successful teams across IPL seasons.

### 🏏 Top 5 Batsmen with Highest Runs

Highlights players who contributed the most runs.

### ⏱ Total Runs Scored per Over

Analyzes scoring patterns throughout the innings.

### 📈 Runs per Over per Match

Examines run distribution across overs.

### 🎯 Winning Margin Distribution

Analyzes how matches are typically won (by wickets).

---

## 📈 Key Insights

* Certain teams consistently dominate across multiple IPL seasons.
* **Powerplay overs contribute significantly to total match runs.**
* A small group of batsmen contributes a major portion of total runs.
* Most IPL matches are won by a margin of **5–7 wickets**, indicating strong chasing performance.

---

## 📁 Project Structure

```
IPL-Data-Analysis-Project
│
├── IPL_Match_Analysis_Using_Python.ipynb
├── matches.csv
├── deliveries.csv
├── cleaned_matches.csv
├── cleaned_deliveries.csv
│
├── Top_5_Teams_with_Most_Wins.png
├── Top_5_Batsmen_with_Highest_Runs.png
├── Total_Runs_Scored_per_Over.png
├── Total_Runs_in_Per_Over.png
├── Winning_Margin_Wickets_Distribution.png
│
└── README.md
```

---

## 🚀 Results

This project demonstrates the ability to:

* Work with **large datasets (~180K records)**
* Perform **data cleaning and preprocessing**
* Conduct **exploratory data analysis**
* Generate insights using **data visualization**


## 👤 Author

**Shubham**

🎯 *Aspiring Data Analyst*

### 🧠 Skills Demonstrated
Python • Pandas • NumPy • Data Cleaning • Exploratory Data Analysis • Data Visualization
