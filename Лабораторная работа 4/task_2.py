NUMS = range(10)

def isaplpha(sym):
    if sym in NUMS:
        return True
    return False


def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = ''.join(str_.lower())
    text = ''.join(str_.replace('.','').replace(',','').replace('!','').split())

    dic = {}
    for s in text:
        if not isaplpha(s):
            if s not in dic:
                dic[s] = 1
            else:
                dic[s] = dic[s] + 1
    return dic

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
