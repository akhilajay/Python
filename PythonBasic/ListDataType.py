grocery_list=['tomato','potato','jackFruit','coconut','bananans']
print("item is ",grocery_list[2])
#replace an item at a location
grocery_list[0]="kiwi"
print("updated  is ",grocery_list)
# print items in a list
print(grocery_list[0:2])

other_events=['Wash Car','Cash Check','Pick Up Kids']

#Adding 2 list to another list
to_do_list=[other_events,grocery_list]
#Print items from list inside a list
print(to_do_list[0][0])
#Append an element at end
grocery_list.append('Apple')
print(to_do_list)
#Replace an iteam in an exisitng location
grocery_list[5]='Onion'
print(to_do_list)
#insert an item at a specific location
grocery_list.insert(0,'Pine Apple')
print(to_do_list)
#remove an item
grocery_list.remove("Pine Apple")
print(to_do_list)
#sorting
grocery_list.sort()
print(to_do_list)
#reversing
grocery_list.reverse()
print(to_do_list)
#deleting an item at specific location
del grocery_list[0]
print(to_do_list)
## Merging to list
to_do_list2= grocery_list+other_events
print(to_do_list2)
#length of a list
print(len(to_do_list2))

print(to_do_list)
print(max(to_do_list))
print(min(to_do_list))