import pymysql
db = pymysql.connect("localhost","python_mysql","$nakesSuckEvery1!","kronos_sec")
cursor = db.cursor()
cursor.execute("SELECT distinct ip from edgar")
data = cursor.fetchone()
print(data)
db.close()

