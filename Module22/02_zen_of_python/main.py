# TODO здесь писать код
zen_file = open('zen.txt', 'r')
lines = zen_file.readlines()
reverse_text = lines[::-1]
for line in reverse_text:
    print(line.strip())
zen_file.close()


