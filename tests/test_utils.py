from utils import filter_sort_spisok, load_data, format_date, mask_card, formatted_data


def test_load_data():
    list_ =[
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
            ]
    assert load_data('test.json') == list_

def test_filter_sort_spisok():
    list_ = [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2019-07-03T18:35:29.512364'
        },
        {
            'id': 2,
            'state': 'OPEN',
            'date': '2018-07-03T18:35:29.512364'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-07-03T18:35:29.512364'
        }
    ]
    sorted_list = [
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2020-07-03T18:35:29.512364'
        },
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2019-07-03T18:35:29.512364'
        }
    ]
    assert filter_sort_spisok(list_) == sorted_list


def test_format_date():
    assert format_date('2019-07-03T18:35:29.512364') == '03.07.2019'
    assert format_date('2018-03-23T10:45:06.972075') == '23.03.2018'


def test_mask_card():
    assert mask_card('Счет 75106830613657916952') == 'Счет **6952'
    assert mask_card('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'
    assert mask_card('Maestro 4598300720424501') == 'Maestro 4598 30** **** 4501'


def test_formatted_data():
    dict1 = {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
    dict2 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 35383033474447895560"
    }
    str1 = '03.07.2019 Перевод организации\n' \
            'MasterCard 7158 30** **** 6758 -> Счет **5560\n' \
            '8221.37 USD\n'
    str2 = '03.07.2019 Перевод организации\n' \
           'Счет **5560\n' \
           '8221.37 USD\n'
    assert formatted_data(dict1) == str1
    assert formatted_data(dict2) == str2
