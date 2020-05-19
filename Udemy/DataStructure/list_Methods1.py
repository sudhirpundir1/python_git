nums=range(1,6)
num =list(nums)
num.append('a') #-- Only appends a single value
num.extend(['xxx','yy'])  #-- Can append multiple values
num.insert(1,'abc') #-- add element at 1st insex or 2nd position.
num.insert(len(num),100) #--Add element at end of the list.
print(num)

num_copy = num.copy()
print(num_copy)