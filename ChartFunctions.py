import mysql.connector as connector
import os
import pandas
import matplotlib.pyplot as plt


def showbillamount():
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    q = 'select billno, sum(amt) from bill group by billno'
    cursor.execute(q)
    data = cursor.fetchall()
    df = pandas.DataFrame(data, columns=['billno', 'sum'])

    plt.plot(df['billno'], df['sum'] , color = 'r')
    plt.title('Bill - Amount Analysis')
    plt.xlabel('BILLNO')
    plt.ylabel('AMOUNT')
    plt.show()
    con.close()




def showitemandpricechart():
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    q = 'select * from item'
    cursor.execute(q)
    data = cursor.fetchall()
    df = pandas.DataFrame(data, columns=['itemno', 'itemname', 'rate'])

    plt.bar(df['itemname'], df['rate'] , color = 'r')
    plt.title('Item - Rate Analysis')
    plt.xlabel('ITEMS')
    plt.ylabel('RATE')
    plt.legend(['rate'],loc = 'upper left')
    plt.yticks(range(0,160,10))
    plt.xticks(rotation = 45)
    plt.show()
    con.close()

def showchartmenu():
    while True:
        os.system('cls')
        print('*********************************************************')
        print('                       DATA ANALYSIS')
        print('*********************************************************')
        print()
        print('1. SHOW ITEM AND PRICE CHART')
        print('2. SHOW BILL - AMOUNT ANALYSIS')
        print()
        print('0. Exit')
        print()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            break
        if choice == 1:
            showitemandpricechart()
        elif choice == 2:
            showbillamount()

