# '''Без использования библиотек, создать класс для представления информации о времени. Ваш класс должен иметь
# возможности установки времени и изменения его отдельных полей (час, минута,
# секунда) с проверкой допустимости вводимых значений. В случае недопустимых
# значений полей нужно установить максимально допустимое значение.
# Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def __repr__(self):
        return f"Time : {self.hours}:{self.minutes}:{self.seconds}"

    def __str__(self):
        return f"Time : {self.hours}:{self.minutes}:{self.seconds}"

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, h):
        if 0 <= hours <= 23:
            self._hours = h
        else:
            self._hours = 23

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, m:
        if 0 <= minutes <= 59:
            self._minutes = m
        else:
            self._minutes = 59

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, s):
        if 0 <= seconds <= 59:
            self._seconds = s
        else:
            self._seconds = 59

    def up_hours(self, h):
        self._hours += h
        while self._hours > 23:
            self._hours -= 24

    def up_minutes(self, m):
        self._minutes = self._minutes + m
        while self._minutes > 59:
            self._minutes -= 60
            self._hours += 1
            if self._hours > 23:
                self._hours = 0

    def up_seconds(self, s):
        self._seconds = self._seconds + s
        while self._seconds > 59:
            self._seconds -= 60
            self._minutes += 1
            if self._minutes > 59:
                self._hours += 1
                self._minutes = 0
            if self._hours > 23:
                self._hours = 0


