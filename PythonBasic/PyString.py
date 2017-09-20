print('py Strigns')

long_string ="i'll catch up if you fall - The Floor"

#print out first 4 char
print(long_string[0:4])

#print last 5 char
print(long_string[-5:])

#print everything upto last 5
print(long_string[:-5])

#concatincate/ join
print(long_string+ " be there")

#format String . adding value dynamically to a string
print("%c is my %s letter and my number %d number is %.5f"%('X','fav',1,.14))

#print capitalise the first letter
print(long_string.capitalize())

#print index value of the start of a string
print(long_string.find('Floor'))

#to check all char are string
print('A23'.isalpha())

print(long_string.isalnum())

print(len(long_string))

print(long_string.replace("Floor","Gorund"))

# remove white space

print(long_string.strip())

