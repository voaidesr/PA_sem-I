text = input().strip() 
x = text.split(" ")
y = ""
for i in range(len(x)):
    x[i] = x[i].capitalize()
text = " ".join(x)
print (text)
 