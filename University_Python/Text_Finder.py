def sorting_and_printing(dictionary, label):
    ans = ""
    sorted_dict = {k: v for k, v in sorted(dictionary.items(), key = lambda item: item[1], reverse = True)}
    values_view = sorted_dict.values()
    value_iterator = iter(values_view)
    max_value = next(value_iterator)

    print(f"Наиболее {label} слово:", end="")
    for key, value in sorted_dict.items():
        if value == max_value:
            ans += f" {key},"

    ans = ans[:-1]
    print(ans)


def text_processor(text):
    lenth_counter = {}
    freq_counter = {}
    refined_text = text.lower().translate(str.maketrans({",": "",
                                                         ".": "",
                                                         "?": "",
                                                         "!": "",
                                                         ":": "",
                                                         ";": "",
                                                         "(": "",
                                                         ")": "",
                                                         "-": ""
                                                                }))

    for word in refined_text.split():
        if word in freq_counter:
            freq_counter[word] += 1

        else:
            freq_counter[word] = 1

        if word not in lenth_counter:
            lenth_counter[word] = len(word)

    for word in refined_text.split():
        if word not in lenth_counter:
            lenth_counter[word] = len(word)

    sorting_and_printing(freq_counter, "частое")
    sorting_and_printing(lenth_counter, "длинное")


text = input("Введите текст для обработки: ")
text_processor(text)
