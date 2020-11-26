#Taking Inputs
lr = int(input("Length: "))
br = int(input("Breadth: "))
rc = int(input("Radius: "))
#Processing on inputs
pr = (br+lr)*2
ar = br*lr
cc = 22*rc/7
ac = (22*(rc**2))/7
#Giving Outputs
print("Area of Rectangle:%d\nPerimeter of Rectangle:%d\nCircumference of Circle:%d\nArea of Circle:%d"%(ar,pr,cc,ac))

