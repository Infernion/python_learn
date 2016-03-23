"""
написать программу которая будет выводить строку в обратном порядке
original = "I like this World"
result = "dlroW siht ekil I"
"""

def reverser(text):
    i = len(text)
    new = ''
    while i != 0:
        i -= 1
        new += text[i]
    return new


if __name__=='__main__':
    # проверка результатов
    assert reverser('I like this World') == 'dlroW siht ekil I'
    assert reverser('Love is ...') == '... si evoL'