print("welcome 2 calcu1ator \n")
print("type the option you want \n, 1. addition \n 2. subtraction \n 3. divide \n 4. multiply")
optionSel = int(input("write here: "))


second_sum = float(input("Second: "))
first_sum = float(input("first: "))
subtraction = first_sum - second_sum
addition = first_sum + second_sum
divide = first_sum / second_sum
multiply = first_sum * second_sum

def calc_startup():
    if optionSel == 1:
        print(addition)
    elif optionSel == 2:
        print(subtraction)
    elif optionSel == 3:
        print(divide)
    elif optionSel == 4:
        print(multiply)

calc_startup()
