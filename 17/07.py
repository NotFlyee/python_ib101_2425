current_profile = ()

def setup_profile(name: str, vacation_dates: str):
    global current_profile
    current_profile = (name, vacation_dates)

def print_application_for_leave():
    name, period = current_profile
    print(f'Заявление на отпуск в период {period}. {name}')

def print_holiday_money_claim(amount: str):
    name = current_profile[0]
    print(f'Прошу выплатить {amount} отпускных денег. {name}')

def print_attorney_letter(to_whom: str):
    name, period = current_profile
    print(f'На время отпуска в период {period} моим заместителем назначается {to_whom}. {name}')
