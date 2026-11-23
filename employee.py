import mysql.connector

# Database Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_db"
)

cur_obj = mydb.cursor()

print("MYSQL DATABASE CONNECTED SUCCESSFULLY")


# CREATE EMPLOYEE
def create_employee():
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")
    city = input("Enter City: ")

    query = """
    INSERT INTO employee
    (emp_id, emp_name, salary, department, city)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (emp_id, emp_name, salary, department, city)

    cur_obj.execute(query, values)
    mydb.commit()

    print("Employee Added Successfully!")


# READ EMPLOYEE
def read_employee():
    cur_obj.execute("SELECT * FROM employee")

    records = cur_obj.fetchall()

    for row in records:
        print(row)


# UPDATE EMPLOYEE
def update_employee():
    emp_id = int(input("Enter Employee ID: "))

    salary = float(input("Enter New Salary: "))
    city = input("Enter New City: ")

    query = """
    UPDATE employee
    SET salary=%s, city=%s
    WHERE emp_id=%s
    """

    values = (salary, city, emp_id)

    cur_obj.execute(query, values)
    mydb.commit()

    print("Employee Updated Successfully!")


# DELETE EMPLOYEE
def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    query = "DELETE FROM employee WHERE emp_id=%s"

    values = (emp_id,)

    cur_obj.execute(query, values)
    mydb.commit()

    print("Employee Deleted Successfully!")


# MENU
while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Create Employee")
    print("2. Read Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        create_employee()

    elif choice == 2:
        read_employee()

    elif choice == 3:
        update_employee()

    elif choice == 4:
        delete_employee()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

cur_obj.close()
mydb.close()