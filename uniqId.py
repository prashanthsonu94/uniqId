# Generating UniqueId's 

import textwrap
import string
import random
from random import randint

def random_digit_generate(length):
    key=""
    for i in range(length):
        # key = key+random.choice(string.digits)                     #Generating random 16 digit number
        key = key+random.choice(string.ascii_lowercase)                #Generating random 12 digit alphabet seperating with specified "string"
    return key
# result=random_digit_generate(16)
result=random_digit_generate(12)
g=textwrap.wrap(result,3)
r1="-".join(g)
print(r1)
# print("TXN"+result)
# print(randint(1,9))


# otp_number = str(random.randint(111111, 999999))
# print(otp_number)
# print(type(otp_number))


toNumber=input("enter num:")
toNumber = toNumber.replace(" ",'').replace("-","").replace("(","").replace(")","")
print(toNumber)
print(type(toNumber))




