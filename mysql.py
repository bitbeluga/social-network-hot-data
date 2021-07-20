import mysql.connector

mydb = mysql.connector.connect(
    host="10.30.10.123",
    user="applet",
    passwd="blue_tv_applet",
    database="test"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
print(mycursor)
for x in mycursor:
    print(x)
