import json
from difflib import SequenceMatcher
from create_data import save_data_to_json
from abc import ABC, abstractmethod


class Algoritm(ABC):
    @abstractmethod
    def find_duplicates(self):
        pass

    def similarity(self, a, b):
        """Вычисляет схожесть двух строк."""
        return SequenceMatcher(None, a, b).ratio()

class One_key_similarity(Algoritm):
    def __init__(self) -> None:
        super().__init__()

    def find_duplicates(self, data, key, threshold=0.8):
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
                if self.similarity(data_sorted[i][key], data_sorted[j][key]) >= threshold:
                    group.append(data_sorted[j])
                    visited[j] = True
            if len(group) > 1:
                duplicates.append({"Duplicate": group})

        return duplicates

class All_keys_average_similarity(Algoritm):
    def __init__(self) -> None:
        super().__init__()

    def average_similarity(self, item1, item2, keys):
        """Вычисляет среднюю схожесть по всем ключам."""
        total_similarity = 0.0
        for key in keys:
            total_similarity += self.similarity(str(item1[key]), str(item2[key]))
        return total_similarity / len(keys)

    def find_duplicates(self, data, threshold=0.8):
        """Находит дубликаты в данных на основе средней схожести всех ключей."""
        keys = data[0].keys()
        duplicates = []
        visited = [False] * len(data)

        for i in range(len(data) - 1):
            if visited[i]:
                continue
            group = [data[i]]
            for j in range(i + 1, len(data)):
                if self.average_similarity(data[i], data[j], keys) >= threshold:
                    group.append(data[j])
                    visited[j] = True
            if len(group) > 1:
                duplicates.append({"Duplicate": group})

        return duplicates

class All_keys_90_similarity(Algoritm):
    def __init__(self) -> None:
        super().__init__()

    def is_duplicate(self, item1, item2, keys, threshold=0.9):
        """Проверяет, являются ли два элемента дубликатами на основе схожести всех ключей."""
        for key in keys:
            if self.similarity(str(item1[key]), str(item2[key])) < threshold:
                return False
        return True

    def find_duplicates(self, data, threshold=0.9):
        """Находит дубликаты в данных на основе схожести всех ключей."""
        keys = data[0].keys()
        duplicates = []
        visited = [False] * len(data)

        for i in range(len(data) - 1):
            if visited[i]:
                continue
            group = [data[i]]
            for j in range(i + 1, len(data)):
                if self.is_duplicate(data[i], data[j], keys, threshold):
                    group.append(data[j])
                    visited[j] = True
            if len(group) > 1:
                duplicates.append({"Duplicate": group})

        return duplicates


class AlgoritmFactory:
    @staticmethod
    def create_algoritm(algorim_type, *args, **kwargs):
        if algorim_type == 'one_key_similarity':
            return One_key_similarity(*args, **kwargs)
        elif algorim_type == 'all_keys_average_similarity':
            return All_keys_average_similarity(*args, **kwargs)
        elif algorim_type == 'all_keys_90%_similarity':
            return All_keys_90_similarity(*args, **kwargs)
        else:
            raise ValueError(f"Unknown algoritm type: {algorim_type}")

def main():
    duplicates = []

    # Шаг 1: Создаем объекты алгоритмов с помощью фабрики
    one_key_similarity = AlgoritmFactory.create_algoritm('one_key_similarity')
    all_keys_average_similarity = AlgoritmFactory.create_algoritm('all_keys_average_similarity')
    all_keys_90_similarity = AlgoritmFactory.create_algoritm('all_keys_90%_similarity')

    # Шаг 2: Загрузка данных из JS
    with open('tv_data.js', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)

    # Шаг 3: Поиск дубликатов
    duplicates.append(
        [one_key_similarity.find_duplicates(data, key='Название', threshold=0.8),
         'duplicates_data_one_key_similarity.js']
    )
    duplicates.append(
        [all_keys_average_similarity.find_duplicates(data),
         'duplicates_data_all_keys_average_similarity.js']
    )
    duplicates.append(
        [all_keys_90_similarity.find_duplicates(data, threshold=0.9),
         'duplicates_data_all_keys_90_similarity.js']
    )

    # Шаг 4: Сохранение найденных дубликатов в формате JSON
    for duplicate in duplicates:
        save_data_to_json(duplicate[0], duplicate[1], dupl=True)

if __name__ == "__main__":
    main()

