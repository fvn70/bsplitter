
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
    check = bill / num
    check = round(check, 2) if check != bill // num else int(check)

    for d in dic:
        dic[d] = check

    print(dic)
