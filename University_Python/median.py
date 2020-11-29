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

def median(massive_m):
    median = []
    i=0
    done = False
    while not done and i !=len(massive_m):
        if input("Добавить число в массив?: ") == "y":
            median.append(massive_m[i])
            median.sort()
            print(median)
            i+=1
            if i % 2 != 0:
                print(f"Медиана: {median[len(median) // 2]}")
            else:
                print(f"Медиана: {(median[len(median) // 2 - 1] + median[len(median) // 2]) / 2}")
        else:
            print("Done")
            done = True

median(iter(massive_n))
