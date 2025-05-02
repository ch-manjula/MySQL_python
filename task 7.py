#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create the sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Insert some sample data
sample_data = [
    ('Apples', 10, 0.50),
    ('Oranges', 5, 0.75),
    ('Bananas', 8, 0.30),
    ('Apples', 7, 0.50),
    ('Oranges', 6, 0.75),
    ('Bananas', 4, 0.30)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

# Commit and close
conn.commit()
conn.close()


# In[5]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('sales_data.db')

# Run SQL query
query = '''
    SELECT 
        product, 
        SUM(quantity) AS total_qty, 
        SUM(quantity * price) AS revenue 
    FROM sales 
    GROUP BY product
'''
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print the results
print("Sales Summary:")
print(df)

# Plot the revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.ylabel('Revenue ($)')
plt.title('Revenue by Product')
plt.tight_layout()

# Show the chart
plt.show()

# Optional: Save the chart
# plt.savefig("sales_chart.png")


# In[ ]:




