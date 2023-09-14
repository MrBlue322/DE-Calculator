#libraries
import time
import sys

#define variables and lists
options = ["Exit", "IVR triangle", "Notation prefix conversions", "Resistance calculations"]
notationoptions = ["Back, ""Find notation conversion units", "# of exponent change from unit to unit"]
triangle = ["Back", "Find Current (i)", "Find voltage (v)","Find Resistance (r)"]
v = 0
i = 0
r = 0

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

#See how much notation between each
#Ex. kilo to regular 10^3
#logarithm - How much an exponent goes up between 2 numbers
#Ex. 10 -> 1000 = 3


#Give symbol if multiply number by 10^? 
#Ex. kilo to mega if 10^3
#Ex. kilo to milli if 10^-6



#main loop
while True:
    print("\n\nWelcome to the 'STEM Sophomore Directory 🤓'")
    print("\n[ - Credits: Andrew K and Dawson B - ]\n")

    for index, obj in enumerate(options):
        print('[{}] {}'.format(index+1,obj))

    action = (input("\nWhat would you like to do?\n"))

    try:
        action = int(action)
    except:
        print("Cannot convert")
        continue

    if 0 < action < len(options):
        pass
    else:
        print("That was not a choice\n")
        continue
    
    if action == 1:
        print("Exiting program...")
        sys.exit()

    if action == 2:
        while True:
            print("\n[ - IVR TRIANGLE - ]\n\n")

            for index, obj in enumerate(triangle):
                print('[{}] {}'.format(index+1,obj))

            print("\nWhat would you like to do?\n")
            
            ivr_find = input()
            ivr_find = ivr_find.lower()

            if ivr_find == "back" or "1":
                break

            if ivr_find == "i" or "v" or "r" or "2" or "3" or "4":
                    

                print("Be sure that your objects are in the same SI unit(Ex: 3 kV = 3000V)")
                print("(Use the tranformation device for this)\n")
                try:
                    #ivr find what you are calculating
                    if ivr_find == "i":

                        v = int(input("What is the Voltage: "))
                        r = int(input("What is the Restence: "))
                        print()
                        print("Answer is {}\n".format(i_vr(v,r)))
                            
                    if ivr_find == "v":
                        i = int(input("What is the current: "))
                        r = int(input("What is the Restence: "))
                        print()
    
                        print("Answer is {}\n".format(v_ir(i,r)))


    
                    if ivr_find == "r":
                        i = int(input("What is the current: "))
                        v = int(input("What is the Voltage: "))
    
                        print()
                        print("Answer is {}\n".format(r_vi(i,v)))
                        print("Be sure that these mumbers are the right SI unit\n")
                except ValueError:
                    print("That wasn't a number. Try again")
                        
            else:
                print("type the letter i, v, r, or the number")
    else:
        print("type the letter i, v, r, or the number")
        continue
    

    if action == 3:
        while True:
            print("\n[ - NOTATION PREFIX CONVERSIONS - ]\n\n")
            for index, obj in enumerate(notationoptions):
                print('[{}] {}'.format(index+1,obj))
            notationchoice = input("\nWhat will you choose?\n")
            try:
                action = int(action)
            except:
                print("Cannot convert")
                continue

            if notationchoice == 1:
            
                convert1 = input("What number will you be converting first?")
            try:
                convert1 = int(convert1)
            except:
                print("unable to convert to int.")
                sys.exit()
            prefixnum1 = input("what unit ")
