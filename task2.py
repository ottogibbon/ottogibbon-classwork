list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
list2 = []
count = 0

for index in range(0,(len(list1) -1)):
 if (list1[index] >=80) and (list1[index] <=100):
   count = count + 1
 else: 
    list2.append(list1[index])

print("Numbers of Numbers in range 80-100: " + str(count))
print(list2)
