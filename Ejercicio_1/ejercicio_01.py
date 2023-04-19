# Exercise 26
text = 'Python Course'
print(text[::-1])

# Exercise 27
var1 = ''
var2 = ' '
var3 = '\n'
print(type(var1))
print(type(var2))
print(type(var3))

#Exercise 28
var1 = None
var2 = False
var3 = 'True'
print(type(var1))
print(type(var2))
print(type(var3))

#Exercise 29
flag = False
print(isinstance(flag, bool))

#Exercise 30
text = 'python is a popular programming language.'
print(text.capitalize())

#Exercise 31
print(text.count("p"))

#Exercise 32
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
print("code1: " + str(code1.endswith("2020")))
print("code2: " + str(code2.endswith("2020")))

#Exercise 33
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
print("path1: " + str(path1.startswith("youtube")))
print("path2: " + str(path2.startswith("youtube")))

#Exercise 34
path1 = (
    'https://e-smartdata.teachable.com/p/'
    'sciezka-data-scientist-machine-learning-engineer'
)
path2 = (
    'https://e-smartdata.teachable.com/p/'
    'sciezka-data-scientist-deep-learning-engineer'
)
path3 = (
    'https://e-smartdata.teachable.com/p/'
    'sciezka-bi-analyst-data-analyst'
)

print("path1: " + str(path1.find("scientist")))
print("path2: " + str(path2.find("scientist")))
print("path3: " + str(path3.find("scientist")))

#Exercise 35
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'

print("code1: " + str(code1.isalnum()))
print("code2: " + str(code2.isalnum()))

#Exercise 36
text = 'Google Colab'
print(text.lower())

#Exercise 37
text = 'Google Colab'
print(text.upper())

#Exercise 38
print(text.strip())

#Exercise 39
code = 'FVNISJND-XX'
print(code.replace("-", " "))

#Exercise 40
text = '340-23-245-235'
print(text.replace("-", ""))

#Exercise 41
text = 'Open,High,Low,Close'
print(text.split(","))

#Exercise 42
text = """Python is a general-purpose language.
Python is popular."""
print(text.split("\n"))

#Exercise 43
num = 34
print(str(num).zfill(6))

#Exercise 44
url = (
    'https://e-smartdata.teachable.com/'
    'p/sciezka-data-scientist-machine-learning-engineer'
)
url = url[url.rfind("/"):]
print(url.replace("-", " "))

#Exercise 45
subjects = {'mathematics', 'biology'}
subjects.add("english")
print(subjects)

#Exercise 46
text = 'Programming in python.'
text = text.lower()
text = text.replace(".", "")
text = text.replace(" ", "")
letters = set(text)
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = letters.difference(vowels)
print(len(letters))

#Exercise 47
A = {2, 4, 6, 8}
B = {4, 10}
print(A.symmetric_difference(B))

#Exercise 48

ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
print("Selected ID: " + str(ad1_id.symmetric_difference(ad2_id)))

#Exercise 49

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
print("Customer ID: " + str(is_clicked.intersection(is_bought)))

#Exercise 50

dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
dji3 = dji1 + dji2
print(dji3)


#Exercise 51
# Le agrego una coma al final de cada tuple para poder hacerle nest
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US'),
dji2 = ('HD.US', 'GS.US', 'NKE.US'),
dji4 = dji1 + dji2
print(dji4)

#Exercise 52

members = (('Kate', 23), ('Tom', 19))
members = (members[0], ('John', 26), members[1])
print(members)

#Exercise 53

default = ('YES', 'NO', 'NO', 'YES', 'NO')
print("Number of occurrences: " + str(default.count("YES")))

#Exercise 54

names = ('Monica', 'Tom', 'John', 'Michael')
print(tuple(sorted(names)))

#Exercise 55
from operator import itemgetter
info = (('Monica', 19), ('Tom', 21), ('John', 18))
print("Ascending: " + str(sorted(info, key = lambda x: x[1])))
print("Descending: " + str(sorted(info, key = lambda x: x[1], reverse = True)))


#Exercise 56
stocks = (('Apple Inc', ('AAPL.US', 310)), ('Microsoft Corp', ('MSFT.US', 184)))
print(stocks[0][1][0])

#Exercise 57
cities = ['Los Angeles', 'New York', 'Chicago']
cities.append("Houston")
print(cities)


#Exercise 58
idx = ['001', '002', '001', '003', '001']
print("Number of occurences: " + str(idx.count("001")))

#Exerwcise 59
text = 'Python programming'
text = text.lower()
text = set(text.replace(" ", ""))
print(sorted(list(text)))


#Exercise 60
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, "phone.jpg")
filenames.remove("ball.png")
print(filenames)
