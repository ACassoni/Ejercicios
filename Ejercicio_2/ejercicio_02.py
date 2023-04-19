#Exercise 61
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2) # Si le pongo print me da None y si lo igualo a una variable y imprimo variable lo mismo
print(day1)

#Exercise 62
techs = ('python', 'java', 'sql', 'aws')
print(tuple(sorted(techs)))

#Exercise 63
hashtags = ['summer', 'time', 'vibes']
print("#" + "#".join(hashtags))

#Exercise 64
dictt = {}
dictt["USA"] = "Washington"
dictt["Gemany"] = "Berlin"
dictt["Austria"] = "Vienna"
print(dictt)

#Exercise 65
capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.keys())

#Exercise 66
print(capitals.values())

#Exercise 67
print(capitals.items())

#Exercise 68
print(capitals.get("Austria"))

#Exercise 69
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print(stocks["AAPL.US"])

#Exercise 70
print(stocks["MSFT.US"]["Microsoft Corp"])

#Exercise 71
stocks["MSFT.US"]["Microsoft Corp"] = 190
print(stocks["MSFT.US"])

#Exercise 72
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
stocks["V.US"] = {"Visa Inc" : 185}
print(stocks.values())

#Exercise 73
tickers = [
    'AAPL.US',
    'AXP.US',
    'BA.US',
    'CAT.US',
    'CSCO.US',
    'CVX.US',
    'DIS.US',
    'DOW.US',
    'GS.US',
    'HD.US',
    'IBM.US',
    'INTC.US',
]
lista = []
for x, y in enumerate(tickers):
    lista.append((x,y))

print(lista)

#Exercise 74
tick = {}
for x, y in enumerate(tickers):
    tick[x] = y

print(tick)

#Exercise 75
project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
print(sorted(set((project_ids.values()))))

#Exercise 76
stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
del stats["traffic"]
print(stats)

#Exercise 77
users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
print(users.get("004", "indefinite"))

#Exercise 78
filename = '01012020_sales.xlsx'
if filename.endswith("xlsx"):
    print("YES")
else:
    print("NO")

#Exercise 79
code = 'DSVNDOICSN'
if code.isupper():
    print("YES")

#Exercise 80
number = 1.0
if type(number) == int:
    print("Yes")
else:
    print("NO")

#Exercise 81
password = 'cskdnjcasa#!'
if len(password) >= 11:
    print("Password correct")
else:
    print("Password too short")

#Exercise 82
password = 'cskdnjcasa#!'
if len(password) >= 11 and "!" in password:
    print("Password correct")
else:
    print("Password incorrect")

#Exercise 83
project_ids = ['02134', '24253']
project_id = '02135'
if project_id not in project_ids:
    project_ids.append(project_id)
    print(project_ids)

#Exercise 84
project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}
if project_ids["02"] == "new":
    project_ids["02"] = "open"
    print(project_ids)

#Exercise 85
item = '001'
items = ['001', '000', '003', '005', '006']
if item in items:
    items.remove(item)
    print(items)

#Exercise 86
for i in range(1,100):
    if i % 11 == 0:
        print(i, end=",")
print("")

#Exercise 87
for i in range(1,100):
    if i % 11 == 0 and i % 3 != 0:
        print(i, end = ",")
print("")

#Exercise 88
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
for num in items[:]: # hago items[:] para hacer copia de items y asi hacer que no cambien de index y me de mal
    if num % 2 != 0:
        items.remove(num)
print(items)

#Exercise 89
items = [1, 5, 3, 2, 2, 4, 2, 4]
for num in items[:]: # sin hacer el [:] no funciona
    if items.count(num) > 1:
        items.remove(num)
print(items)

#Exercise 90
text = 'Python is a very popular programming language'
text = text.split(" ")
text = text[0:4]
for i in range(0, len(text)):
    text[i] = text[i].lower()
print(text)

#Exercise 91
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
for prob in probabilities:
    if prob < 0.5:
        probabilities.remove(prob)
print(probabilities)

#Exercise 92
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
for num in range(0, len(probabilities)):
    if probabilities[num] > 0.5:
        probabilities[num] = 1
    else:
        probabilities[num] = 0
print(probabilities)

#Exercise 93
item_dict = {}
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
for item in items:
    item_dict[item] = items.count(item)
print(item_dict)

#Exercise 94
text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""
text = text.split(" ")
for i in range(0, len(text)):
    text[i] = text[i].lower()
    text[i] = text[i].replace(".", "")
    text[i] = text[i].replace("\n", " ")
print(text)

#Exercise 95
indexes = [
    'BOVESPA',
    'DOW JONES COMP',
    'DOW JONES INDU',
    'DOW JONES TRANS',
    'DOW JONES UTIL',
    'IPC',
    'IPSA',
    'MERVAL',
    'NASDAQ COMP',
    'NASDAQ100',
    'S&P500',
    'S&P/TSX COMP',
]
# Era solo printear los que cumplen requisito pero lo puse en lista que es mas complicado
for index in indexes[:]:
    if not(index.startswith("DOW")) and not(index.startswith("S&P")):
        indexes.remove(index)
print(indexes)

#Exercise 96
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for key, item in gaming.items():
    if item > 100:
        print(key)

#Exercise 97
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
for name in names:
    if name.isalpha():
        print(f"Hello {name}!")

#Exercise 98
