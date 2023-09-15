#libraries
import time
import sys

capacitorcode = {
        'NONE': 20,
        'A': 0.05,
        'B': 0.1,
        'C': 0.25,
        'D': 0.5,  
        'F': 1,
        'G': 2,
        'J': 5,
        'K': 10,
        'M': 20,
        'N': 30,
    }



capacitorcodeletters = ["NONE", "A", "B", "C", "D", "F", "G", "J", "K", "M", "N", "Q", "S", "T", "Z"]
capactorcodetolerance = 20, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 30 #Didnt continue on because Q S T and Z are special and have specific minuses and pluses, Imma prob just use a dictionary


options = ["Exit", "IVR triangle", "Notation prefix conversions", "Resistance calculations", "Resistor Color Code", "Capacitor Code", "Find Min/Max Tolerance based on number"]
notationoptions = ["Back", "Find notation conversion units", "# of exponent change from unit to unit", "compact number into notation", "Compact number into units"]
triangle = ["Back", "Find Current (i)", "Find voltage (v)","Find Resistance (r)"]

ohm_symbol = "Ω" #variable for ohm symbol

v = 0
i = 0
r = 0

engineeringnotationconvert1 = 0

loadingdelay = 1

"""
SPECIAL CHARACTER ARCHIVE:

Ω - Ohms/Omega
μ - Micro

"""

#IVR triangle (I = Current, V = Voltage, R = Resistance) functions

def i_vr(v,r):    #I = V/R
    return v/r

def v_ir(i,r): # V = I*R
    return i*r 

def r_vi(v,i):   #R = V/I
    return v/i


#resistence calculator
def pResistence(args):     #args must contain only ints
    rt = 0
    for i in args:
        rt += 1/i
    return 1/rt


def sResistence(args):      #args must contain only ints
    rt = 0
    for i in args:
        rt += i
    return rt


def convert(self, symbol1, num1, symbol2):
    pass


def engineering_notation(number):
    # Handle zero
    if number == 0:
        return "0"

    # Determine the exponent of the number
    exponent = 0
    while abs(number) < 1 or abs(number) >= 1000:
        if abs(number) < 1:
            number *= 1000
            exponent -= 3
        else:
            number /= 1000
            exponent += 3

    # Convert to a string in engineering notation
    return "{:.2f} x 10^{}".format(number, exponent)


def compact_engineering_notation(value):
    prefixes = {
        'pico': 1e-12,
        'nano': 1e-9,
        'micro': 1e-6,
        'milli': 1e-3,
        'regular': 1e0,  # Base unit
        'kilo': 1e3,
        'mega': 1e6,
        'giga': 1e9,
        'tera': 1e12
    }

    for prefix, multiplier in prefixes.items():
        if abs(value) >= multiplier:
            compact_value = value / multiplier
            if abs(compact_value) < 1000:
                return "{:.3g} {}".format(compact_value, prefix)
    return "{:.3g}".format(value)


def convert_prefix(value, from_prefix, to_prefix):
    prefixes = {
        'pico': 1e-12,
        'nano': 1e-9,
        'micro': 1e-6,
        'milli': 1e-3,
        'regular' : 1e0,
        'kilo': 1e3,
        'mega': 1e6,
        'giga': 1e9,
        'tera': 1e12
    }

    # Check if the provided prefixes are valid
    if from_prefix not in prefixes or to_prefix not in prefixes:
        return "Invalid prefixes"

    # Perform the conversion
    converted_value = value * (prefixes[from_prefix] / prefixes[to_prefix])
    return converted_value


def calculate_resistor_value(first_color, second_color, third_color, fourth_color=None):
    color_codes = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'gray': 8,
        'white': 9
    }

    multiplier_values = {
        'black': 1,
        'brown': 10,
        'red': 100,
        'orange': 1000,
        'yellow': 10000,
        'green': 100000,
        'blue': 1000000,
        'violet': 10000000
    }

    tolerance_values = {
        'gold': '+/- 5%',
        'silver': '+/- 10%',
        'none': '+/- 20%'
    }


    try:
        digit1 = color_codes[first_color]
        digit2 = color_codes[second_color]
        multiplier = multiplier_values[third_color]

        resistance = (digit1 * 10 + digit2) * multiplier

        if fourth_color != "":
            tolerance = tolerance_values.get(fourth_color, 'Invalid tolerance color')
            result = "Resistance value: {} {} ohms, Tolerance: {}".format(resistance, ohm_symbol, tolerance)
        else:
            result = "Resistance value: {} {} ohms".format(resistance, ohm_symbol)

        return result

    except KeyError:
        return "Invalid color code"

def tolerance_calc(tolerating_number, sub_tolerance_percent, add_tolerance_percent):
    
    tolerating_number = float(tolerating_number)

    sub_tolerance = float(sub_tolerance_percent) * float(tolerating_number)
    sub_tolerance = sub_tolerance / 100

    add_tolerance = float(add_tolerance_percent) * float(tolerating_number)
    add_tolerance = add_tolerance / 100

    min_tolerance = tolerating_number - sub_tolerance
    max_tolerance = tolerating_number + add_tolerance

    tolerate_result = "Min Acc Value: {}\nMax Acc Value: {}".format(min_tolerance, max_tolerance)
    return tolerate_result

#See how much notation between each
#Ex. kilo to regular 10^3
#logarithm - How much an exponent goes up between 2 numbers
#Ex. 10 -> 1000 = 3


#Give symbol / name if multiply number by 10^? 
#Ex. kilo to mega if 10^3
#Ex. kilo to milli if 10^-6
















#main loop
while True:
    time.sleep(loadingdelay)
    print("\n\nWelcome to the 'STEM Sophomore Calculator Directory 🤓'")
    print("\n[ - Credits: Andrew K and Dawson B - ]\n")

    for index, obj in enumerate(options):
        print('[{}] {}'.format(index+1,obj))

    action = (input("\nWhat would you like to do?\n"))

    try:
        action = int(action)
    except:
        print("Cannot convert")
        continue

    if 0 < action <= len(options):
        pass
    else:
        print("That was not a choice\n")
        continue
    
    if action == 1:
        print("Exiting program...")
        sys.exit()

    if action == 2:
        while True:
            time.sleep(loadingdelay)
            print("\n[ - IVR TRIANGLE - ]\n\n")

            for index, obj in enumerate(triangle):
                print('[{}] {}'.format(index+1,obj))

            print("\nWhat would you like to do?\n")
            
            ivr_find = input()
            ivr_find = ivr_find.lower()

            if ivr_find in ["back", "1"]:
                break

            if ivr_find in ["i", "v", "r", "2", "3","4"]:

                print("Be sure that your objects are in the same SI unit (Ex: 3 kV = 3000V)")
                print("(Use the tranformation device for this)\n")
                try:
                    #ivr find what you are calculating
                    if ivr_find in  ["i","2"]:

                        v = float(input("What is the Voltage: "))
                        r = float(input("What is the Resistance: "))
                        print()
                        print("****Current is {} A****\n".format(i_vr(v,r)))
                            
                    if ivr_find in ["v", "3"]:
                        i = float(input("What is the current: "))
                        r = float(input("What is the Resistance: "))
                        print()
    
                        print("****Voltage is {} V****\n".format(v_ir(i,r)))


            
                    if ivr_find in ["r","4"]:
                        i = float(input("What is the current: "))
                        v = float(input("What is the Voltage: "))
    
                        print()
                        print("****Resistance is {} Ω****\n".format(r_vi(v,i)))
                        print("Be sure that this numbers is in the right SI unit\n")
                        
                    time.sleep(loadingdelay)
                except ValueError:
                    print("That wasn't valid. Try again")
                        
            else:
                print("type the letter i, v, r, or the number")

    if action == 3:
        while True:
            print("\n[ - NOTATION PREFIX CONVERSIONS - ]\n\n")
            for index, obj in enumerate(notationoptions):
                print('[{}] {}'.format(index+1,obj))
            notationchoice = input("\nWhat will you choose?\n")
            try:
                notationchoice = int(notationchoice)
            except:
                print("Cannot convert")
                continue

            if notationchoice == 1:
                break

            #notation conversion
            if notationchoice == 2:
            
                # Ask for user input
                value = float(input("What is your starting number? "))
                from_prefix = input("What is the starting unit (ex. pico, nano, micro, milli, regular, kilo, mega, giga, tera)? ").lower()
                to_prefix = input("What unit do you want to convert to (ex. pico, nano, micro, milli, regular, kilo, mega, giga, tera)? ").lower()

                # Perform the conversion
                result = convert_prefix(value, from_prefix, to_prefix)
                print("\n{} {} ---> {} {}\n".format(value, from_prefix, result, to_prefix))
                print("TIPS: If the number ends in .00 you can just leave the whole number as it is.")
                print("If the number ends in a bunch of zeros and a random num at the end just look for the last number before the trail and that should be the right number. We can't convert decimal places because that might ruin the conversion method.\n\n")
            
            #compaction
            if notationchoice == 4:
                print("What number are you compacting? TYPE FULL NUMBER (Ex. 650000000)")
                engineeringnotationconvert1 = input()
                
                try:
                    engineeringnotationconvert1 = float(engineeringnotationconvert1)
                except:
                    print("Cannot convert")
                    continue
            
                print("\n**** Notation Product is: {} ****\n".format(engineering_notation(engineeringnotationconvert1)))
                print("TIPS: If the number ends in .00 you can just leave the whole number as it is.")
                print("If the number ends in a bunch of zeros and a random num at the end just look for the last 0 and that should be the right number. We can't convert decimal places because that might ruin the conversion method.\n\n")
            if notationchoice == 5:
                # Ask the user for input
                value = float(input("What number do you want to compact? (MUST BE STANDARD UNITS)"))

                # Call the function to compact the number
                result = compact_engineering_notation(value)

                print("\nCompact Engineering Notation: {}".format(result))

    if action == 5:
        while True:
            print("\nTIP: USE VIOLET INSTEAD OF PURPLE FOR THE CODE TO WORK.\n")
            # Input resistor color bands
            first_band = input("Enter the color of the first band: ").lower()
            second_band = input("Enter the color of the second band: ").lower()
            third_band = input("Enter the color of the third band: ").lower()

            # Optional: Input tolerance band
            fourth_band = input("Enter the color of the fourth (tolerance) band (optional): ").lower()

            # Calculate resistance value
            result = calculate_resistor_value(first_band, second_band, third_band, fourth_band)

            print(result)
            break

    if action == 7:
        while True:
        
            print("\nTIP: You do not need to include units on this one because you can just add the prefix (Ex. 18'k'Ω ±5% --> 17.1'k' --> 18.9'k')")
            print("TIP: If your tolerating value is not a seperate number, (Ex. +/- 20%) then use 20 for both subtracting percentage and addition percentage.\n")
            tolerating_number = input("What is your Nominal Value?")
            sub_tolerance_percent = input("What percent is your subtracting tolerance value?")
            add_tolerance_percent = input("What percent is your addition tolerance value?")
            tolerate_result = tolerance_calc(tolerating_number, sub_tolerance_percent, add_tolerance_percent)
            print("\n" + tolerate_result)
            break
