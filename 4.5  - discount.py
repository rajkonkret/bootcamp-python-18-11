from datetime import date, timedelta, datetime

today = date.today()
print(type(today))  # <class 'datetime.date'>
print(today)  # 2023-12-03

time = datetime.now()
print(time)  # 2023-12-03 09:28:14.413980
print(type(time))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2023-12-04

print(time.hour)
print(today.day)

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 03/12/2023

formated_time = datetime.now().strftime('%H:%M')
print(formated_time)  # 09:34
print(formated_time.removeprefix("0"))  # 9:34

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 80.0},
    {'sku': 3, 'exp_date': today, 'price': 50},
]

print(products)
for product in products:
    # print(product)
    if product['exp_date'] != today:
        print("Kontynuujemy")
        continue  # konczy biezace wykonanie petli, bierze kolejny elemnt i wykonuje całą petle
    product['price'] *= 0.5  # price = price * 0.5
    print(f"""
    Price for sky {product['sku']}
    is now {product['price']}""")
