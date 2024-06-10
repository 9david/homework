import json
from difflib import SequenceMatcher
from create_data import save_data_to_json


def similarity(a, b):
    """Вычисляет схожесть двух строк."""
    return SequenceMatcher(None, a, b).ratio()

def is_duplicate(item1, item2, keys, threshold=0.9):
    """Проверяет, являются ли два элемента дубликатами на основе схожести всех ключей."""
    for key in keys:
        if similarity(str(item1[key]), str(item2[key])) < threshold:
            return False
    return True

def find_duplicates(data, threshold=0.9):
    """Находит дубликаты в данных на основе схожести всех ключей."""
    keys = data[0].keys()
    duplicates = []
    visited = [False] * len(data)

    for i in range(len(data) - 1):
        if visited[i]:
            continue
        group = [data[i]]
        for j in range(i + 1, len(data)):
            if is_duplicate(data[i], data[j], keys, threshold):
                group.append(data[j])
                visited[j] = True
        if len(group) > 1:
            duplicates.append({"Duplicate": group})

    return duplicates

# Шаг 1: Загрузка данных из JS
with open('tv_data.js', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Шаг 2: Поиск дубликатов
duplicates = find_duplicates(data, threshold=0.9)  # Установите порог в 90% схожести

# Шаг 3: Сохранение найденных дубликатов в формате JSON
save_data_to_json(duplicates, 'duplicates_data_all_keys_90%_similarity.js', duplicate=True)

