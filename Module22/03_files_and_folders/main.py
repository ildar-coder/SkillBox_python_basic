# TODO здесь писать код
import os

# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кб):  9.61
# Количество подкаталогов:  3
# Количество файлов:  7 /Users/ildardautov/Dev/SKILLBOX/Python_Basic/Module14

def get_directory_info(directory_path):
    directory_size = 0
    num_dir = 0
    num_files = 0

    for dirpath, dirnames, filenames in os.walk(directory_path):
        num_dir += len(dirnames)
        num_files += len(filenames)
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            directory_size += os.path.getsize(file_path)

    directory_size_kb = directory_size / 1024

    return directory_size_kb, num_dir, num_files


path_in_example = os.path.abspath(os.path.join('..', '..', 'Module14'))

size_kb, dirs, files = get_directory_info(path_in_example)
print(f'Размер каталога {path_in_example} (в Кб): {size_kb:.2f}')
print(f'Количество подкаталогов: {dirs}')
print(f'Количество файлов: {files}')
