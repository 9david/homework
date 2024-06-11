import json
from difflib import SequenceMatcher
from mrjob.job import MRJob
from create_data import save_data_to_json


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

class FindDuplicatesJob(MRJob):

    def mapper(self, _, line):
        data = json.loads(line)
        yield data['Название'], data

    def reducer(self, key, values):
        data_list = list(values)
        if len(data_list) > 1:
            yield None, {"Duplicate": data_list}

if __name__ == '__main__':
    # Создание экземпляра MRJob
    job = FindDuplicatesJob()

    # Запуск MRJob
    with job.make_runner() as runner:
        # Чтение входного файла с данными
        with open('tv_data.js', 'r', encoding='utf-8') as jsonfile:
            # Запуск MapReduce задачи
            runner.run()

            # Обработка результатов
            duplicates = []
            for _, output in job.parse_output(runner.cat_output()):
                duplicates.append(output)

    # Сохранение дубликатов в формате JSON
    save_data_to_json(duplicates, 'duplicates_data_mrjob.js', dupl=True)
