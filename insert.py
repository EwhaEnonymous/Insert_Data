import pandas as pd
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='{비밀번호}',
    db='ttockclinic_db',
    charset='utf8'
)
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "insert into clinic (address, holiday_opening_hours, name, phone, saturday_opening_hours, si_do, si_gun_gu, waitings, weekday_opening_hours) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


data = pd.read_excel("./clinic.xls")
data = data.where((pd.notnull(data)), None)
for idx in range(len(data)):
    curs.execute(sql, tuple(data.values[idx]))
conn.commit()

curs.close()
conn.close()


