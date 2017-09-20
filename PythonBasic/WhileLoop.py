print('while loop')

# to generate random number
import random

#While are used when we are unsure about how many times we need to loop
randum_num = random.randrange(0,100)

while(randum_num!=15):
    print(randum_num)
    randum_num=random.randrange(0,100)

print("\n")
#while loop like for loop
i=0;
while (i<=20):
    if(i%2==0):
        print(i)
    elif(i==9):
        break

    i+=1

