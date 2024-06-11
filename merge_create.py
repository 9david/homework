import json
from create_data import save_data_to_json

def merge_duplicates(duplicates):
    '''
    Эта функция принимает список групп дубликатов.
    Обходит каждую группу и создает объединенный словарь.
    Для каждого атрибута, если значения различаются, объединяет их в список уникальных значений.
    Возвращает список объединенных элементов.
    '''
    merged_data = []
    for group in duplicates:
        merged_item = {}
        for item in group["Duplicate"]:
            for key, value in item.items():
                if key not in merged_item:
                    merged_item[key] = value
                elif merged_item[key] != value:
                    if not isinstance(merged_item[key], list):
                        merged_item[key] = [merged_item[key]]
                    if value not in merged_item[key]:
                        merged_item[key].append(value)
        merged_data.append(merged_item)
    return merged_data

# Шаг 1: Загрузка данных из JS
with open('duplicates_data_all_keys_90%_similarity.js', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# Шаг 2: Объединение данных
merged_data = merge_duplicates(data)

# Шаг 3: Сохранение объединенных данных в формате JSON
save_data_to_json(merged_data, 'merge_data.js')