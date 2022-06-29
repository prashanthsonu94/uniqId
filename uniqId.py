# Generating UniqueId's 


# import string
# import random
# from random import randint

# def random_digit_generate(length):
#     key=""
#     for i in range(length):
#         key = key+random.choice(string.digits)
#     return key
# result=random_digit_generate(16)
# print("TXN"+result)
# print(randint(1,9))


# otp_number = str(random.randint(111111, 999999))
# print(otp_number)
# print(type(otp_number))


toNumber=input("enter num:")
toNumber = toNumber.replace(" ",'').replace("-","").replace("(","").replace(")","")
print(toNumber)
print(type(toNumber))


