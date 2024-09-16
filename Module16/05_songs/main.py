violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
N = int(input("Сколько песен выбрать? "))
total_time = 0

for i in range(N):
    song_title = input(f"Название {i+1}-й песни: ")
    for song in violator_songs:
        if song[0] == song_title:
            total_time += song[1]
            break

print(f"\nОбщее время звучания песен: {total_time} минуты")