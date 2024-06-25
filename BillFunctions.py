import os
import mysql.connector as connector
import pandas


def searchbill():
    os.system('cls')
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()

    searchbillno = input('Enter Bill No To Be Searched: ')
    q = "select * from bill where billno = {}".format(searchbillno)
    cursor.execute(q)
    data = cursor.fetchall()

    if cursor.rowcount > 0:
        os.system('cls')
        print('*********************************************************')
        print('                       YOUR BILL')
        print('*********************************************************')
        print()

        df = pandas.DataFrame(data, columns=['Billno', 'Billdate', 'Name', 'Itemname', 'Qty', 'Rate', 'Amount'])
        print()

        print('Bill No: ', df.at[0, 'Billno'])
        print('Bill Date: ', df.at[0, 'Billdate'])
        print('Cusomer Name: ', df.at[0, 'Name'])
        print()

        print('Itemname', '\t\t', 'Qty', '\t\t', 'Rate', '\t\t', 'Amount')
        for ri, rd in df.iterrows():
            print(rd[3], '\t\t', rd[4], '\t\t', rd[5], '\t\t', rd[6])

        q = "select sum(amt) from bill where billno = {}".format(searchbillno)
        cursor.execute(q)
        data = cursor.fetchall()
        gt = data[0][0]
        print()
        print('GRAND TOTAL: ', gt)
        print()
        input('Press Enter To Continue...................')
    else:
        print()
        print('This Bill No Does Not Exist !')
        print()
        input('Press Enter To Continue.........')



def generatebillno():
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    q = "select max(billno)+1 from bill"
    cursor.execute(q)
    data = cursor.fetchall()
    if data[0][0] == None:
        return 1
    else:
        return data[0][0]

def getiteminfo():
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    searchitem = input('Enter Item Name Or Some Part Of It:')
    q = "select * from item where itemname like '%{}%' ".format(searchitem)
    cursor.execute(q)
    data = cursor.fetchall()
    if cursor.rowcount > 0:
        print()
        df = pandas.DataFrame(data, columns=['Itemno', 'Item Name', 'Rate'])
        print(df)
        print()
        itemno = input('Enter Item No Of The Item You Want To Add To The Bill: ')
        q = "select itemname, rate from item where itemno = {} ".format(itemno)
        cursor.execute(q)
        data = cursor.fetchall()
        return ([data[0][0], data[0][1]])
    else:
        return False


def showcurrentbill(billno):
    os.system('cls')
    print('*********************************************************')
    print('                       YOUR BILL')
    print('*********************************************************')
    print()

    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    q = "select * from bill where billno = {}".format(billno)
    cursor.execute(q)
    data = cursor.fetchall()
    df = pandas.DataFrame(data, columns=['Billno', 'Billdate', 'Name', 'Itemname', 'Qty', 'Rate', 'Amount'])
    print()

    print('Bill No: ', df.at[0, 'Billno'])
    print('Bill Date: ', df.at[0, 'Billdate'])
    print('Cusomer Name: ', df.at[0, 'Name'])
    print()

    print('Itemname', '\t\t', 'Qty', '\t\t', 'Rate', '\t\t', 'Amount')
    for ri, rd in df.iterrows():
        print(rd[3], '\t\t', rd[4], '\t\t', rd[5], '\t\t', rd[6])

    q = "select sum(amt) from bill where billno = {}".format(billno)
    cursor.execute(q)
    data = cursor.fetchall()
    gt = data[0][0]
    print()
    print('GRAND TOTAL: ', gt)
    print()
    input('Press Enter To Continue...................')


def createnewbill():
    os.system('cls')
    print('*********************************************************')
    print('NEW BILL CREATION')
    print('*********************************************************')
    print()
    billno = generatebillno()
    print('Bill No: ', billno)
    con = connector.connect(host='localhost', username='root', password='root', database='restaurantxiig')
    cursor = con.cursor()
    q = "select curdate()"
    cursor.execute(q)
    data = cursor.fetchall()
    print('Bill Date: ', data[0][0])
    name = input('Enter Customer Name: ')

    print()
    while True:
        iteminfo = getiteminfo()
        if iteminfo != False:
            print('Item Name: ', iteminfo[0])
            print('Item Rate: ', iteminfo[1])
            qty = input('Enter Qty: ')
            amt = int(qty) * int(iteminfo[1])
            print('Amount: ', amt)
            q = "insert into bill values({}, '{}', '{}', '{}', {}, {}, {})".format(billno, data[0][0], name, iteminfo[0], qty, iteminfo[1], amt)
            cursor.execute(q)
            con.commit()
            print()
            print('Item Added To The Bill !')
            print()
            ask = input('Do You Want To Add More Items(y/n):')
            if ask == 'n':
                showcurrentbill(billno)
                break
        else:
            print()
            print('No Such Item Found !')
            print()
            ask = input('Continue Searching(y/n): ')
            if ask == 'n':
                break
            print()
