import pandas as pd
import random
from faker import Faker
fake=Faker()
departments=['HR','IT','CS','DS']
regions=['North','South','east','west']
data=[]
#generating random data using faker module
for i in range(500):
    data.append({
        'ID': i + 1,
        'Name': fake.name(),
        'Age': random.randint(20, 60),
        'Gender': random.choice(['M', 'F']),
        'Department': random.choice(departments),
        'Salary': random.randint(30000, 80000),
        'Joining Date': fake.date_between(start_date='-10y', end_date='today'),
        'Sales': random.randint(10000, 40000),
        'Region': random.choice(regions),
        'Project Hours': random.randint(20, 60)
    })
df = pd.DataFrame(data)
print(df)
