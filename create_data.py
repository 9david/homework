import csv
import json

def save_data_to_csv(tv_data, csv_file):
    '''Сохранение данных в формате CSV'''
    csv_columns = ["Название", "Тип панели", "Диагональ (дюйм)", "Разрешение", "Поддержка hdr", "Частота (гц)", "Операционная система"]
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in tv_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

    print(f"Созданы данные в файле {csv_file}")

def load_data_from_csv(csv_file):
    '''Выгрузка данных из CSV в python обьект в виде списка словарей'''
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def save_data_to_json(data, js_file, duplicate=False):
    '''Сохранение данных в формате JSON'''
    with open(js_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        if not duplicate:
            print(f'Данные из python обьекта сохранены в файле {js_file}')
        else:
            print(f'Созданы и приведены дубликаты данных в файле {js_file}, найдено {len(data)} групп дубликатов.')


# Данные о телевизорах
tv_data = [
    # Дублированные записи
    {"Название": "Samsung Q80T", "Тип панели": "QLED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Tizen"},
    {"Название": "LG CX", "Тип панели": "OLED", "Диагональ (дюйм)": 65, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "webOS"},
    {"Название": "Sony X900H", "Тип панели": "LED", "Диагональ (дюйм)": 75, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Android TV"},
    {"Название": "TCL 6-Series", "Тип панели": "QLED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Roku TV"},
    {"Название": "Vizio P-Series", "Тип панели": "LED", "Диагональ (дюйм)": 65, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "SmartCast"},
    {"Название": "Hisense H9G", "Тип панели": "LED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Android TV"},
    {"Название": "Panasonic HX800", "Тип панели": "LED", "Диагональ (дюйм)": 58, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "My Home Screen"},
    {"Название": "Philips OLED805", "Тип панели": "OLED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Android TV"},
    {"Название": "Sharp Aquos", "Тип панели": "LED", "Диагональ (дюйм)": 70, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "SmartCentral"},
    {"Название": "JVC Fire TV Edition", "Тип панели": "LED", "Диагональ (дюйм)": 50, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Fire OS"},

    # Дублированные записи
    {"Название": "Samsung Q80T", "Тип панели": "QLED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Tizen"},
    {"Название": "LG CX", "Тип панели": "OLED", "Диагональ (дюйм)": 65, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "webOS"},
    {"Название": "Sony X900H", "Тип панели": "LED", "Диагональ (дюйм)": 75, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Android TV"},
    {"Название": "TCL 6-Series", "Тип панели": "QLED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Roku TV"},
    {"Название": "Vizio P-Series", "Тип панели": "LED", "Диагональ (дюйм)": 65, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "SmartCast"},
    {"Название": "Hisense H9G", "Тип панели": "LED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Android TV"},
    {"Название": "Panasonic HX800", "Тип панели": "LED", "Диагональ (дюйм)": 58, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "My Home Screen"},
    {"Название": "Philips OLED805", "Тип панели": "OLED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Android TV"},
    {"Название": "Sharp Aquos", "Тип панели": "LED", "Диагональ (дюйм)": 70, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "SmartCentral"},
    {"Название": "JVC Fire TV Edition", "Тип панели": "LED", "Диагональ (дюйм)": 50, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Fire OS"},

    # Уникальные записи
    {"Название": "Samsung RU7100", "Тип панели": "LED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Tizen"},
    {"Название": "LG NanoCell 85 Series", "Тип панели": "LED", "Диагональ (дюйм)": 65, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "webOS"},
    {"Название": "Sony A8H", "Тип панели": "OLED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 120, "Операционная система": "Android TV"},
    {"Название": "TCL 5-Series", "Тип панели": "QLED", "Диагональ (дюйм)": 50, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Roku TV"},
    {"Название": "Vizio M-Series Quantum", "Тип панели": "LED", "Диагональ (дюйм)": 65, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "SmartCast"},
    {"Название": "Hisense H8G", "Тип панели": "LED", "Диагональ (дюйм)": 55, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Android TV"},
    {"Название": "Panasonic GX800", "Тип панели": "LED", "Диагональ (дюйм)": 58, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "My Home Screen"},
    {"Название": "Philips PUS7304", "Тип панели": "LED", "Диагональ (дюйм)": 50, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Android TV"},
    {"Название": "Sharp LC-50N7000U", "Тип панели": "LED", "Диагональ (дюйм)": 50, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "SmartCentral"},
    {"Название": "JVC LT-43MAW595", "Тип панели": "LED", "Диагональ (дюйм)": 43, "Разрешение": "4K", "Поддержка hdr": True, "Частота (гц)": 60, "Операционная система": "Roku TV"},
]


if __name__ == "__main__":
    # Сохранение данных в формате CSV
    save_data_to_csv(tv_data, "tv_data.csv")

    # Выгрузка данных из CSV в python обьект
    py_data = load_data_from_csv('tv_data.csv')

    # Сохранение данных в формате JSON
    save_data_to_json(py_data, 'tv_data.js')