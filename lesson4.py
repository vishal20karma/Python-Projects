# Integer Divison (//)
a=2
b=3
c=1
d=0.5
intDiv1=a//b
intDiv2=b//a
intDiv3=a//d
intDiv4=d//a
print(intDiv1)   # it prints the lowest rounding value, exact value of 2/3=0.33 but it prints '0'
print(intDiv2)   # it prints the lowest rounding value, exact value of 3/2=1.5 but it prints '1'
print(intDiv3)   # it prints the lowest rounding value, exact value of 2/0.5=4 but it prints '4.0'
print(intDiv4)   # it prints the lowest rounding value, exact value of 0.5/2=0.25 but it prints '0'
# any negative result will be one more smaller output, example, -5.2 will result in -6

print("###########################################")

# only negative denominator results in negative output, rest all returns positive output
x,y,z=3,4,-2
intDiv5=x/y
intDiv6=x/z
intDiv7=z/z
intDiv8=z/x
print(intDiv5)
print(intDiv6)
print(intDiv7)
print(intDiv8)