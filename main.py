import datetime as dt
# Нужно удалить. Модуль которые не используется не является обязательным.
import json

# Отступы. Между импортами и остальным кодом должно быть 2 строки
class Record:
    def __init__(self, amount, comment, date=''):
        # '=' нужно окружить пробелами для читабельности
        # как self.amount = amount или self.comment = comment
        self.amount=amount
        # длина стороки превышеат 80 символов и код в одну линию
        # является мение читабельным
        # так как строка 20 очень грамозкая то лучше сделать указано ниже
        # if date
        #     self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        # else:
        #     dt.datetime.now().date()
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment=comment
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        # Можно типизировать так как тип обьекта нам известен заранее
        # self.records: List[Record] = []
        # и '=' окржить пробелами
        self.records=[]
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        today_stats=0
        # Поменять наименование Record на record для лучшей читаемости по pep8
        for Record in self.records:
            # dt.datetime.now().date() лучше вышести в отдельную переменную
            if Record.date == dt.datetime.now().date():
                # + лучше окрущить пробеломи
                today_stats = today_stats+Record.amount
        return today_stats
    def get_week_stats(self, reNone):
        # окружить пробелами =
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            # Длинная строка. Лучше вывести
            # (today -  record.date).days в
            # отдельную переменную days
            # и сделать в виде 0 <= days < 7
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                week_stats +=record.amount
        return week_stats
class CaloriesCalculator(Calculator):
    # перед коменарием далжно быть 2 пробела
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        x=self.limit-self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        # Лишняя else
        else:
            return 'Хватит есть!'
class CashCalculator(Calculator):
    # Пробелы рядом с '=' и 2 пробела до # и один после
    USD_RATE=float(60) #Курс доллар США.
    EURO_RATE=float(70) #Курс Евро.
    # USD_RATE и EURO_RATE не нудны, так как мы можем получить к ним доступ
    # внутри класса через self. self.USD_RATE
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # Не нужное присваивание
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        # Пробелы. Операторы сравнения лучше окружать пробелами
        if currency=='usd':
            # заменить USD_RATE на self.USD_RATE
            cash_remained /= USD_RATE
            currency_type ='USD'
        elif currency_type=='eur':
            # заменить EURO_RATE на self.EURO_RATE
            cash_remained /= EURO_RATE
            currency_type ='Euro'
        # Не нужная операция. С рублем ничего делать не нужно
        # а currency_type можно написать ранее как рубль
        elif currency_type=='rub':
            cash_remained == 1.00
            currency_type ='руб'
        if cash_remained > 0:
            # строка превышеат 80 строк
            # можно строку разделать и 2 строки
            # Арифметических операций в f-string
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        # elif лучше поменять на else
        elif cash_remained < 0:
            #  строка превышеат 80 строк
            # можно строку разделать и 2 строки
            # Заменить format на f-string ,
            # так как ранее испрользовались f-string
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)

    # Не нужно перегружать метод, если в нем ничего не меняется
    # данная функция лишняя
    def get_week_stats(self):
        super().get_week_stats()


# Общие замечания:
# '=' нужно окружить пробелами для читабельности
# как self.amount = amount или self.comment = comment в строках 10 и 12
#
# - Если атрибут класса используется только внутри класса следует сделать его
# непубличным, т.е. добавить символ подчеркивания перед названием. Пример
# self._amount = amount
#
# - Перед комментариями, оставленными на той же строке, что и код,
# следует оставлять два пробела перед #. Например в 52 строчке следует сделать
# так:
# def get_calories_remained(self):  # Получает остаток калорий на сегодня
#
# - Классы следует разделять двумя пустыми строками
#
# - Между методами внутри класса следует оставлять пустую строку
#
#  Исполняемый код в .py-файлах должен быть закрыт конструкцией if __name__ == ‘__main__’
