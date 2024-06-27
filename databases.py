import sqlite3
import pandas as pd
import pyodbc


# # connecting to new database
conn = sqlite3.connect('firstSql.db')

# # cursor is the tool used to communicate with the database
c = conn.cursor()

# # comment out after running
# # create a table and the columns within the table, and the data type
# c.execute("""CREATE TABLE VetClinic(
#                 FirstName text,
#                 LastName text,
#                 PetName text,
#                 AnimalType text,
#                 Procedure text,
#                 Date text,
#                 Cost real
#          )""")

# # datatypes in sqlite3:
# # 5 diff variables: text, regular numbers, real numbers(decimal), blob(binary data, image)
# # Integers:
    # INT
    # INTEGER
    # TINYINT
    # SMALLINT
    # MEDIUMINT
    # BIGINT
    # UNSIGNED BIG INT
    # INT2
    # INT8
# # Text:
    # CHARACTER(20)
    # VARCHAR(255)
    # VARYING CHARACTER(255)
    # NCHAR(55)
    # NATIVE CHARACTER(70)
    # NVARCHAR(100)
    # TEXT
    # CLOB
# # Blob:
    # BLOB
# # Real:
    # REAL
    # DOUBLE
    # DOUBLE PRECISION
    # FLOAT
# # Numeric
    # NUMERIC
    # DECIMAL(10,5)
    # BOOLEAN
    # DATE
    # DATETIME

# # comment out after running
# c.execute("INSERT INTO VetClinic VALUES ('Sean', 'Beans', 'Baby Luv', 'Cat', 'cuteness overload', 'May 1st', '16.00' )")
# c.execute("INSERT INTO VetClinic VALUES ('Akxa', 'Beans', 'Jovi', 'Cat', 'cuteness overload', 'Dec 10th', '16.00' )")

# # another example to insert values
# class VetClinic:
#     def __init__(self, first, last):
#         self.first_name
#         self.last_name
#
#
# def insert_into_vetclinic(clinic):
#     c.execute("INSERT INTO VetClinic VALUES (?,?,?,?,?,?,?)", clinic.first_name, clinic.last_name)
#
# patient = VetClinic('Hupe', 'Alex')
# insert_into_vetclinic(patient)

# write this query to take a look at our data that we just inserted
c.execute("SELECT * FROM VetClinic")
output = c.fetchall()
print(output)

conn.commit()
conn.close()


# to connect to SQL server:
# install packages: pandas, pandas-gbq, pyodbc(need it to handle the ODBC driver)
# import pandas and pyodbc at the top of page

connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=server_address;DATABASE=database_name;UID=user_name;PWD=user_password'
connection = pyodbc.connect(connection_string)

dataframe = pd.read_sql_query('SELECT * FROM [dbo].[VetClinic]', connection)

print(dataframe)
