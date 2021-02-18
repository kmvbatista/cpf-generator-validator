from random import randint
from digit_validator import Digit_validator

class Cpf_generator:
    def __init__(self):
        self.digit_validator = Digit_validator()

    def generate(self):
        first_nine_digits = self.get_first_nine_digits()
        final_digits = self.get_final_digits(first_nine_digits)
        return self.get_string_from_list(final_digits)

    def get_final_digits(self, first_nine_digits):
        first_validation_digit = self.digit_validator.get_validation_digit(self.get_string_from_list(first_nine_digits))
        cpf_digits = [*first_nine_digits, first_validation_digit]
        second_validation_digit = self.digit_validator.get_validation_digit(self.get_string_from_list(cpf_digits), get_second_digit=True)
        cpf_digits.append(second_validation_digit)
        return self.get_cpf_formatted(cpf_digits)

    def get_first_nine_digits(self):
        numbers = [0,0]
        while numbers[0] == numbers[1]:
            numbers = self.get_random_numbers()
        return numbers    
    
    def get_random_numbers(self):
        numbers = []
        for _ in range(9):
            numbers.append(randint(0,9))
        return numbers

    def get_cpf_formatted(self, digits: list):
        digits.insert(3, '.')
        digits.insert(7, '.')
        digits.insert(-2, '-')
        return self.get_string_from_list(digits)

    def get_string_from_list(self, digits):
        return ''.join(map(str, digits))