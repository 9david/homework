import csv
import json
from difflib import SequenceMatcher
from create_data import save_data_to_json


def similarity(a, b):
    """Вычисляет схожесть двух строк."""
    return SequenceMatcher(None, a, b).ratio()

def average_similarity(item1, item2, keys):
    """Вычисляет среднюю схожесть по всем ключам."""
    total_similarity = 0.0
    for key in keys:
        total_similarity += similarity(str(item1[key]), str(item2[key]))
    return total_similarity / len(keys)

def find_duplicates(data, threshold=0.8):
    """Находит дубликаты в данных на основе средней схожести всех ключей."""
    keys = data[0].keys()
    duplicates = []
    visited = [False] * len(data)

    for i in range(len(data) - 1):
        if visited[i]:
            continue
        group = [data[i]]
        for j in range(i + 1, len(data)):
            if average_similarity(data[i], data[j], keys) >= threshold:
                group.append(data[j])
                visited[j] = True
        if len(group) > 1:
            duplicates.append({"Duplicate": group})

    return duplicates


# Шаг 1: Загрузка данных из JS
with open('tv_data.js', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Шаг 2: Поиск дубликатов
duplicates = find_duplicates(data)

# Шаг 3: Сохранение найденных дубликатов в формате JSON
save_data_to_json(duplicates, 'duplicates_data_all_keys_average_similarity.js', duplicate=True)

