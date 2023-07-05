bangla = int(input('Please enter your marks for Bangla? '))
english = int(input('Please enter your marks for English? '))
math = int(input('Please enter your marks for Math? '))
science = int(input('Please enter your marks for Science? '))

avr= (bangla + english + math + science) / 4

if avr > 90:
    print('Your grade point is A+')
elif avr > 80:
    print('Your grade point is A')
elif avr > 70:
    print('Your grade point is B')
elif avr > 60:
    print('Your grade point is C')
elif avr > 40:
    print('Your grade point is D')
else:
    print('You are fail')
