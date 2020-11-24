"""
Написать программу, реализующую цикл «for», в том числе с принудительным его
завершением, например, для определения стихотворного размера.
"""

"""
Примеры текстов:
Хорей:
бУ/ря мглО/ю нЕ/бо крО/ет вИх/ри снЕж/ны/е кру/тЯ
Ямб:
тЫ по/грус/тИ, ко/гдА ум/рЁт по/Эт, по/кУ/да звОн бли/жАй/шей Из цер/квЕй нЕ воз/вес/тИт, чтО Э/тот нИз/кий свЕт Я про/мен/Ял нА нИз/ший мИр чер/вЕй.
Дактиль:
тУч/ки не/бЕс/ны/е, вЕч/ны/е стрАн/ни/ки! стЕпь/ю ла/зУр/но/ю, цЕпь/ю жем/чУж/но/ю…
Амфибрахий:
до/рО/же от/чИз/ны — нЕ знАл ни/че/гО бо/Ец, нЕ лю/бИв/ший по/кО/я.
Анапест:
ночь хо/лОд/на/я мУт/но гля/дИт под ро/гО/жу ки/бИт/ки мо/Ей, под по/лОзь/я/ми пО/ле скри/пИт, под ду/гОй ко/ло/кОль/чик зве/нИт, а ям/щИк по/го/нЯ/ет ко/нЕй.
"""

def horei(udar):
    match = 0
    horei_syllable = []
    for i in range(1,len(udar)+1):
        syllable = 2*i - 1
        horei_syllable.append(syllable)
    for item in udar:
        if item in horei_syllable:
            match+=1
    return match

def yamb(udar):
    match = 0
    yamb_syllable = []
    for i in range(1,len(udar)+1):
        syllable = 2*i
        yamb_syllable.append(syllable)
    for item in udar:
        if item in yamb_syllable:
            match+=1
    return match

def daktil(udar):
    match = 0
    daktil_syllable = []
    for i in range(1,len(udar)+1):
        syllable = 3*i - 2
        daktil_syllable.append(syllable)
    for item in udar:
        if item in daktil_syllable:
            match+=1
    return match

def amfibr(udar):
    match = 0
    amfibr_syllable = []
    for i in range(1,len(udar)+1):
        syllable = 3*i - 1
        amfibr_syllable.append(syllable)
    for item in udar:
        if item in amfibr_syllable:
            match+=1
    return match

def anapest(udar):
    match = 0
    anapest_syllable = []
    for i in range(1,len(udar)+1):
        syllable = 3*i
        anapest_syllable.append(syllable)
    for item in udar:
        if item in anapest_syllable:
            match+=1
    return match


text = input("Введите форматированный текст для анализа: ").translate(str.maketrans({",": "",".": "","?": "","!": "",":": "",";": "","(": "",")": "","-": ""})).split()
syllable_num = 0
udar = []
for word in range(len(text)):
    text[word] = text[word].split("/")
    for syllable in range(len(text[word])):
        syllable_num+=1
        for char in text[word][syllable]:
            if char.isupper():
                udar.append(syllable_num)

poem_dict = {"Хорей" : horei(udar),
             "Ямб" : yamb(udar),
             "Дактиль" : daktil(udar),
             "Амфибрахий" : amfibr(udar),
             "Анапест" : anapest(udar),
}

max_match = max(horei(udar), yamb(udar), daktil(udar), amfibr(udar), anapest(udar))
for key, value in poem_dict.items():
    if value == max_match:
        print(f"Данное стихотворение написано в размере '{key}'")
        break
