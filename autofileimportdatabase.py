#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pyodbc

# Import CSV - generate file from machine processing 
data = pd.read_csv (r'mention_path\result.csv')   
df = pd.DataFrame(data)
print(df)



# add your SQL server details 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=;'
                      'Database=;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table in SQL server
cursor.execute('''
CREATE TABLE result (
result_id int primary key,
machine_id nvarchar(50) 
testid nvarchar(50),
test_type nvarchar(50),
result float
)
               ''')

# Insert DF in a created table
# itertuples() : It is used to Iterate over DataFrame rows as namedtuples.

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO result (result_id, machine_id, testid ,test_type ,result )
                VALUES (?,?,?)
                ''',
                row.result_id, 
                row.machine_id,
                row.testid,
                row.test_type
                row.result
                )
conn.commit()

