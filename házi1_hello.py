import random as rnd
import os

# return a random ip: x.x.x.x  x:[0:255]
def ip():
    res = str(rnd.randint(0,255))
    for i in range(3):
        res = res+ "." +str(rnd.randint(0,255))
    return res

# return a random mac adress 
def mac():
    abc = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    res = str(rnd.choice(abc)) + str(rnd.choice(abc))
    for i in range(5):
        res = res + ":" + str(rnd.choice(abc)) + str(rnd.choice(abc))
    return res

def nev(list):
    for i in range(len(list)):
        name = input("Name of the computer: ")
        list[i] = {
            "nev" : name,
            "ip" : ip(),
            "mac" : mac()
        }
    return list

#pass a number
def nev_ip_mac(list):
    adresses = nev(list)
    for i in range(len(adresses)):
        print(str(i+1)+". Számitógép adatai:\nNév: "+adresses[i]["nev"]+"\nIP: "+adresses[i]["ip"]+"\nMac: "+adresses[i]["mac"])
        print("-------------------------")
    return adresses