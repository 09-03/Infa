import random
massive_n = [i+1 for i in range(int(input("Введите длину массива n: ")))]
def iter(list):
    massive_m = []
    m=int(input("Введите длину итогового массива m: "))
    counter = 0
    done = False
    i = 1
    while not done:
        if random.random() < 1/len(list):
            x = list[i-1]
            massive_m.append(x)
            counter+=1
            if i==len(list):
                i=1
            else:
                i+=1
            if counter == m:
                done = True
        if i==len(list):
            i=1
        else:
            i+=1
    return massive_m

print(iter(massive_n))
