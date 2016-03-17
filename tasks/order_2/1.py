'''
Дан текст text и ограничение длины текста limit (в количестве символов). Необходимо, создать функцию trimmed_text(text, limit), которая в случае, если текст не помещается в ограничение обрезает его, но при этом слова не должны обрываться на середине (исключение первое слово), и в конце нужно добавить троеточие ("..."). Перед троеточием не должно быть других разделительных знаков
'''

def trimmed_text(text, limit):
    pass



if __name__=='__main__':
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 64) == 'Python is simple to use, but it is a real programming language.'
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 63) == 'Python is simple to use, but it is a real programming language.'
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 62) == 'Python is simple to use, but it is a real programming...'
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 33) == 'Python is simple to use, but...'
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 28) == 'Python is simple to use...'
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 19) == 'Python is simple...'
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 9) == 'Python...'
   assert trimmed_text('Python is simple to use, but it is a real programming language.', 7) == 'Pyth...' 
