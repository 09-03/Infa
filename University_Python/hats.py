"""
Король после пира в своём дворце дал команду страже арестовать 100 звездочётов,
так как они позже всех пришли на празднество и этим его обидели.
Он был любителем поиграть и приказал звездочётам выстроиться в ряд,
задумав надеть на их головы синие и красные шляпы.
После построения им будет запрещено общаться, издавать какие-либо звуки, оглядываться и снимать шляпы.
Однако разрешено смотреть на шляпы стоящих спереди и слушать ответы стоящих сзади.

Король будет подходить к каждому звездочёту и задавать один и тот же вопрос: «какого цвета твоя шляпа?»

Учёные должны ответить на вопрос короля только одним словом: «красная» или «синяя».
Неверный ответ карается тихой смертью, а за верный даруется жизнь (но всё равно придётся стоять безмолвно).

Король доходчиво объяснил, что в случае нарушения правил будет казнена вся сотня участников его игры.
После чего разрешил учёным посовещаться.

Какой алгоритм поможет спасти максимальное количество звездочётов?
"""
from random import randint


def survival_alg(W): # Для W = 100 С вероятностью 50% выживут 100 волжебников или 99 (с такой же вероятностью)
    hats = []
    num_visible_red_hats = 0
    survived_counter = 0
    for i in range(W):
        if randint(0,1) == 1:
            hats.append(["Red"])
            num_visible_red_hats +=1
        else:
            hats.append(["Blue"])

    for hat_color in hats:
        if hat_color == ["Red"]:
            num_visible_red_hats-=1
        hat_color.append(num_visible_red_hats % 2)

    if randint(0,1) == 1:
        hats[0].append("Red")

    else:
        hats[0].append("Blue")

    if hats[0][0] == hats[0][2]:
        survived_counter+=1

    for k in range(1, len(hats)):
        if hats[k-1][1] != hats[k][1]:
            hats[k].append("Red")

        else:
            hats[k].append("Blue")

        if hats[k][0] == hats[k][2]:
            survived_counter+=1

    return print(f"Выжило: {survived_counter}/{W}")


survival_alg(100)
