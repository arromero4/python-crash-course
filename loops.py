#----4.3
for n in range(1,21):
    print(n)
print("--------------------------")
#----4.4
#print one million
#it works but takes too much time to execute
#for m in range(1,1_000_000):
    #print(m)

#4.5
#Summing a Million: Make a list of the numbers from one to one million
numbers = [value for value in range(1,1_000_001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("--------------------------")

#4.6 Odd Numbers
for oddNumber in range(1, 21, 2):
    print(oddNumber)
print("--------------------------")

#4-7. Threes
threes = [ value for value in range(3,31,3)]
print(threes)
print("--------------------------")
#4-8 and 4.9. Cubes
cubes = [ value ** 3 for value in range(1,11)]
print(cubes)
