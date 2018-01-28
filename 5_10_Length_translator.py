units = {"mile": 1609,
         "yard": 0.9144,
         "foot": 0.3048,
         "inch": 0.0254,
         "km": 1000,
         "cm": 0.01,
         "mm": 0.001,
         "m": 1}

instruction = input()  #<number> <unit_from> in <unit_to>

def convert(number, unit_from, unit_to):
    return number * units[unit_from] / units[unit_to]

n = float(instruction.split()[0])
f = instruction.split()[1]
t = instruction.split()[3]

print("%.2e" % convert(n, f, t))
