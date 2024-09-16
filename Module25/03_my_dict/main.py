# TODO здесь писать код
class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, key, default=0):
        return super().get(key, default)


my_dict = MyDict(a=5, b=6)
print(my_dict.get('a'))
print(my_dict.get('b'))
print(my_dict.get('c'))

my_other_dict = MyDict({'d': 7, 'e': 8})
print(my_other_dict.get('d'))
print(my_other_dict.get('e'))
print(my_other_dict.get('f'))
