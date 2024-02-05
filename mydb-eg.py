# set up virtual env
# virt\Scripts\activate.bat
# cd into DCRM/DCIM and open VS code

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'UoT@2024'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE databaseName")

print("Successful!")
