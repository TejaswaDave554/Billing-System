import mysql.connector as connector
import os
import pandas


def modifyitem():
    os.system('cls')
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    itemno = input('Enter Item No To Be Modified: ')
    q = "select * from item where itemno = {}".format(itemno)
    cursor.execute(q)
    data = cursor.fetchall()

    if cursor.rowcount > 0:
        df = pandas.DataFrame(data, columns=['ItemNo', 'ItemName', 'ItemRate'])
        print()
        print(df)
        print()
        ask = input('Are you sure you want to modify this record (y/n): ')
        if ask == 'y':
            newitemname = input('Enter new item name: ')
            newrate = input('Enter new rate: ')
            q = "update item set itemname = '{}', rate = {} where itemno = {}".format(newitemname,newrate,itemno)
            cursor.execute(q)
            con.commit()
            print()
            print('Record Updated !')
            print()
            input('Press Enter To Continue........')
            con.close()
        else:
            print('No changes saved !')
    else:
        print('This Item Does Not Exist !')





def deleteitem():
    os.system('cls')
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    itemno = input('Enter Item No To Be Deleted: ')
    q = "select * from item where itemno = {}".format(itemno)
    cursor.execute(q)
    data = cursor.fetchall()

    if cursor.rowcount > 0:
        df = pandas.DataFrame(data,columns=['ItemNo','ItemName','ItemRate'])
        print()
        print(df)
        print()
        ask = input('Are you sure you want to delete this record (y/n): ')
        if ask == 'y':
            q = "delete from item where itemno = {}".format(itemno)
            cursor.execute(q)
            con.commit()
            print()
            print('Record Deleted !')
            print()
            input('Press Enter To Continue........')
            con.close()
        else:
            print('No changes saved !')
    else:
        print('This Item Does Not Exist !')



def showallitems():
    os.system('cls')
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    q = 'select * from item'
    cursor.execute(q)
    data = cursor.fetchall()
    df = pandas.DataFrame(data,columns=['ItemNo','ItemName','ItemRate'])
    print()
    print(df)
    print()
    input('Press Enter To Continue........')
    con.close()


def getlatestitemno():
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    q = 'select max(itemno) + 1 from item'
    cursor.execute(q)
    data = cursor.fetchall()
    return(data[0][0])

def addnewitem():
    os.system('cls')
    print('************************************************')
    print('CREATE NEW ITEM')
    print('************************************************')
    print()
    itemno = getlatestitemno()
    print('New Item No: ',itemno)
    itemname = input('Enter item name: ')
    itemrate = input('Enter item rate: ')
    con = connector.connect(host='localhost',username='root',password='root',database='restaurantxiig')
    cursor = con.cursor()
    q = "insert into item values({}, '{}', {})".format(itemno,itemname,itemrate)
    cursor.execute(q)
    con.commit()
    print()
    print('New Item Created !')
    print()
    input('Press Enter To Continue........')
    con.close()





