# TODO здесь писать код
file_text = open('text.txt', 'w')
file_text.write('Mama myla ramu.')
file_text.close()

file_text = open('text.txt', 'r')
frequency_analysis_dic = {}
text = file_text.readline().strip().lower()
text_no_spaces = ''.join(text.split()).rstrip('.')
for i_sym in text_no_spaces:
    if i_sym in frequency_analysis_dic:
        frequency_analysis_dic[i_sym] += 1
    else:
        frequency_analysis_dic[i_sym] = 1
print(frequency_analysis_dic)
sorted_frequency_analysis = sorted(frequency_analysis_dic.items(),
                                   key=lambda item: (-item[1], item[0])
                                   )
print(sorted_frequency_analysis)
file_text.close()

file_analysis = open('analysis.txt', 'w')
for key, value in sorted_frequency_analysis:
    file_analysis.write(f'{key}: {(value/len(text)):.3f}\n')
file_analysis.close()
