# 5.1
# def multiplication(a: float, b: float) -> float:
#     """
#     mulitiplie a par b

#     a float le nombre a
#     b float le nombre b
#     return float
#     """
#     return a * b

# print(help(multiplication))

# 5.2
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(my_text.find("minim"))


# 5.3
print(my_text[12:21])

# 5.4
print(my_text.split(" ")[5])

#5.5
ligne = 0
for i in range (len(my_text)):
    if my_text[i] == ".":
        ligne += 1
print(ligne)



