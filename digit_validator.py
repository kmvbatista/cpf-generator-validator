class Digit_validator:
    def get_validation_digit(self, cpf, get_second_digit = False):
        number_to_divide = 11
        if get_second_digit:
            block_sum = self.__get_block_sum(11, 10, cpf)
        else:
            block_sum = self.__get_block_sum(10, 9, cpf)
        division_rest = block_sum % number_to_divide
        if division_rest in [0,1]:
            return 0
        return number_to_divide - division_rest
    
    def __get_block_sum(self, number_to_get_multiplier, number_to_range, cpf):
        digits_sum = 0
        for cpf_index in range(number_to_range):    
            number_to_multiply = number_to_get_multiplier-cpf_index
            digits_sum += int(cpf[cpf_index])*number_to_multiply
        return digits_sum
