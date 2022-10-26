import math
import random

სახელი = ["ლუკა", "ანდრო", "გიო", "სანდრო"]
რაიონი = ["გლდანი", "ვაკე"]
კუთხე = ["იმერეთი", "კახეთი", "სამეგრელო"]
გვარი = ["ივანიაძე", "წიქვაძე", "ბაღათურია"]
ქუჩა = ["კავსაძე", "ქერჩი", "ჭავჭავაძე"]


for num in range(10):
    first = random.choice(სახელი)
    last = random.choice(გვარი)

    phone = f'{random.randint(500, 600)}-{random.randint(10,99)}-{random.randint(10,99)}-{random.randint(10,99)}'

    street_num = random.randint(100, 999)
    street = random.choice(ქუჩა)
    city = random.choice(რაიონი)
    state = random.choice(კუთხე)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} ქუჩა., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@btu.edu.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')
