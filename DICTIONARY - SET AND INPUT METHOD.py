print("------------------------------------------------------------------------------------------------")
print(" ")
print("ELECTRONIC COMPONENTS DICTIONARY ")
print(" ")
print("------------------------------------------------------------------------------------------------")
print(" ")
print("CHOOSE FROM THE TERMS PRESENTED: ")
print(" ")
print("------------------------------------------------------------------------------------------------")
print(" ")
print('''RESISTOR
CAPACITOR
INDUCTOR
TRANSFORMER
POTENTIOMETER
FUSE
THERMISTOR
VARISTOR
CRYSTAL OSCILLATOR
DIODE
ZENER DIODE
LIGHT EMITTING DIODE
PHOTODIODE
BIPOLAR JUNCTION TRANSISTOR
FIELD EFFECT TRANSISTOR
MOSFET
THYRISTOR
TRIAC
OPTPCOUPLER
OPERATIONAL AMPLIFIER
555 TIMER IC
MICROCONTROLLER
MICROPROCESSOR
ANALOG TO DIGITAL CONVERTER
DIGITAL TO ANALOG CONVERTER
RECTIFIER
VOLTAGE REGULATOR
RELAY
BUZZER
PRINTED CIRCUIT BOARD 
ARDUINO
''')
print(" ")
print("------------------------------------------------------------------------------------------------")

DATA ={
    "RESISTOR":"Limits the flow of electric current in a circuit.",
    "CAPACITOR":" Stores and releases electrical energy in a circuit.",
    "INDUCTOR":"Stores energy in a magnetic field when electrical current flows through it.",
    "TRANSFORMER":" Transfers electrical energy between circuits using electromagnetic induction.",
    "POTENTIOMETER":"A variable resistor used to adjust voltage or current.",
    "FUSE":" A safety device that breaks the circuit when excessive current flows.",
    "THERMISTOR":" A resistor whose resistance changes with temperature.",
    "VARISTOR":"(VDR) A resistor that changes resistance based on voltage, protecting against voltage spikes.",
    "CRYSTAL OSCILLATOR":"Generates precise clock signals for circuits.",
    "DIODE":" Allows current to flow in only one direction.",
    "ZENER DIODE":"Allows current to flow in reverse when a specific voltage is reached, used for voltage regulation.",
    "LIGHT EMITTING DIODE":"(LED) Emits light when current passes through it.",
    "PHOTODIODE":"Converts light into electrical current.",
    "BIPOLAR JUNCTION TRANSISTOR":"(BJT) A transistor that amplifies or switches electrical signals.",
    "FIELD EFFECT TRANSISTOR":"(FET) Controls current flow using an electric field.",
    "MOSFET":"A type of FET widely used in digital circuits and power electronics.",
    "THYRISTOR":"(SCR) A semiconductor switch that conducts once triggered.",
    "TRIAC":"A semiconductor switch that controls AC power.",
    "OPTOCOUPLER":"Uses light to transfer electrical signals between circuits, providing isolation.",
    "OPERATIONAL AMPLIFIER":"(OP-AMP) A high-gain voltage amplifier used in signal processing.",
    "555 TIMER IC":"A versatile IC used for timing, oscillation, and pulse generation.",
    "MICROCONTROLLER":"A small computer on a chip used in embedded systems.",
    "MICROPROCESSOR":"The central processing unit (CPU) of a computer.",
    "ANALOG TO DIGITAL CONVERTER":"(ADC) Converts analog signals to digital.",
    "DIGITAL TO ANALOG CONVERTER":"(DAC) Converts digital signals to analog.",
    "RECTIFIER":"(BRIDGE RECTIFIER) Converts AC to DC using diodes.",
    "VOLTAGE REGULATOR":"Maintains a stable output voltage despite input or load changes.",
    "RELAY":" An electromechanical switch controlled by an electrical signal.",
    "BUZZER":" Produces sound using electrical signals.",
    "PRINTED CIRCUIT BOARD":"(PCB) A board that holds and connects electronic components in a circuit.",
    "ARDUINO":"Company that makes microcontrollers"
}
#

a = input("term: ")
print("-")
print(DATA[a])

#
print("-")
b = input("Add a new term in the dictionary:")
DATA[b] = b
print("-")
print("The new term,", [b], "is now added")

#
print("-")
c = input("Definition of the recently added term:")
DATA[b] = c
print("-")
print("The definition of the recently added term", [b], "is now added")

#

print("Here is the updated list of terms ")
print("-")
print('''RESISTOR
CAPACITOR
INDUCTOR
TRANSFORMER
POTENTIOMETER
FUSE
THERMISTOR
VARISTOR
CRYSTAL OSCILLATOR
DIODE
ZENER DIODE
LIGHT EMITTING DIODE
PHOTODIODE
BIPOLAR JUNCTION TRANSISTOR
FIELD EFFECT TRANSISTOR
MOSFET
THYRISTOR
TRIAC
OPTPCOUPLER
OPERATIONAL AMPLIFIER
555 TIMER IC
MICROCONTROLLER
MICROPROCESSOR
ANALOG TO DIGITAL CONVERTER
DIGITAL TO ANALOG CONVERTER
RECTIFIER
VOLTAGE REGULATOR
RELAY
BUZZER
PRINTED CIRCUIT BOARD 
ARDUINO
''',[b])

#

d = input("term:")
print("-")
print(DATA[d])

#
print(" ")
e = input("Remove a term: ")
del DATA[e]
print("the term",[e],"is now removed")

print("Here is the updated list of terms ")

print("-")

print('''RESISTOR
CAPACITOR
INDUCTOR
TRANSFORMER
POTENTIOMETER
FUSE
THERMISTOR
VARISTOR
CRYSTAL OSCILLATOR
DIODE
ZENER DIODE
LIGHT EMITTING DIODE
PHOTODIODE
BIPOLAR JUNCTION TRANSISTOR
FIELD EFFECT TRANSISTOR
MOSFET
THYRISTOR
TRIAC
OPTPCOUPLER
OPERATIONAL AMPLIFIER
555 TIMER IC
MICROCONTROLLER
MICROPROCESSOR
ANALOG TO DIGITAL CONVERTER
DIGITAL TO ANALOG CONVERTER
RECTIFIER
VOLTAGE REGULATOR
RELAY
BUZZER
PRINTED CIRCUIT BOARD
ARDUINO''')

#
f = input("Term:")
print("-")
print(DATA[f])
