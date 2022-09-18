#Абстрактная фабрика реализовать фабрику по созданию студенческой весны факультета ПММ и математического
from abc import ABC, abstractmethod

class RegionalProgram(ABC):
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        ...

class Vocal(ABC):
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        ...

class Dance(ABC):
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        ...

class PMMRegionalProgram(RegionalProgram):
    def __init__(self):
        super().__init__('PMM')

    def create(self):
        print(f'Created RegionalProgram for {self._system}')

class PMMVocal(Vocal):
    def __init__(self):
        super().__init__('PMM')

    def create(self):
        print(f'Created Vocal for {self._system}')

class PMMDance(Dance):
    def __init__(self):
        super().__init__('PMM')

    def create(self):
        print(f'Created Dance for {self._system}')


class FacultyOfMathematicsRegionalProgram(RegionalProgram):
    def __init__(self):
        super().__init__('Faculty of Mathematics')

    def create(self):
        print(f'Created RegionalProgram for {self._system}')


class FacultyOfMathematicsVocal(Vocal):
    def __init__(self):
        super().__init__('Faculty of Mathematics')

    def create(self):
        print(f'Created Vocal for {self._system}')


class FacultyOfMathematicsDance(Dance):
    def __init__(self):
        super().__init__('Faculty of Mathematics')

    def create(self):
        print(f'Created Dance for {self._system}')

class AbstractFacrtory(ABC):
    @abstractmethod
    def getRegionalProgram(self) -> RegionalProgram:
        pass
    def getVocal(self) -> Vocal:
        pass
    def getDance(self) -> RegionalProgram:
        pass

class PMMFactory(AbstractFacrtory):
    def getRegionalProgram(self) -> RegionalProgram:
        return PMMRegionalProgram()
    def getVocal(self) -> Vocal:
        return PMMVocal()
    def getDance(self) -> Dance:
        return PMMDance()

class FacultyOfMathematicsFactory(AbstractFacrtory):
    def getRegionalProgram(self) -> RegionalProgram:
        return FacultyOfMathematicsRegionalProgram()
    def getVocal(self) -> Vocal:
        return FacultyOfMathematicsVocal()
    def getDance(self) -> Dance:
        return FacultyOfMathematicsDance()

class Application:
    def __init__(self, factory: AbstractFacrtory):
        self._factory = factory

    def create(self):
        regionalprogram = self._factory.getRegionalProgram()
        vocal = self._factory.getVocal()
        dance = self._factory.getDance()
        regionalprogram.create()
        vocal.create()
        dance.create()

def create_factory(system_name: str) -> AbstractFacrtory:
    factory_dict = {
        "PMM": PMMFactory,
        "FacultyOfMathematics": FacultyOfMathematicsFactory
    }
    return factory_dict[system_name]()

if __name__ == "__main__":
    #system_name = "FacultyOfMathematics"
    #u1 = create_factory(system_name)
    #app = Application(u1)
    #app.create()
    Application(create_factory("PMM")).create()