from microbit import *

# Beating heart
for i in range(5):
    display.show(Image.HEART, clear=True)
    
blood_types = ['A', 'B', 'AB', '0']
antibodies = ['anti-B', 'anti-A', '', 'anti-A & anti-B']
antigens = ['A-antigen', 'B-antigen', 'A-antigen & B-antigen', '']

# First output display
i = 0
display.show(blood_types[i])
length = len(blood_types)

# Getting input
while True:
    
    # Scroll antibodies
    if pin1.is_touched():
        if antibodies[i]:
            display.scroll(antibodies[i])
        else:
            display.show(Image.NO)
    
    # Scroll antigens
    elif pin2.is_touched():
        if antigens[i]:
            display.scroll(antigens[i])
        else:
            display.show(Image.NO)
    
    # Show a smiley face because I can
    elif pin0.is_touched():
        display.show(Image.HAPPY)
    
    # Move left
    if button_a.is_pressed():
        i += -1
        if i < 0:
            i = length-1
        display.scroll(blood_types[i])
    
    # Move right
    elif button_b.is_pressed():
        i += 1
        if i == length:
            i = 0
        display.scroll(blood_types[i])