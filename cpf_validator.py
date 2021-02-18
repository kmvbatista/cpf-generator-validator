import re
from digit_validator import Digit_validator


class Cpf_validator:
    def __init__(self, cpf):
        self.cpf = cpf
        self.digit_validator = Digit_validator()

    def is_cpf_valid(self):
        if self.__is_cpf_format():
            self.cpf = self.cpf.replace('.', '').replace('-', '')
        return not self.__are_digits_the_same() and self.__are_validation_digits_correct()

    def __is_cpf_format(self):
        pattern = r"^(\d{3}.){2}\d{3}-\d{2}$"
        return bool(re.match(pattern, self.cpf))

    def __are_digits_the_same(self):
        return all([number == self.cpf[0] for number in self.cpf])

    def __are_validation_digits_correct(self):
        first_validation_digit = self.digit_validator.get_validation_digit(
            self.cpf)
        if first_validation_digit != int(self.cpf[-2]):
            return False
        return self.digit_validator.get_validation_digit(self.cpf, get_second_digit=True) == int(self.cpf[-1])
