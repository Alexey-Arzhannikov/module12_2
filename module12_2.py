class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers



    # def start(self):
    #     """
    #     Исправлена ошибка, по которой  бегун с меньшей скоростью
    #     мог пробежать некоторые дистанции быстрее, чем бегун с большей
    #     """
    #     finishers = {}
    #     while self.participants:
    #         for participiant in self.participants:
    #             participiant.run()
    #             finishers[participiant.distance] = participiant
    #             self.participants.remove(participiant)
    #     results_table = dict(sorted(finishers.items(), reverse=True))
    #     return results_table

