# TODO здесь писать код
import random
fst_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
scd_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [fst_team[i] if fst_team[i] > scd_team[i] else scd_team[i] for i in range(20)]
print("Первая команда:", fst_team)
print("Вторая команда:", scd_team)
print("Победители тура:", winners)
