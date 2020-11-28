import random
n = int(input("Введите количество участников: "))
list = [[i+1, i+1] for i in range(n)]
random.shuffle(list)
temp = list[0][1]
for i in range(n):
    if i == n-1:
        list[i][1] = temp
    else:
        list[i][1] = list[i+1][1]
    file = open(f"SecretSanta{i+1}.txt", "w")
    file.write(f"Ваш номер участника: {list[i][0]}\nВы дарите подарок участнику под номером: {list[i][1]}")
    file.close()
