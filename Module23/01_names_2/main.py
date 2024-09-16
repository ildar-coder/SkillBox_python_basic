# TODO здесь писать код
line_count = 0
sum_sym = 0
with open('people.txt', 'r', encoding='utf-8') as people_file:
    for line in people_file:
        try:
            line_count += 1
            lenght = len(line.strip())
            sum_sym += lenght
            if lenght < 3:
                raise ValueError
        except ValueError as exc:
            print(f"менее трёх символов в строке {line_count}.")

print(f"Общее количество символов {sum_sym}")
