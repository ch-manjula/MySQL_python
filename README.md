# MySQL_python
# Sales Data Analysis with SQLite and Python

This simple project demonstrates how to use **SQLite** with **Python** to analyze sales data using SQL queries, display the output in the terminal, and visualize results using **matplotlib**.

## 🧰 Tools Used

- Python (standard installation)
- SQLite (`sqlite3` module — built into Python)
- pandas
- matplotlib

## 📁 Files Included

- `create_sales_db.py` – Creates the SQLite database and inserts sample sales data.
- `analyze_sales.py` – Connects to the database, runs a SQL query, displays the result, and plots a bar chart.
- `sales_data.db` – The SQLite database file (created by `create_sales_db.py`).
- `README.md` – This file.

## 🗂️ Sales Table Structure

| Column  | Type    | Description             |
|---------|---------|-------------------------|
| id      | INTEGER | Primary key             |
| product | TEXT    | Name of the product     |
| quantity| INTEGER | Quantity sold           |
| price   | REAL    | Price per unit          |

## 📊 Sample Data

| Product  | Quantity | Price |
|----------|----------|-------|
| Apples   | 10       | 0.50  |
| Oranges  | 5        | 0.75  |
| Bananas  | 8        | 0.30  |
| Apples   | 7        | 0.50  |
| Oranges  | 6        | 0.75  |
| Bananas  | 4        | 0.30  |

## 🚀 How to Run

### 1. Create the Database

Run this script to create `sales_data.db` and populate it with sample data:

```bash
python create_sales_db.py

2. Analyze Sales and View Chart
Run the analysis script to:

Query total quantity and revenue per product

Display results in terminal

Show a bar chart using matplotlib

python analyze_sales.py
Printed Output:
Sales Summary:
  product  total_qty  revenue
0  Apples         17     8.50
1 Bananas         12     3.60
2 Oranges         11     8.25

