import math
import random
naameq=['what is your name','what is your name?','what\'s your name','your name','Who are you']
greetings=['hi','hello','welcome','hey nice to meet you']
greets=['hi','hello','hey']

shoplist={'soap':20,'shampoo':30,'mascara':40,'cream':180,'bindi':50,'eyeliner':100}
print("products for shopping")
sell=0
for i in shoplist:
    print(i)
    
    item=shoplist.keys()
    price=shoplist[i]

data=input("enter item to buy\n")
price=shoplist[data]
bid=int(input("enter what price you bid\n"))
print(data,":","rs",bid)

print(price)
discount=float (0.2*price)
sell=float(price-discount)

print(bid,sell)    
if (bid>sell):
    print("you can buy the product at",bid,"rs")
else :
    print("sorry cant sell")
    


    
