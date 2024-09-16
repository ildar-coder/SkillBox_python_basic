# TODO здесь писать код
import os

from collections import Counter

file_text = open('voyna-i-mir.txt', 'r')
text = file_text.read().strip()
text_no_spaces = ''.join(text.split())
counter = Counter(text_no_spaces)
sorted_text_to_count = sorted(counter.items(),
                              key=lambda item: item[1],
                              reverse=True)
file_text.close()

file_answer = open('answer.txt', 'w')
for i_item in sorted_text_to_count:
    file_answer.write(f'{i_item[0]}: {i_item[1]}\n')
file_answer.close()
text_path = os.path.abspath('voyna-i-mir.txt')
