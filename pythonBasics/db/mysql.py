 # pip3 install PyMySQL
 # pip3 install redis
import pymysql
# 获取db连接
def getDBCon():
	return pymysql.connect("127.0.0.1", "root", "admin", "student", charset='utf8' )

# def getRedisCon():
# 	return redis.Redis(host="127.0.0.1", port=6379, password="admin", db=1)
	

def getStudent(db):
	cursor = db.cursor()
	try:
	
		sql = "select * from student"
			# print(sql)
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			fname = row[0]
			lname = row[1]
			age = row[2]
			sex = row[3]、
			income = row[4]
			print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income )
	except Exception as e:
			print (e)


def closeDB(db):
	db.close()
	# redisCon.connection_pool.disconnect()
	print("数据库已关闭")


db=getDBCon()
getStudent(db)
closeDB(db)