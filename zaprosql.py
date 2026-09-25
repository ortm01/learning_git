import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://artem:1234@localhost:5432/mydb')
query = """
SELECT 
    name,
    dept_id,
    salary,
    SUM(salary) OVER (
        PARTITION BY dept_id 
        ORDER BY salary DESC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM stafs
WHERE dept_id IS NOT NULL;
"""
df = pd.read_sql(query, engine)
print(df)
print('='*30)
print(df[df['salary'] > 3000])