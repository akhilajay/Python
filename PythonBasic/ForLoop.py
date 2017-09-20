print('Looping')
#for loop
for x in range(0,5):
    print(x,end=" ")

# loop through a list
print('\n')
list=['one','two','three','four']
for a in list:
    print(a)

for b in ["akhil","ramya","kannan"]:
     print(b)

for z in [10,20,30,40,50]:
     print(z)
#multi dimensional array
num_list=[[1,2,3],[10,20,30],[100,200,330]]
for x in num_list:
    for y in x:
        print(y)

print("\n")

for p in range(0,3):
    for q in range(0,3):
        print(num_list[p][q])
