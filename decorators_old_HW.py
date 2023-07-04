from decorators_test_1 import logger

test_list = [['Ira', 'Petya', 'Larisa', 'Boris', 'Rosa'],
            [12, 'forest', 'man'],
            [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
             {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}],
            [{"title":"Web-разработчик с нуля", "duration":19,
			"mentors":["Николай Лопин", "Алексей Кулагин", "Эдгар Нуруллин", "Александр Дудинский"]}],
            [(1, 2, 3),(10,15,20)]]
@logger
def flat_generator(new_list):
    for item in new_list:
        for elem in item:
            yield elem

if __name__ == '__main__':
    for item_1 in flat_generator(test_list):
        print(item_1)
