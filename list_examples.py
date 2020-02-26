thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.sort()
thislist.append("guinep")
thislist.insert(2, "sea grapes")
print(thislist)
thislist.remove("banana")
#print(thislist)

list_of_lists = [[1,2,3,"dog", "cat"],
                 [2,4,5],
                 [3,7,12]]

print()
for row in range(len(list_of_lists)):
    for column in range(len(list_of_lists[row])):
        print("Row",  row, "Column", column, "=", list_of_lists[row][column])

print()
for the_list in list_of_lists:
    for counter in range(len(the_list)):
        print(the_list[counter])


x = 5
y = x
y+= 1
print()
print("X =", x)
print("Y =", y)


pets = ["dog", "cat", "bird", "snake", "fish"]
copy_of_pets = pets.copy()
copy_of_pets.append("hamster")
print()
print(pets)
print(copy_of_pets)

person = ["Roy", "Biv", "male", 37, "Rainbow Hunter"]
print()
print(person[2])

#Dictionary Examples
the_person = {"first_name":"Roy",
              "last_name": "Biv",
              "gender":"male",
              "age": 37,
              "job": "Rainbow Hunter"}

print(the_person["age"])
the_person["allergies"] = "none"

#Print all members of the dictionary
for key,value in the_person.items():
    print(key, ":", value)

kids = {"child1":{"name": "Jerry", "age": 14},
        "child2":{"name": "Katie", "age": 12},
        "child3":{"name": "Cora", "age": 7}}

print()
for key,value in kids.items():
    print()
    print(key)
    print("--------")
    for k,v in value.items():
        print(k, v)

#Set Examples
print()
my_list = [1,1,1,2,2,3,3,44,66,7,7,7,8,8,19]
my_list = set(my_list)
print(my_list)

my_set = {1,1,1,2,2,3,3,44,66,7,7,7,8,8,19}
print(my_set)








