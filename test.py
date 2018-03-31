#sql test
import sqlite3
#connecting to sqlite3 database
connection = sqlite3.connect('data.db')
#executing queries for database
cursor=connection.cursor()
#sql command(Create TABLE tableName (columns...schema))
create_table="CREATE TABLE users(id int, user text, passowrd text)"
#implement
cursor.execute(create_table)

#store data in database
user=(1,'Andrew','complexPassword')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

#many users
users=[
    (2, 'joe','asdf'),
    (3, 'Allison','Gorgeous')
]
cursor.executemany(insert_query, users)


#retrieve data
select_query="SELECT * FROM users"
for row in cursor.execute(select_query):
    #print data from database
    print(row)
#pushes to db file
connection.commit()
#good practice
connection.close()
