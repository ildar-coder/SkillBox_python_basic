# TODO здесь писать код
letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и",
          "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
          "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь",
          "э", "ю", "я"
          ]


def caesar_cipher(text: str, shift: int):
    ciphertext = ''
    for symbol in text:
        if symbol == " ":
            ciphertext += ' '
        elif letters.index(symbol) + shift > len(letters) - 1:
            i_cipher = (letters.index(symbol) + shift) % (len(letters) - 1) - 1
        else:
            i_cipher = letters.index(symbol) + shift
        ciphertext += letters[i_cipher]

    return ciphertext


print(caesar_cipher("это питон", 3))
