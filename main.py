# Write a program to overload the less than (<) and equal to (==) operators.
# For example, create objects - ob1 and ob2 with values 3 and 4 to compare values,
#  respectively. You can additionally create more objects to try different values.

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self,other):
        x=self.x < other.x
        y=self.y < other.y
        return x,y
    def __eq__(self,other):
        x=self.x == other.x
        y=self.y == other.y
        return x,y
    def show1(self):
        print (f"{self.x} {self.y}")    


ob1=point(3,4)   
ob2=point(3,4)
print(ob1<ob2)
print(ob1==ob2)

    