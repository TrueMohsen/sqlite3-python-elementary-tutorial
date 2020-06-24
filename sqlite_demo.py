import sqlite3
from Employee import Employee

conn = sqlite3.connect('employee.db')
def insert_emp(emp):
    with conn:
        cursor.execute("INSERT INTO employees VALUES (?,?,?)",(emp.first,emp.last,emp.pay))
        # cursor.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})
        # cursor.execute("INSERT INTO employees VALUES ('mohsen','kashani',100000)")


def get_emps_by_name(lastname):
    # cursor.execute("SELECT * FROM employees WHERE last='Doe'")
    # cursor.execute("SELECT * FROM employees WHERE last=?",('Doe',))
    cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return cursor.fetchall()

def update_pay(emp,pay):
    pass

def remove_emp(emp):
    pass


cursor = conn.cursor()
# cursor.execute(""" CREATE TABLE employees (
#             first text ,
#             last text ,
#             pay integer) """)

emp_1 = Employee('isaac','Doe',90000)
emp_2 = Employee('jack','Doe',90000)
insert_emp(emp_1)
insert_emp(emp_2)
emps = get_emps_by_name('Doe')
print(emps)
conn.commit()
conn.close()




