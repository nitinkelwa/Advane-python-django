# from operator import indexOf
#
# import pymysql
#
# connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
# cursor = connection.cursor()
# sql = "INSERT INTO user VALUES (6, 'buff', 'singh', 70000)"
# cursor.execute(sql)
# connection.commit()
# connection.close()
# print("Data Inserted Successfully")

#######################################################################################################

import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='indore')
cursor = connection.cursor()
sql = "insert into marksheet values (16,200,'mahi',50,100,80)"
cursor.execute(sql)
connection.commit()
connection.close()
print("data insert successfully")
