items = ["cat", "dog", "pig", "fox"] # make list

items.append("frog") # add "frog" to end

items.insert(0, "raccoon") # add "raccoon" to position 0

x = items.pop(3) # remove item at index 3

items.remove("pig") # remove item "pig"

items.sort() # sort origional list

new_items = sorted(items) # save a sorted version of list 

items.reverse() # reverse origional list

new_items = reversed(items) # save a reversed version of list

items[1] = "kitten" # change item at index 1 to "kitten"

a = items[0] # stores first item of list

b = items[1:] # stores from index 1 to end

c = items[::2] # stores every other element
#
# [start:stop:skip]
#
#
for each in items: # print each item in list by element
    print(each)

for i in range len(items): # print each item by index
    print(items[i])

i = 0
while i < len(items): # print each item by a count system
    print(items[i])
    i += 1