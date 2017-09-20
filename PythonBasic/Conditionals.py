print('Conditionals')

## if elif

age =10

if age >16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >=21:
    print('You are old enough to drive a tractor')
elif age>=16:
    print('You are old enough to drive')
else:
    print('You cant drive')

#and -- or

if((age>=1) and (age<=18)):
    print('You get a big birthday')
elif((age==21) or (age>=65)):
    print('You get a birthday')
elif(age ==30):
    print('you wont get a birthday')
else:
   print ('Yeahhh!!!')
