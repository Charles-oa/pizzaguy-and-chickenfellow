#pizza ordering app
menuMain = {1:'1.Select pizza size', 2:'2.Select toppings', 3:'3.Order a drink', 0:'0.Exit'}
menuSize = {1:'1.Large pizza', 2:'2.Medium pizza', 3:'3.Small pizza',9:'9.Back to menu'}
menuToppings = {1:'1.Pepperoni', 2:'2.Sausage', 3:'3.Mushrooms', 4:'4.Bacon', 5:'5.Onions', 6:'6.Extra cheese', 7:'7.Chicken', 9:'9.Back to menu'}
menuDrinks = {1:'1.Coca-cola', 2:'2.Fanta', 3:'3.Sprite', 4:'4.Dr.Pepper', 5:'5.Alvaro', 6:'6.Malt', 7:'7.Shandy', 9:'9.Back to menu'}

def printMenu(menuTitle, menu): #we should input the menu we want to print
    print('\n', menuTitle)
    print('-------------')
    for value in menu.values():
        print(value, '\n')

printMenu('Welcome to pizzaguy and chickenfellow', menuMain)
mainChoice = int(input('option: '))

while mainChoice != 0: #this means if the person enters 0 stop the app
    if mainChoice == 1: #select pizza size
        printMenu('please select your preferred pizza size', menuSize)
        purchaseSize = int(input('Enter product: ')) #recieve what size user wants

        while purchaseSize != 9:
            print('size: ',menuSize[purchaseSize])
            input('\nPress any key to continue---')

            printMenu(menuMain)

    elif mainChoice == 2: #select toppings
        printMenu('please choose your desired toppings', menuToppings)
    elif mainChoice == 3: #order a drink
        printMenu('please choose a drink',menuDrinks)
    else:
        print('Invalid input')
    
    input('\nPress any key to continue---')

    printMenu('welcome to pizzaguy and chickenfellow',menuMain)
    mainChoice = int(input('option: '))

print('\nWe are sorry to see you go')
    