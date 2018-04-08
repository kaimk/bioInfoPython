meine_list = []
for i in range(1, 100):
    meine_list.append(i)

var1 = 0
var2 = 0

for i in meine_list:
    if i %2 == 0:
        var1 += i
    else:
        var2 += i

print(var1)
print(var2)