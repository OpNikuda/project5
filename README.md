# Home Work

## Цель проекта

Цель данного проекта - разработка модуля Python, содержащего функцию для сортировки списка словарей по значению ключа 'date'. Функция должна корректно обрабатывать даты, преобразовывать их в формат, пригодный для сравнения и сортировки, и предоставлять возможность сортировки как по возрастанию, так и по убыванию.

## Установка

Для использования разработанного модуля не требуется установка дополнительных пакетов, так как он использует только стандартные библиотеки Python (datetime).

## Использование

### 1. Импорт модуля

Скопируйте код в файл Python (например, `date_utils.py`).  Затем импортируйте функцию `sort_by_date` из этого файла:

```python
from date_utils import sort_by_date
```


### Примеры использования:

```python
data = [
    {'title': 'A', 'date': '10-02-2024'},
    {'title': 'B', 'date': '01-02-2024'},
    {'title': 'C', 'date': '15-02-2024'}
]
sorted_data = sort_by_date_custom_format(data, date_format='%d-%m-%Y')
print(sorted_data)
```

## Тестирование

В проекте используются тесты для проверки корректности работы кода и документации. Для запуска тестов необходимо установить зависимости и выполнить команду `pytest`.

## Лицензия

Этот проект распространяется под лицензией [MIT](https://opensource.org/licenses/MIT). Смотрите файл [LICENSE](LICENSE) для получения подробностей.
