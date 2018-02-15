import json
data = {
    "name1": "Alina",
    "surname1": "Berezhnaya",
    "patronymic1": "Alexandrovna",
    "address1": {
        "streetAddress": "Pushkinskaya st., h. 134, f. 45",
        "city": "Rostov-on-Don",
        "postalCode": "344082"
    },
    "contacts1": [
        "8-908-519-67-84",
        "https://vk.com/evildvive"
    ],
    "name2": "Anastsiya",
    "surname2": "Cherdantseva",
    "patronymic2": "Alexandrovna",
    "address2": {
        "streetAddress": "Mechnikova st., h. 79a",
        "city": "Rostov-on-Don",
        "postalCode": "344010"
    },
    "contacts2": [
        "8-918-506-58-80",
        "https://vk.com/id136141535"
    ],
    "name3": "Artur",
    "surname3": "Abuiev",
    "patronymic3": "Zelimkhanovich",
    "address3": {
        "streetAddress": "Mechnikova st., h. 79a",
        "city": "Rostov-on-Don",
        "postalCode": "344010"
    },
    "contacts3": [
        "8-999-634-78-78",
        "https://vk.com/artikabu"
    ],
    "name4": "Andrey",
    "surname4": "Nemoguchev",
    "patronymic4": "Alexieyevich",
    "address4": {
        "streetAddress": "Mechnikova st., h. 79a",
        "city": "Rostov-on-Don",
        "postalCode": "344010"
    },
    "contacts4": [
        "8-906-466-27-19",
        "https://vk.com/andre_andreevich"
    ],
    "name5": "Murzin",
    "surname5": "Alexander",
    "patronymic5": "Vitalievich",
    "address5": {
        "streetAddress": "Mechnikova st., h. 79a",
        "city": "Rostov-on-Don",
        "postalCode": "344010"
    },
    "contacts5": [
        "8-928-673-58-45",
        "https://vk.com/id92938902"
    ],
    "name6": "Nikita",
    "surname6": "Skakun",
    "patronymic6": "Dmitriyevich",
    "address6": {
        "streetAddress": "Mechnikova st., h. 79a",
        "city": "Rostov-on-Don",
        "postalCode": "344010"
    },
    "contacts6": [
        "8-989-534-34-61",
        "https://vk.com/blackyellowhite"
    ],
    "name7": "Valeria",
    "surname7": "Protokovilova",
    "patronymic7": "Andreyevna",
    "address7": {
        "streetAddress": "Sholohova st., h. 76, f.13",
        "city": "Rostov-on-Don",
        "postalCode": "344037"
    },
    "contacts7": [
        "8-918-124-52-79",
        "https://vk.com/id272981383"
    ],
    "name8": "Elizaveta",
    "surname8": "Arkusha",
    "patronymic8": "Yevgeniyevna",
    "address8": {
        "streetAddress": "B.Sadovay st., h. 74, f.37",
        "city": "Rostov-on-Don",
        "postalCode": "344006"
    },
    "contacts8": [
        "8-951-764-32-24",
        "https://vk.com/arkusha_lis"
    ],
    "name9": "Siechkin",
    "surname9": "Alexander",
    "patronymic9": "Alexieyevich",
    "address9": {
        "streetAddress": "Lebedinskaya st., h. 15, f.24",
        "city": "Rostov-on-Don",
        "postalCode": "344023"
    },
    "contacts9": [
        "8-988-552-62-37",
        "https://vk.com/sechkin99"
    ],
    "name10": "Igor",
    "surname10": "Shmidt",
    "patronymic10": "Vladimirovich",
    "address10": {
        "streetAddress": "Smolenskaya st., h. 39",
        "city": "Rostov-on-Don",
        "postalCode": "344000"
    },
    "contacts10": [
        "8-908-192-11-94",
        "https://vk.com/id37309992"
    ],
}
with open('result.json', 'w') as outfile:
    json.dump(data, outfile)