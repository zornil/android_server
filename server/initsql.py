import pymysql
from model import User


url = "localhost"
user = "root"
password = "root"
database = "api"
db = pymysql.connect(url, user, password, database)
cursor = db.cursor()


def isUserExisted(email=None):
    sql = "SELECT * FROM users WHERE username = '%s'" % email
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            return False
        elif results[2] == email:
            return True
    except:
        print ("Error: unable to fetch data")
        return False


def getUserDataByName(name=None):
    sql = "SELECT * FROM users WHERE name = '%s'" % name
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            return "userIsNotExisted"
        for row in results:
            uid = row[0]
            name = row[1]
            email = row[2]
            encrypted_password = row[3]
            out = User(id, name, email, encrypted_password)
        return out
    except:
        print ("Error: unable to fetch data")
        return "failure"


def insertData(name=None, email=None, passwd=None):
    res = isUserExisted(email)
    if res is True:
        return "userIsExisted"

    sql = "INSERT INTO users(name, email, encrypted_password) VALUES ('%s', '%s', '%s')" % (name, email, passwd)
    try:
        cursor.execute(sql)
        db.commit()
        return "success"
    except:
        db.rollback()
        return "failure"


def quitMysql(self):
    db.close()
