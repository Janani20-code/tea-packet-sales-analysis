# 🍵 Tea Packet Sales Analysis

A real-world data analysis project built to understand and improve sales in my father's tea packet business.  
This project uses **MySQL**, and **Python (Pandas & Matplotlib)** to load, clean, analyze, and visualize sales data for better decision-making.

---

## 📌 Project Overview

- 📦 Track **product performance** across customers and shops
- 📊 Visualize **monthly profits**, top customers, and high-performing shops
- 🧹 Clean and standardize real-world data using **Pandas**
- 📈 Generate charts using **Matplotlib** and save them as images
- ✅ Designed as an end-to-end **Data Analyst portfolio project**
- 🔐 **Password handled via a helper function** imported from an earlier project (keeps credentials out of the code)
- ⚙️ **Fully automated pipeline** — run one script (`main.py`) for the entire workflow
- 📂 **Sample datasets (CSV format)** now included in the `data/` folder for reference and testing without a live MySQL setup

---

## 💡 Project Background

This project was inspired by my father's small-scale **tea packet business**.  
Initially, I managed the data in **Excel**, including profit and quantity calculations.  
Later, I migrated the data to **MySQL**, and developed this Python-based pipeline to automate analysis, create business insights, and prepare myself for real-world data analyst roles.

---

## 🛠️ Tech Stack

| Tool / Library       | Role                           |
|----------------------|--------------------------------|
| Python               | Core programming language      |
| MySQL                | Relational database            |
| Pandas               | Data cleaning & manipulation   |
| Matplotlib           | Data visualization             |
| PyCharm              | IDE for writing and testing    |

---

## 📂 Project Structure

```bash
tea_packet_sales_analysis/
├── main.py                  # Orchestrates the whole process
├── db_connection.py         # Connects to MySQL (uses helper for password)
├── data_loader.py           # Loads tables into DataFrames
├── data_cleaner.py          # Cleans & converts datatypes
├── visualizer.py            # Creates and saves charts
├── data/                    # ← Added: Contains CSV versions of MySQL tables
│   ├── customer.csv
│   ├── customersale.csv
│   ├── financesummary.csv
│   ├── product.csv
│   ├── purchase.csv
│   ├── shop.csv
│   ├── shopsale.csv
│   └── vendor.csv
├── requirements.txt         # Python dependencies
└── README.md                # ← you’re reading it
```
---

✍️ **Author**  
** V.Janani**  
Aspiring Data Analyst | Python & SQL Learner  
[LinkedIn Profile](https://www.linkedin.com/in/jananiv20)

📘 **License**  
This project is built for personal learning and portfolio demonstration.  
Feel free to fork, improve, or use the ideas in your own projects.

🙌 **Support**  
If you found this helpful or learned something new, feel free to ⭐️ star the repo!
