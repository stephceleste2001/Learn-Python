print("Unit Convertor")
print("==============")

# Choose type of conversion
unit_change = \
    {
        1: "Length",
        2: "Mass",
        3: "Temperature",
        4: "Time",
        5: "Speed",
        6: "Energy",
        7: "Pressure"
    }

# for getting number of type
for keys, values in unit_change.items():
    print("{:2}. {}".format(keys, values))

change = int(input("\nWhich type of conversion you want to do from 1 to 7: "))

# Type 1 (length)
if change == 1:
    print(">>> You chose type Length")
    print("")
    length_dict = \
         {
            1: "Centimeter to Meter",
            2: "Meter to Centimeter",
            3: "Centimeter to Inch",
            4: "Ince to Centimeter",
            5: "Centimeter to Kilometer",
            6: "Kilometer to Centimeter",
            7: "Centimeter to Foot",
            8: "Foot to Centimeter",
            9: "Kilometer to Mile",
            10: "Mile to Kilometer"
         }

# for getting number of conversion
print("=====================")
length_value = float(input("- Enter a number to convert: "))
for keys, values in length_dict.items():
    print("{:2}. {}".format(keys, values))
length_convert = int(input("\nWhich conversion you want to do from 1 to 8: "))

# converting
if length_convert == 1:
    print("{} cm is equal to {} m.".format(length_value, length_value / 100))
elif length_convert == 2:
    print("{} m is equal to {} cm.".format(length_value, length_value * 100))
elif length_convert == 3:
    print("{} is equal to {} inch.".format(length_value, length_value / 2.54))
elif length_convert == 4:
    print("{} inch is equal to {} cm.".format(length_value, length_value * 2.54))
elif length_value == 5:
    print("{} cm is equal to {} km.".format(length_value, length_value / 100000))
elif length_value == 6:
    print("{} km is equal to {} cm.".format(length_value, length_value * 100000))
elif length_value == 7:
    print("{} cm is equal to {} feet".format(length_value, length_value / 30.48))
elif length_convert == 8:
    print("{} fee is equal to {} cm.".format(length_value, length_value * 30.48))
elif length_convert == 9:
    print("{} KM is equal to {} mile.".format(length_value / 1.609))
else:
    print("Sorry, please type correct number from 1 to 10.")

