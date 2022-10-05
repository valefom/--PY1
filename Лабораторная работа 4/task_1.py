# TODO реализовать функцию
def remove_whitespace(str_):
    new_text = []
    idx = []
    s_prev = ''
    for i, v in enumerate(str_):
        if i > 0:
            if(str_[i] == str_[i-1] and str_[i] == ' '):
                new_text.append('')
                #new_text.appen('')
            else:
                new_text.append(str_[i])
        else:
            new_text.append(str_[i])
    return ''.join(new_text)

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
