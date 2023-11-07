import time  # Importujemy moduł time, który pozwala nam pracować z czasem.

class AiRandsChoice:
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time())  # Jeśli nie podano ziarna, ustawiamy je na aktualny czas w sekundach od początku epoki Unix.
        self.seed = seed
        self.multiplier = int(time.time() * 10**6)  # Ustawiamy mnożnik na wartość aktualnego czasu w mikrosekundach.
        self.increment = int(time.time() * 10**9)  # Ustawiamy dodatek (inkrement) na wartość aktualnego czasu w nanosekundach.
        self.modulus = 2**32  # Ustawiamy wartość modułu, która ogranicza zakres generowanych liczb pseudolosowych.

    def next_int(self, max_value=None):
        self.seed = (self.seed * self.multiplier + self.increment) % self.modulus  # Wygenerowanie kolejnego pseudolosowego ziarna za pomocą liniowego generatora kongruencyjnego.
        if max_value is None:
            return self.seed  # Zwracamy wygenerowane pseudolosowe ziarno jako liczbę całkowitą.
        return self.seed % max_value  # Zwracamy wygenerowane pseudolosowe ziarno z ograniczeniem do zakresu od 0 do `max_value-1`.

    def weighted_choice(self, items, weights):
        total_weight = sum(weights)  # Obliczamy sumę wag wszystkich elementów, aby wygenerować zakres losowania.
        r = self.next_int(total_weight)  # Losujemy wartość `r` z zakresu od 0 do sumy wag.
        cumulative_weight = 0
        for item, weight in zip(items, weights):
            cumulative_weight += weight  # Dodajemy wagę aktualnego elementu do zmiennej `cumulative_weight`.
            if cumulative_weight > r:  # Sprawdzamy, czy `cumulative_weight` jest większe od wylosowanej wartości `r`.
                return item  # Jeśli tak, to oznacza, że osiągnęliśmy punkt na osi ważonej, w którym wybieramy odpowiedni element.

# Przykład użycia
# items = ["A", "B", "C"]  # Definiujemy listę `items`, zawierającą elementy, które chcemy losować.
# weights = [1, 1, 1]  # Definiujemy listę `weights`, która zawiera wagi odpowiadające elementom z listy `items`.

# aiRadsCho = AiRandsChoice()  # Tworzymy instancję klasy `AiRandsChoice`, używając domyślnego ziarna (aktualny czas).
# random_item = aiRadsCho.weighted_choice(items, weights)  # Wywołujemy metodę `weighted_choice` na instancji `custom_random`, aby wylosować element z listy `items` zgodnie z wagami z listy `weights`.
# print(random_item)  # Wypisujemy wylosowany element na ekranie.

# import awareness as a
# base = a.take_base('memory_CLO_v2010')
# lista = ['OR_3416', 'DO_5248', 'DO_6612', 'DO_967', 'OK_1289']
# wagi = [a.stats_part(base, w)['TOTAL'] for w in lista]

# print(lista)
# print(wagi)
# print(aiRadsCho.weighted_choice(lista, wagi))
