from datetime import datetime
import time
import matplotlib.pyplot as plt

import numpy as np
from mysql.connector import MySQLConnection, Error

import crawl_db
from connectDB import read_db_config
from crawl_db import getDB

"""
def queryDB():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("select * from db_covid")

        rows = cursor.fetchone()
        print(rows)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
"""

def insert_db(banghi):
    global cursor, conn
    query = "insert into db_covid(total_case,today_case,number_item_khoi,number_item_tuvong,number_item_dangdieutri,time) values(%s,%s,%s,%s,%s,%s)"

    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        cursor = conn.cursor()
        cursor.executemany(query,banghi)

        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def main_insert():

    banghi = getDB()
    insert_db(banghi)

def queryDB():
    global cursor, conn
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("select total_case from db_covid")

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def query_covid(query):
    global cursor, conn, db
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()
        db = []
        for row in rows:
            db.append(row)
    except Error as e:
        print('Error: ',e)
    finally:
        cursor.close()
        conn.close()
    return db

def plt_covid():
    dt = query_covid("select time from db_covid")
    x = np.array(dt)

    #plt_total_case
    dulieu_total_case = query_covid("select total_case from db_covid")
    y = np.array(dulieu_total_case)
    plt.subplot(2, 2, 1)
    plt.title('Total case')
    plt.xlabel('Time')
    plt.ylabel('People')
    plt.grid(linestyle='dotted')
    plt.plot(x,y)


    #plt_today_case
    dulieu_today_case = query_covid("select today_case from db_covid")
    y = np.array(dulieu_today_case)

    plt.subplot(2,2,2)
    plt.title('Today case')
    plt.xlabel('Time')
    plt.ylabel('People')
    plt.grid(linestyle='dotted')
    plt.plot(x,y)

    #plt_number_item_khoi
    dulieu_nb_item_khoi = query_covid("select number_item_khoi from db_covid")
    y = np.array(dulieu_nb_item_khoi)

    plt.subplot(2,2,3)
    plt.title('Number Item Khoi')
    plt.xlabel('Time')
    plt.ylabel('People')
    plt.grid(linestyle='dotted')
    plt.plot(x,y)

    #plt_number_item_tuvong
    dulieu_nb_item_tuvong = query_covid("select number_item_tuvong from db_covid")
    y = np.array(dulieu_nb_item_tuvong)

    plt.subplot(2,2,4)
    plt.title('Number Item Tu Vong')
    plt.xlabel('Time')
    plt.ylabel('People')
    plt.grid(linestyle='dotted')
    plt.plot(x,y)

    plt.suptitle("Covid - 19")
    plt.show()

if __name__=='__main__':
    crawl_db.driver.close()
    dt = datetime.now()
    if dt.hour == 7 or dt.hour == 19:
        print("Cập nhật thông tin thành công")
        #main_insert()
    plt_covid()