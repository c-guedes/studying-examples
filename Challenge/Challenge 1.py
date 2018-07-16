num = []
i = 0
c = 1

while i < 10:
    num.append(int(input("Insira o número" + " " + str(c) + ":")))
    i+=1
    c+=1

i = 0
while i <len(num):
    x = 0
    j = 0
    while j < len(num):
        if num[i] < num[j]:
            x = num[j]
            num[j] = num[i]
            num[i]= x
        j+=1
    i+=1
print(num)


