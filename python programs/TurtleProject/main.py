from turtle import Turtle,Screen
totty=Turtle();
print(totty)
totty.shape("turtle");
totty.color("orange");
totty.forward(100);
myscreen=Screen();
height=myscreen.canvheight;

print(height);
myscreen.exitonclick();