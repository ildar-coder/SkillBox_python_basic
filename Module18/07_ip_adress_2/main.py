# TODO здесь писать код
def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return "Адрес — это четыре числа, разделённые точками."

    for part in parts:
        if not part.isdigit():
            return f"{part} — это не целое число."

        number = int(part)

        if not (0 <= number <= 255):
            return f"{part} превышает 255."

    return "IP-адрес корректен."


input_ip = input("Введите IP: ")
validation_result = is_valid_ip(input_ip)
print(validation_result)


