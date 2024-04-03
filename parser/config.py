connection_string = "postgresql://postgres:admin@localhost:5433/yandexMaps"
time_sleep_gap_for_reviews_increase = 1.2
default_org_id = 1124715036

org_url_template = "https://yandex.ru/maps/org/_/reviews"
station_url_template = "https://yandex.ru/maps/213/moscow/stops/_?tab=reviews"

# 'id': ['Title', 'Link type'] - in the link id instead of including
target_objects = {
    '1062848432': ['Курский вокзал', 'org'],
    '1095876672': ['Киевский вокзал', 'org'],
    'station__lh_2000005': ['Павелецкий вокзал', 'station'],
    '2057340510': ['Белорусский вокзал', 'station'],
    '1079518466': ['Казанский вокзал', 'org'],
    '1039320330': ['Рижский вокзал', 'org'],
    'station__lh_2000009': ['Савёловский вокзал', 'station'],
    '84701147661': ['Восточный вокзал', 'org']
}
