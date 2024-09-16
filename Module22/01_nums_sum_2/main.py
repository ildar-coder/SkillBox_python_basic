# TODO здесь писать код
numbers_file = open('numbers.txt', 'r')
sum_numbers = 0
for i_line in numbers_file:
    lst_int = list(map(int, i_line.split()))
    sum_numbers += sum(lst_int)
sum_numbers_str = str(sum_numbers)
numbers_file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(f'Содержимое файла answer.txt {sum_numbers_str}')
answer_file.close()
