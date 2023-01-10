# 変数とは何か？
# 型とはなにか？これだけおぼえておけばok

# str
name = "Wakata"
print(name)
print(type(name)) # typeで変数の型がわかる。

# int
number = 20
print(number)
print(type(number)) 

# float
number = 1.5
print(number)
print(type(number))

number = 20.0
print(number)
print(type(number))

# bool
is_vebots = True
print(is_vebots)
is_vebots = False
print(is_vebots)
print(type(is_vebots))

zero = 1
isZero = zero == 0
print(isZero) # True or False ? 
print(type(isZero))

# list
members = ["wakata","takai","fujii"]
print(members)
print(type(members))

member = members[1] #list内の要素にインデックス（何番目的な）でアクセスできる
print(member) #誰がでるかな？
print(type(member))

# dictionary
vebots_teachers = {'准教授' : "岡本先生", '教授' : "野口先生"} # keyとvalueの組み合わせ
print(vebots_teachers)
print(type(vebots_teachers))

professor = vebots_teachers["教授"] #key（准教授、教授など）をもとに要素にアクセスできる
print(professor)
print(type(professor))

# 変数名の規約（こう名付けたほうがいいよ）というものがあるよ
# https://qiita.com/naomi7325/items/4eb1d2a40277361e898b

class Human:

  def __init__(self, name, year):
    
    self.name = name
    self.year = year

Kota = Human("ITAKURA KOTA",22)
print(Kota.name)
print(type(Kota))
print(Kota.year)
print(type(Kota))

def twice(number):
    number = number *2
    return number

age = 22
age = twice(age)
print(age)

def greet(name):
    text = f"おはよう{name}"
    return text
