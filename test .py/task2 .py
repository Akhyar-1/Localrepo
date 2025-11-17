fruits = ["apple", "banana", "cherry", "date"]
fruits.append("pineapple")
print(fruits)

fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry", "date"]
fruits.insert(1, "kiwi")
print(fruits)

fruits = ["apple", "banana", "cherry", "date"]
fruits.reverse()
print (fruits)

fruits = ["apple", "banana", "cherry", "date"]
fruits = [f for f in fruits if f.startswith("a")]
print(fruits)