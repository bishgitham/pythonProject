
# list exercise append, extend, merge two lists, insert, index
tropical_fruits = ["papaya", "mango", "jackfruit", "tomato", "banana"]

print (tropical_fruits)
print (tropical_fruits[0])
print (tropical_fruits [3])
print (tropical_fruits [-1])

tropical_fruits.append("newfruit")
print (tropical_fruits)
tropical_fruits.append("fruit")
print(tropical_fruits)
tropical_fruits.pop(1)
print (tropical_fruits)

winter_fruits = ["apple", "orange", "grape", "kiwi"]

fruits =[]
fruits =list(tropical_fruits+winter_fruits)
print(fruits)