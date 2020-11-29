numbers = "1 2 3 4 5 6 7 8 9"
symbols = ["", "-", "+"]
equations_list = []

for i in range(3):
    place1 = numbers.replace(" ", symbols[i], 1)
    for j in range(3):
        place2 = place1.replace(" ", symbols[j], 1)
        for k in range(3):
            place3 = place2.replace(" ", symbols[k], 1)
            for a in range(3):
                place4 = place3.replace(" ", symbols[a], 1)
                for b in range(3):
                    place5 = place4.replace(" ", symbols[b], 1)
                    for c in range(3):
                        place6 = place5.replace(" ", symbols[c], 1)
                        for d in range(3):
                            place7 = place6.replace(" ", symbols[d], 1)
                            for e in range(3):
                                place8 = place7.replace(" ", symbols[e], 1)
                                if eval(place8) == 100:
                                    equations_list.append(place8)

print(equations_list)
