a = [1,2,3,4,5]
#list comprehension cu 2 for-uri, creeaza un set
b = {(x,y) for x in a for y in a}
print(b)