from cpf_validator import Cpf_validator
from cpf_generator import Cpf_generator

def validate_cpf():
    cpf = input('digite seu cpf com pontos\n')
    cpf_validator = Cpf_validator(cpf)
    if cpf_validator.is_cpf_valid():
        message_user('esse cpf está válido')
    else:
        message_user('esse cpf está inválido')

def generate_cpf():
    generator = Cpf_generator()
    generated_cpf = generator.generate()
    message_user(f'cpf gerado: {generated_cpf}')

def message_user(message):
    print(f'{message}\n')

def init():
    choice = -1
    while choice != 0:
        choice = input('escolha 1 - validar cpf ou 2 - gerar ou 0 -sair \n')
        if choice == '1':
            validate_cpf()
        elif choice =='2':
            generate_cpf()
        else:
            message_user('escolha uma opção válida')

init()