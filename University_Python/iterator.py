import random
list = [i+1 for i in range(100)]
def iter(list):
    done = False
    i = 1
    while not done:
        if random.random() < 1/len(list):
            x = list[i-1]
            print(x)
            if i==len(list):
                i=1
            else:
                i+=1
            if input("Продолжаем? ") != "y":
                done = True
        if i==len(list):
            i=1
        else:
            i+=1

iter(list)
