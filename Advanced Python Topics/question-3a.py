
from enum import Enum

THE_CODE = 'password'


class AlphaNumericInput:
    @staticmethod
    def validate_input(str):
        if not str.isalnum():
            raise ValueError

    @classmethod
    def get_input(cls):
        input_str = input("Please enter code:")
        cls.validate_input(input_str)
        return input_str


class NumericInput:
    @staticmethod
    def validate_input(str):
        if not str.isdigit():
            raise ValueError

    @classmethod
    def get_input(cls):
        input_str = input("Please enter code:")
        cls.validate_input(input_str)
        return input_str


class CarLock:
    class State(Enum):
        LOCKED = "locked"
        BLOCKED = "blocked"
        UNLOCKED = "unlocked"

    def __init__(self,input_device, code, lockout_tries = 3,):
        self._state = CarLock.State.LOCKED
        self._code = code;
        self._lockout_tries = lockout_tries
        self._input_device = input_device

    def unlock(self):
        if self._state == CarLock.State.BLOCKED:
            return False
        for count in range(0,self._lockout_tries):
            input_str = self._input_device.get_input()
            if input_str == self._code:
                self._state = CarLock.State.UNLOCKED
                return True
        # if correct code was not entered...
        self._state = CarLock.State.BLOCKED
        return False


cl = CarLock(AlphaNumericInput,'test211',4)
print(cl.unlock())
print(cl.unlock())
cl = CarLock(NumericInput,'1234')
print(cl.unlock())
print(cl.unlock())