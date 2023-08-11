import mysql.connector

def create_connection():
    conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306,auth_plugin='mysql_native_password')
    return conn