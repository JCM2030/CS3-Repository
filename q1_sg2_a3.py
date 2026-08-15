year = int(input('Enter your birth year: '))
if year < 1900:
  print('Invalid Year, it should not be earlier than 1900')
else: rem = (year - 1900) % 12
print(rem)
