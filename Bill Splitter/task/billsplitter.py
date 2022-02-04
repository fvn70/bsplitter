import random


def calc_pay(bill, num):
    pay = bill / num
    return int(pay) if pay.is_integer() else round(pay, 2)


num = int(input("Enter the number of friends joining (including you):\n"))
if num <= 0:
    print("\nNo one is joining for the party")
else:
    dic = {}
    print("\nEnter the name of every friend (including you), each on a new line:")
    for n in range(num):
        name = input()
        dic[name] = 0

    bill = int(input("Enter the total bill value:\n"))
    pay = calc_pay(bill, num)
    for d in dic:
        dic[d] = pay

    if input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n') == "Yes":
        lucky = random.choice(list(dic.keys()))
        print(f"\n{lucky} is the lucky one!")
        pay = calc_pay(bill, num - 1)
        for name in dic.keys():
            dic[name] = round(pay, 2) if name != lucky else 0
    else:
        print("\nNo one is going to be lucky")

    print(dic)
