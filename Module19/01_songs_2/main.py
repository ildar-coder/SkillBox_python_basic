violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
# Сколько песен выбрать? 3
# Название первой песни: Halo
# Название второй песни: Enjoy the Silence
# Название третьей песни: Clean
#
# Общее время звучания песен: 14.93 минуты
# TODO здесь писать код
songs_count = int(input("Сколько песен выбрать? "))
duration_of_sound = []
for i_song in range(songs_count):
    song_name = input("Название {}-й песни: ".format(i_song + 1))
    duration_of_sound.append(violator_songs[song_name])
print("\nОбщее время звучания песен: {} минуты".format(sum(duration_of_sound)))
