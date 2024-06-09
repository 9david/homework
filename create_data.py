import csv
import json

def load_data_from_csv(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def save_data_to_json(data, filename, duplicate=False):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        if not duplicate:
            print('Данные из csv формата сохранены в формат json')
        else:
            print('Созданы продублированные данные')


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
    csv_columns = ["Название", "Тип панели", "Диагональ (дюйм)", "Разрешение", "Поддержка hdr", "Частота (гц)", "Операционная система"]
    csv_file = "tv_data.csv"
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in tv_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

    print(f"Созданы данные в файле {csv_file}")


    # Выгрузка данных из CSV в python обьект
    data = load_data_from_csv('tv_data.csv')

    # Сохранение данных в формате JSON
    save_data_to_json(data, 'tv_data.js')