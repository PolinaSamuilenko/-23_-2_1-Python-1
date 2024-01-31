# TODO  Напишите функцию count_letters
def count_letters(text):
    text_lower = text.lower()
    list_text = list(text_lower)

    letter_list = []
    for letter in list_text:
        if letter.isalpha():
            letter_list += letter
    letter_dict = {}
    for letters in letter_list:
        if letters in letter_dict:
            letter_dict[letters] += 1
        else:
            letter_dict[letters] = 1
    return letter_dict

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_):
    summary_letters = 0
    for key_let in dict_:
        summary_letters += dict_.get(key_let)

    frequency_dict = {}
    for key_letter in dict_:

        frequency_dict[key_letter] = round(dict_.get(key_letter) / summary_letters, 2)

    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
frequency_ = calculate_frequency(count_letters(main_str))
for i in frequency_:
    print(f"{i}: {frequency_[i]}")