existing_good_log_lines = set()
existing_bad_log_lines = set()

# Считываем уже существующие плохие логи, чтобы избежать дублирования
try:
    with open('registrations_bad.log', 'r', encoding='utf-8') as f:
        for line in f:
            existing_bad_log_lines.add(line.strip())
except FileNotFoundError:
    pass

# Считываем уже существующие хорошие логи, чтобы избежать дублирования
try:
    with open('registrations_good.log', 'r', encoding='utf-8') as f:
        for line in f:
            existing_good_log_lines.add(line.strip())
except FileNotFoundError:
    pass

def register_bad_log(text, exception: str):
    with open('registrations_bad.log', 'a', encoding='utf-8') as f:
        row = '\t'.join([text, exception])
        if row.strip() not in existing_bad_log_lines:
            f.write(row + '\n')
            existing_bad_log_lines.add(row.strip())

def register_good_log(text):
    with open('registrations_good.log', 'a', encoding='utf-8') as f:
        if text.strip() not in existing_good_log_lines:
            f.write(text + '\n')
            existing_good_log_lines.add(text.strip())

with open('registrations.txt', 'r', encoding='utf-8') as registr_file:
    for i_line in registr_file:
        user_info = i_line.split()
        line = ' '.join(user_info)
        try:
            if len(user_info) != 3:
                raise IndexError("Присутствуют не все три поля")
            if not user_info[0].isalpha():
                raise NameError("Поле «Имя» не содержит только буквы")
            if '@' not in user_info[1] or '.' not in user_info[1]:
                raise SyntaxError("Поле «Имейл» не содержит @ или . (точку)")
            if int(user_info[2]) < 10 or int(user_info[2]) > 99:
                raise ValueError('Поле «Возраст» не является числом от 10 до 99')

        except IndexError as exc:
            register_bad_log(line, str(exc))
        except NameError as exc:
            register_bad_log(line, str(exc))
        except SyntaxError as exc:
            register_bad_log(line, str(exc))
        except ValueError as exc:
            register_bad_log(line, str(exc))
        else:
            register_good_log(line)

print(existing_bad_log_lines)
print(existing_good_log_lines)