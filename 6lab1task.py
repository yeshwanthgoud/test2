import math

class point():

   x = 0

   y = 0

pt1=point()

pt2=point()



def distance_between_points(p1,p2):



 pnt1_x=int(input("Enter the value of x co-ordinate of point 1 "))

 pnt1_y=int(input("Enter the value of y co-ordinate of point 1 "))

 pnt2_x=int(input("Enter the value of x co-ordinate of point 2 "))

 pnt2_y=int(input("Enter the value of y co-ordinate of point 2 "))

 p1.x = pnt1_x

 p1.y = pnt1_y

 p2.x = pnt2_x

 p2.y = pnt2_y

 print("The first set of points are (%s, %s) "%(p1.x,p1.y))

 print("The second set of points are (%s, %s) "%(p2.x,p2.y))

 first_point=(p1.x,p1.y)

 second_point=(p2.x,p2.y)

 y=dist(first_point,second_point)

 return y



def dist(first,second):

  

  X=(abs((second[0]-first[0])**2))+(abs((second[1]-first[1])**2))

  distance=float(math.sqrt(X))

  return distance

result=distance_between_points(pt1,pt2)

print("The distance between two points are %s " %result) 

