def print_menu():
    print('1. Length\t\t2. Temperature\t\t3. Area')
    print('4.Volume\t\t5. Weight\t\6. Time\n')

def length_print_menu():
    print('\nConvert from: \n')
    print('1. Meters\t\2. Kilometers\t\3. Centimeters')
    print('4. Millimeters\t\t5. Micrometers\t\t6. Nanometers')
    print('7. Miles\t\t8. Yards\t\t9. Feet')
    print('10. Inches\t\t11. Light Years\n')

def meter_menu():
    print('\nConvert from meters to: \n')
    print('1. Kilometers\t\t2. Centimeters\t\t3. Millimeters')
    print('4. Micrometers\t\t5. Nanometers\t\t6. Miles')
    print('7. Yards\t\t8. Feet\t\t9. Inches')
    print('10. Light Years\n')

def meters_to_kilometers():
    while True:
        try:
            m = float(input('Enter the length to meters: '))
            km = m / 1000
            print('\n{0} meters - {1} kilometers.'.format(m,km))
            break
        except ValueError:
            print('Invalid input\n')
            continue

def main():
    while True:
        print_menu()
        choice = input('Which calculation do you want to make? ')
        if choice == '1':
            length_print_menu()
            choice = input('Pick one of the options. ')
            if choice == '1':
                meter_conversion_print_menu()
                choice = input('Pick one of the options. ')
                if choice == '1':
                    meters_to_kilometers()
                else:
                    print('Invalid input')
            else:
                    print('Invalid input')
        else:
                    print('Invalid input')
        print()
        answer = input('Do you want to exit the program? (y) for yes ')
        if answer = 'y':
            break
 main()