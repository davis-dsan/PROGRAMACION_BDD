count = 0
res = 0

while count < 10:
    count +=1
    if count == 4:
        print("Hola")
        break
    res = count + res
    print(count)
print(res)