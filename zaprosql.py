import pandas as pd
from sqlalchemy import create_engine

# 1. Данные для подключения
# Шаблон: postgresql://логин:пароль@localhost:5432/имя_базы

engine = create_engine('postgresql://artem:1234@localhost:5432/mydb')
# 2. Наш прошлый SQL-запрос с оконной функцией
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

# 3. Чтение SQL-запроса напрямую в Pandas DataFrame
df = pd.read_sql(query, engine)

# Вывод результата в консоль
print(df)
print('='*30)
print(df[df['salary'] > 3000])