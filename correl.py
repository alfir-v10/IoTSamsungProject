hives = {
    'hive1': {
        'Temperature': 10,
        'Pressure': 15,
        'Humidity': 30,
        'Vibration': 10,
        'Luminosity': 40,
        'Weight': 100
    },
    'hive2': {
        'Temperature': 13,
        'Pressure': 15,
        'Humidity': 30,
        'Vibration': 12,
        'Luminosity': 45,
        'Weight': 100
    }
}
from math import sqrt
def sim_pearson(prefs,h1,h2):
    # получить список предметов оцененных обоими
    si = {}
    for item in prefs[h1]:
        if item in prefs[h2]:
            si[item] = 1
    n = len(si)
    # если нет ни одной общей оценки вернуть 0
    if n == 0: return 0

    #вычислить сумму всех предпочтений
    sum1 = sum([prefs[h1][it] for it in si])
    sum2 = sum([prefs[h2][it] for it in si])
    #вычислить сумму квадратов
    sum1Sq = sum([pow(prefs[h1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[h2][it], 2) for it in si])
    #вычислить сумму произведений
    pSum = sum([prefs[h1][it]*prefs[h2][it] for it in si])
    #вычислить коэф пирсона
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq - pow(sum1, 2)/n)*(sum2Sq - pow(sum2,2)/n))
    if den == 0: return 0
    r = num/den
    return r
print(sim_distance(hives,'hive1', 'hive2'))
print(sim_pearson(hives,'hive1', 'hive2'))