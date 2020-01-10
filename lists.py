# Indexing , slicing and concatenation of lists. 

my_list = [1,2,3]
my_list = ['STRING', 100, 23.2]
print(len(my_list)) # prints the length of the list. 
mylist = ['one','two','three']
print(mylist[0]) # prints elemtent at position 0.
print(mylist[1:]) # prints elements 1 and two from the list. 
another_list = ['four', 'five']
newlist = mylist + another_list
print(newlist)
newlist[0] = 'ONE IN ALL CAPS'
print(newlist)
newlist.append('six')
print(newlist)
newlist.append('seven')
newlist.append(8)
newlist.append("NINE")
print(newlist)
newlist.pop()
print(newlist)
popped_item = newlist.pop()
print(popped_item)
print(newlist)

new_list = ['s','k','j','b','a','f','g']
num_list = [4,8,0,3,6,2,1]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
new_list.reverse()
print(new_list)


