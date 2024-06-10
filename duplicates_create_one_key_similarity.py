import json
from difflib import SequenceMatcher
from create_data import save_data_to_json

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_duplicates(data, key, threshold=0.8):
    '''
    Используется метод сортированных соседей (Sorted Neighborhood Method).
    Этот метод основан на сортировке данных по определенному ключу
    и сравнении соседних записей для обнаружения дубликатов.
    '''
    data_sorted = sorted(data, key=lambda x: x[key])
    duplicates = []
    visited = [False] * len(data_sorted)

    for i in range(len(data_sorted) - 1):
        if visited[i]:
            continue
        group = [data_sorted[i]]
        for j in range(i + 1, len(data_sorted)):
            if similarity(data_sorted[i][key], data_sorted[j][key]) >= threshold:
                group.append(data_sorted[j])
                visited[j] = True
        if len(group) > 1:
            duplicates.append({"Duplicate": group})

    return duplicates

with open('tv_data.js', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Поиск дубликатов
duplicates = find_duplicates(data, key='Название')

# Сохранение дубликатов в формате JSON
save_data_to_json(duplicates, 'duplicates_data_one_key_similarity.js', duplicate=True)

