import os
import ItemsFunctions
import BillFunctions
import ChartFunctions

while True:
    os.system('cls')
    print('*********************************************************')
    print('RESTAURANT BILLING SYSTEM')
    print('*********************************************************')
    print()
    print('1. Add Item')
    print('2. Display All Items')
    print('3. Delete Item')
    print('4. Modify Item')
    print('5. Create Bill')
    print('6. Search Bill')
    print('7. Show Charts')
    print('0. Exit')
    print()
    choice = int(input('Enter your choice: '))

    if choice == 0:
        break
    elif choice == 1:
        ItemsFunctions.addnewitem()
    elif choice == 2:
        ItemsFunctions.showallitems()
    elif choice == 3:
        ItemsFunctions.deleteitem()
    elif choice == 4:
        ItemsFunctions.modifyitem()
    elif choice == 5:
        BillFunctions.createnewbill()
    elif choice == 6:
        BillFunctions.searchbill()
    elif choice == 7:
        ChartFunctions.showchartmenu()









