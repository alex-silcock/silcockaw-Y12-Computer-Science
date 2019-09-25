mylist = []
total = 0
outlet1 = [10,12,15,10]
outlet2 = [5,8,3,6]
outlet3 = [10,12,15,10]

mylist.append(outlet1)
mylist.append(outlet2)
mylist.append(outlet3)
#print(mylist[0][0])
for i in range(0,3):
  for j in range(0,4):
    total = total + mylist[i][j]
  print("Value for quarter", (i + 1), ":", total)
  total = 0






