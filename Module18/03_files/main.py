# TODO здесь писать код

symbols_start = tuple("@№$%^&*()\\")
symbols_end = ('.txt', '.docx')

file_name = input("Название файла: ")
if file_name.startswith(symbols_start):
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(symbols_end):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно')
