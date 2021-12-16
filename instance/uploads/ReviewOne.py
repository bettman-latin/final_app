# print("input a number: ")
# x = int(input())

# def zeroDigits(x):
#     count = 0
#     digits = str(x)
#     for each in digits:
#         if each == "0":
#             count += 1
#     return count

# print(zeroDigits(x))

# def minmax():
#     y = 0
#     min = 0
#     max = 0
#     print("Type a number: ")
#     y = int(input())
#     while y != -1:
#         if y > max:
#             max = y
#         if y < min:
#             min = y
#         print("Type a number: ")
#         y = int(input())
#     print("Minimum Number Was: ", min)
#     print("Maximum Number Was: ", max)   
# minmax()


# def message():        
#     print("Type something: ")
#     x = input()
#     try:
#         y = int(x)
#         print("You typed the integer: ", y)
#     except ValueError:
#         try:
#             y = float(x)
#             print("You typed the float: ", y)
#         except ValueError:
#             print("Not a Number!")

# message()


def GCD(x,y):
    if x == 0:
        return (x)
    else:   
        return GCD(y, x % y)


x = input("Type Number: ")
y = input("Type Another Number: ")

x = int(x) # converts to int
y = int(y) # converts to int
print (GCD(x,y))

# matrix1 = [[1, 2, 3,],[4, 5, 6],[7, 8, 9]]
# print (matrix1[1][2]) #prints second row, third collumn
# matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# print (matrix2[1][2])


