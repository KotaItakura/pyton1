if True:
    print("True")
else:
    print("F")

name = "gok"
isROL = name == "ROL"
print(isROL)
if isROL:
    print("俺")
else:
    print("俺以外")
number = 8
isOdd = number % 2

if 0:
    print("奇数")
else:
    print("偶数")

members = ["wakata","takai","fuji","terazawa"]
for member in members:
    print(member)

for i in range(5):
    print(i)

for i, member in enumerate(members):
    print(f"{i+1}番目のメンバーは{member}")

for member in members:
    print(member)
    if member == "fuji":
        print(f"{member}で終了")
        break

for member in members:
    if member == "takai":
        continue
    print(member)

num  = 1
print("Start")

while num < 6:
    print("num = " + str(num))
    num += 1