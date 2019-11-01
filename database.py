import pymysql


db = pymysql.connect(host='localhost', user='root', password='', db='spider')
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print('database version:', data)
# cursor.execute('create database spider default character set utf8')
# cursor.execute('drop table if exists test')
# sql = 'create table if not exists webs(id varchar(255)not null, name varchar(255)not null, host varchar(255)not null,' \
#       'primary key(id))'
sql = 'insert into webs(id,name,host)values(%s,%s,%s)'
try:
    cursor.execute(sql, ('1002', 'weibo', 'www.weibo.com'))
except:
    db.rollback()
db.commit()
db.close()