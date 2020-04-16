import random 
import os 
import sys 
clear = lambda: os.system("cls")
tanks = 0
soldiers = 1000
money = 100000
resources = 1
factorys = 1
dmt = 30
day = 0
try:
    save = open("wargamesave.txt","r")
    lines = save.readlines()
    tanks = int(lines[0])
    soldiers = int(lines[1])
    money = int(lines[2])
    resources = int(lines[3])
    factorys = int(lines[4])
    dmt = int(lines[5])
    day = int(lines[6])
except:
    print()

action = "%"
while action != "0":
    resources = resources + factorys*5
    clear()
    attck = random.randint(1, 100)
    if attck > 90:
        if day > 0:
            print("You are being attcked!!")
            
            ypower = tanks * 10 
            ypower = ypower + soldiers * .02
            ypower = ypower + resources/4
            epower = random.randint(0, 100)
            if ypower > 100:
                epower = epower * 2
            if ypower > epower:
                print("You won the battle, but it came at a cost.")
                if tanks > 0:
                    tanks = tanks - random.randint(1,10)
                    if tanks < 0:
                        tanks = 0
                soldiers = soldiers - random.randint(1,30)
                if soldiers < 0:
                        soldiers = 0
            else:
                print("You have lost but you are not out yet")
                factorys = factorys/2
                if money > 0: 
                    money = money/2
                else:
                    money = money + money/2
                soldiers = soldiers - soldiers * .5
                tanks = tanks - 4
    print("Resources:", resources)
    print("soldiers:", soldiers)
    print("Factorys:", factorys)
    if tanks > 0:
        print("Tanks", tanks)
    print("days till money return", dmt)
    print("Money:", money)
    print("Day: ", day)
    print("1:Buy tanks")
    print("2:Buy soldiers")
    print("3:Buy factorys")
    print("4:Do nothing")
    print("0:Quit")
    action = input("Action: ")
    try: 
        while action == "1":
            clear()
            print("Money:", money)
            print("Price for 1 50,000")


            print("0 to cancel")
            amount = int(input("Amount: "))
            price = amount * 50000
            money1 = int(money) - price

        
            if money1 < -10000:
                print("Insuficent funds")
            else:
                action = "a"
                tanks = tanks + amount
                money = int(money) - price
        else:
            while action == "2":
                clear()
                print("Money:", money)
                print("Price for 1 250")
                print("0 to cancel")
                amount = int(input("Amount: "))

                price = amount * 250
                money1 = int(money) - price

                if money1 < -10000:
                    print("Insuficent funds")
                else:
                    soldiers = soldiers + amount
                    action = "a"
                    money = int(money) - price
            while action == "3":
                clear()
                print("Money:", money)
                print("Price for 1 1,000")
                print("0 to cancel")
                amount = int(input("Amount: "))
                price = amount * 1000
                money1 = int(money) - price

                if money1 < -10000:
                    print("Insuficent funds")
                else:
                    factorys = factorys + amount
                    action = "a"
                    money = int(money) - price
            else:
                dmt = dmt - 1 
                if dmt < 1:
                    money = money + 25000
                    dmt = 30
                    money = money + resources*5
                    resources = 0
                day = day + 1
                if soldiers <= 0:
                    break
                if tanks < 0:
                    tanks = 0

    except:
        print()

else:
    save = open("wargamesave.txt", "w")
    save.write(f"{tanks}\n")
    save.write(f"{soldiers}\n")
    save.write(f"{money}\n")
    save.write(f"{resources}\n")
    save.write(f"{factorys}\n")
    save.write(f"{dmt}\n")
    save.write(f"{day}\n")
    save.close
        

