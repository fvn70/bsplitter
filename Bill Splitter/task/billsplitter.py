num = int(input("Enter the number of friends joining (including you):\n"))
if num <= 0:
    print("\nNo one is joining for the party")
else:
    dic = {}
    print("\nEnter the name of every friend (including you), each on a new line:")
    for n in range(num):
        name = input()
        dic[name] = 0
    print(dic)