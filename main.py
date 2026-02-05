import sqlite3 
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# Select all columns from the employees table
employee_data = pd.read_sql("""SELECT * FROM employees;""", conn)
print(employee_data)

# Another way to select all columns from the employees table
print(pd.read_sql("""
SELECT *
  FROM employees;
""", conn))

# Select lastName and firstName columns from the employees table
employees_last_and_first = pd.read_sql("""
SELECT lastName, firstName
  FROM employees;
""", conn).head()

print(employees_last_and_first)

# Select firstName and lastName columns from the employees table
employees_first_and_last = pd.read_sql("""
SELECT firstName, lastName
  FROM employees;
""", conn).head()

print(employees_first_and_last)

# Select firstName column from the employees table with the alias name
employees_first_names = pd.read_sql("""
SELECT firstName AS name
  FROM employees;
""", conn).head()

print(employees_first_names)

# Select firstName, latname, and jobTitle columns from the employees table
# and create a new column 'role' based on jobTitle
employees_by_role = pd.read_sql("""
SELECT firstName, lastName, jobTitle,
       CASE
       WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
       ELSE "Not Sales Rep"
       END AS role
  FROM employees;
""", conn).head(10)

print(employees_by_role)

# Select firstName, lastName, and officeCode columns from the employees table
# and create a new column 'office' based on officeCode
employees_with_location = pd.read_sql("""
SELECT firstName, lastName, officeCode,
       CASE
       WHEN officeCode = "1" THEN "San Francisco, CA"
       WHEN officeCode = "2" THEN "Boston, MA"
       WHEN officeCode = "3" THEN "New York, NY"
       WHEN officeCode = "4" THEN "Paris, France"
       WHEN officeCode = "5" THEN "Tokyo, Japan"
       END AS office
  FROM employees;
""", conn).head(10)

print(employees_with_location)

# Alternative syntax for the same query using CASE ... WHEN ... THEN ... END
employees_with_location = pd.read_sql("""
SELECT firstName, lastName, officeCode,
       CASE officeCode
       WHEN "1" THEN "San Francisco, CA"
       WHEN "2" THEN "Boston, MA"
       WHEN "3" THEN "New York, NY"
       WHEN "4" THEN "Paris, France"
       WHEN "5" THEN "Tokyo, Japan"
       END AS office
  FROM employees;
""", conn).head(10)

print(employees_with_location)

# Using length string function to get the length of first names
employee_name_lengths = pd.read_sql("""
SELECT length(firstName) AS name_length
  FROM employees;
""", conn).head()

print(employee_name_lengths)

# Using upper string function to convert first names to uppercase
upper_employees = pd.read_sql("""
SELECT upper(firstName) AS name_in_all_caps
  FROM employees;
""", conn).head()

print(upper_employees)

# Using substr string function to get the first initial of first names
employees_initials = pd.read_sql("""
SELECT substr(firstName, 1, 1) AS first_initial
  FROM employees;
""", conn).head()

print(employees_initials)

# Using substr string function to get the first initial of first names
# and use a concatenation operator (||) to add a period after the initial
employees_initials = pd.read_sql("""
SELECT substr(firstName, 1, 1) || "." AS first_initial
  FROM employees;
""", conn).head()

print(employees_initials)

# Concatenating firstName and lastName without space
employees_full_names = pd.read_sql("""
SELECT firstName || lastName AS full_name
  FROM employees;
""", conn).head()

print(employees_full_names)

# Concatenating firstName and lastName with space
employees_full_names = pd.read_sql("""
SELECT firstName || " " || lastName AS full_name
  FROM employees;
""", conn).head()

print(employees_full_names)

# Select all columns from the orderDetails table
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print(order_details)

# Using round numeric function to round priceEach values
rounded_prices = pd.read_sql("""
SELECT round(priceEach) AS rounded_price
  FROM orderDetails;
""", conn)

print(rounded_prices)

# Using round numeric function to round priceEach values and cast to integer
rounded_prices = pd.read_sql("""
SELECT CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails;
""", conn)

print(rounded_prices)

# Calculating total price by multiplying priceEach and quantityOrdered
totals = pd.read_sql("""
SELECT priceEach * quantityOrdered AS total_price
  FROM orderDetails;
""", conn)

print(totals)

# Select all columns from the orders table
orders = pd.read_sql("""SELECT * FROM orders;""", conn)
print(orders)

# Incorrect way to calculate days remaining (will not work as expected)
days_remaining = pd.read_sql("""
SELECT requiredDate - orderDate
  FROM orders;
""", conn)

print(days_remaining)

# Correct way to calculate days remaining using julianday function
days_remaining = pd.read_sql("""
SELECT julianday(requiredDate) - julianday(orderDate) AS days_from_order_to_required
  FROM orders;
""", conn)

print(days_remaining)

# Adding 7 days to orderDate using date function
order_dates = pd.read_sql("""
SELECT orderDate, date(orderDate, "+7 days") AS one_week_later
  FROM orders;
""", conn)

print(order_dates)

# Extracting month, year, and day from orderDate using strftime function
order_dates = pd.read_sql("""
SELECT orderDate,
       strftime("%m", orderDate) AS month,
       strftime("%Y", orderDate) AS year,
       strftime("%d", orderDate) AS day
  FROM orders;
""", conn)

print(order_dates)

conn.close()