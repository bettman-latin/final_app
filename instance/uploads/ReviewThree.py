list1 = [0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12, 0, 14, 0, 16]

def removeInRange(list, start, stop, element):
    for x in list[start:stop]:
        if x == element:
            list.remove(element)
            print(list1)
    return

def removeInRange2(list, start, stop, element):
    for x in list[start:stop]:
        if x == element:
            list.remove(element)
    return
removeInRange(list1, 1, 17, 0)

thisdict = {
  42: "Marty",
  81: "Sue",
  17: "Ed",
  31: "Dave",
  56: "Ed",
  3: "Marty",
  29: "Ed"
}
print(thisdict)

reversed_dictionary = {value : key for (key, value) in thisdict.items()}
#thisdict.items takes the key and value pair, sets them to the key, value 
#variables, and then using : reverses the order of them
#since it stays as a dictionary it automatically keeps unique keys
#found it online, but I thought it was a cool solution
print(reversed_dictionary)