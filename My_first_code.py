#my first python code

print ("I am Samina")
print ("I'm Samina")
print ('I am "Samina"')
print ("My name is"" ""Samina")
print ('I\'m Samina')

# Operators

val1= 20
val2 = 5
print (val1 / val2)
val3 = 20.5
print (val3 // val2) #gives floor value
print(val3 % val2)   #gives remainder
val4 = 4
print(val2 ** val4)  #raises val4 to the val2 i.e. 5power4
#precedence of comparison operators is same but lower than arithemetic operators
print(val1>val2<val4)
print(val3<=val1)
print(val2!=val4)
print(val2==val2)
print(val3%100)
#arithemetic operators precedence follows PEMDAS

print (val1+val2/val2**(val4//val4))

a, b = 10, 20
min = a if a < b else b
print(min)
#if-else with comparison operators
if (val1 > val2):
   print(val2, "is greater")

#Expressions
    #relational expressions
res = (val1 + val2) <= (val3 - val4)
print(res)
    #logical expressiions
res3 = val1 and val2
print (res3)
