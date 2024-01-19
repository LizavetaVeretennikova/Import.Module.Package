from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import pandas as pd

now = datetime.now()
df = pd.DataFrame({
    'employees': ['Иван', 'Александр', 'Екатерина'],
    'salary': ['50000', '30000', '40000']
})
if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print("Текущая дата и время: {}.{}.{} {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))
    print(df)