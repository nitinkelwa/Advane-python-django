# import pymysql
#
# connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
# cursor = connection.cursor()
# sql = "DELETE FROM USER WHERE ID =6"
# cursor.execute(sql)
# connection.commit()
# connection.close()
# print("Data Delete Successfully")

########################################################################################################################


import pymysql

connection= pymysql.connect(host='localhost',port=3306,user='root',password='root',db='indore')
cursor=connection.cursor()
sql="delete from marksheet where id =16"
cursor.execute(sql)
connection.commit()
connection.close()
print("data deleted successfully")

