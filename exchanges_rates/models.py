from datetime import datetime


class Rates:
    """
    Хранение списка курсов и даты их последнего обновления
    """
    last_set: str = None
    rates = {}
    is_set = False

    def set(self, rates: dict):
        """
        Сохранение курсов и времени обновления

        :param rates: словарь курсов в формате
            {...
            'rates': {
                'RATE1': 36.65,
                'RATE2': 41.15
                }
            }
        :return: None
        """
        self.last_set = datetime.now().isoformat()
        self.rates = rates['rates']

    def get_all(self) -> dict:
        """
        Курсы всех валют

        :return: словарь со всеми курсами
        """
        return self.rates

    def get(self, name: str) -> float or None:
        """
        Курс валюты по её имени

        :param name: имя требуемой валюты
        :return: курс или None, если такой валюты нет
        """
        if name.upper() in self.rates.keys():
            return self.rates[name.upper()]
        return None
