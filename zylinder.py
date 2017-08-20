# zylinder.py
from math import pi

# Input
input_diameter = input('diameter in meter: ')
input_height = input('height in meter: ')

# Processing
# Hint: input()-function provides strings, casts are necessary
d = float(input_diameter)
h = float(input_height)
volume = pi * (d/2)**2 * h

# Output
print('\n')
print('The zylinder has a volume of (cubic meter): ',
      round(volume, 2))
