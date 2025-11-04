# 🧠 MongoDB and Python Integration for Data Science Projects

This project demonstrates how to efficiently connect, manage, and analyze data using **MongoDB** and **Python (PyMongo)** — all within a data science workflow.  
It includes real examples, aggregation pipelines, update operations, and query optimizations designed for use in **Kaggle Notebooks** and **MongoDB Atlas** environments.

---

## 📊 Project Overview

MongoDB is a flexible NoSQL database ideal for storing large, unstructured datasets used in modern data science projects.  
This repository provides step-by-step implementations covering:
- Database creation and connection (local & Atlas)
- Data insertion and indexing
- Querying and filtering
- Update and delete operations
- Aggregation pipelines for data analysis
- Integration with `pandas` for visualization

---

## 🧩 Dataset & Objective

A synthetic dataset is created to simulate **sales data** for multiple product categories and regions.  
We use **two collections** to explore MongoDB’s analytical capabilities:
1. `sales_data` → Product-level details (category, price, quantity, revenue)
2. `region_sales` → Regional summaries by year and location

The goal is to show how MongoDB’s **Aggregation Framework** can replace complex SQL queries and help in generating analytical insights directly within the database.

---

## ⚙️ Key Steps Implemented

| Step | Description |
|------|--------------|
| 1️⃣| Connect to MongoDB (local & Atlas) using `pymongo` |
| 2️⃣| Create databases and collections dynamically |
| 3️| Insert bulk data from DataFrames |
| 4️| Create single and compound indexes for faster queries |
| 5️| Perform advanced filtering and conditional updates |
| 6️| Apply Aggregation pipelines for grouped analysis |
| 7️| Export and visualize results with `pandas` and `matplotlib` |

---

## 📂 Folder Structure

```

📦 MongoDB_Python_DataScience/
├── notebooks/        → Kaggle notebooks for exploration and analysis
├── src/              → Clean modular code (db_connect, data_ops, aggregations)
├── assets/           → Sample images, charts, and visualizations
├── results/          → Output CSVs, reports, and figures
├── models/           → Saved data models (if applicable)
├── configs/          → Configuration files (MongoDB URIs, settings)
├── logs/             → Logs and connection traces
├── README.md         → English project documentation
├── README_FA.md      → Persian project documentation
├── requirements.txt  → Required dependencies
├── .gitignore        → Ignored temporary files
└── CONTRIBUTING.md   → Contribution guidelines

````

---

## 🧰 Installation

### 1️ Clone this repository:
```bash
git clone https://github.com/<your-username>/MongoDB_Python_DataScience.git
cd MongoDB_Python_DataScience
````

### 2️ Install dependencies:

```bash
pip install -r requirements.txt
```

### 3️ Configure MongoDB Connection:

You can use either:

* **Local MongoDB** → `mongodb://localhost:27017/`
* **MongoDB Atlas** → Replace the URI with your Atlas cluster connection string in the config file

---

## 📈 Results & Visualizations

MongoDB’s aggregation pipeline allows concise analytical queries like:

```python
pipeline = [
    {"$group": {"_id": "$category", "total_revenue": {"$sum": "$revenue"}, "avg_price": {"$avg": "$price"}}},
    {"$sort": {"total_revenue": -1}}
]
```

---

## 🔗 Kaggle Notebook

You can view the full notebook implementation here:
**[👉 Open on Kaggle](https://www.kaggle.com/code/sepehrkh/mongodb-and-python-on-kaggle-using-mongodb-atlas)**


---

## 🚀 Future Work

* Integrate **MongoDB Atlas Search** for text-based data retrieval
* Explore **MongoDB Aggregation with PySpark**
* Build **Dash/Streamlit dashboard** connected to MongoDB for real-time analytics

---

## 🧾 License

This project is licensed under the **MIT License**.
Feel free to use and modify for educational or research purposes.

---

## 📬 Contact

For questions or collaborations:
**Kaggle:**[@sepehrkh](https://www.kaggle.com/sepehrkh)
**GitHub:** [@sepehr-khb](https://github.com/sepehr-khb)
**LinkedIn:** [Sepehr Khalili](https://www.linkedin.com/in/sepehr-khalilib/)


