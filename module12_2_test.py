import module12_2 as trnt
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner_1 = trnt.Runner('Усейн', 10)
        self.runner_2 = trnt.Runner('Андрей', 9)
        self.runner_3 = trnt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):

        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            key_position = 1
            for key, value in test_value.items():
                print(f'\t{key_position}: {value.name}')
                key_position += 1

    def test_turn1(self):
        turn_1 = trnt.Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат 1-го соревнования'] = result

    def test_turn2(self):
        turn_2 = trnt.Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат 2-го соревнования'] = result

    def test_turn3(self):
        turn_3 = trnt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат 3-го соревнования'] = result

    def test_turn4(self):
        """
        Дополнительный тест, выявляющий ошибку алгоритма start класса Tournament.
        Удаление объекта из списка participants может
        происходить до того, как будет обработан весь цикл и для каждого объекта будет
        запущен метод participant.run()
        """
        turn_4 = trnt.Tournament(4, self.runner_1, self.runner_2, self.runner_3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник должен быть последним')
        self.all_results['Результат 4-го соревнования'] = result


if __name__ == '__main__':
    unittest.main()