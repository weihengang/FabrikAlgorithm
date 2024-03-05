import turtle as t
import math as m
tscreen = t.Screen()
tscreen.bgcolor("black")
t.tracer(0)
t.hideturtle()
t.color("grey")
t.width(3)
target_point = (-650, 300)
origin_point = (0, 0) #start of link
target_turtle = t.Turtle()
target_turtle.up()
target_turtle.shape("circle")
target_turtle.color("blue")
target_turtle.goto(target_point)
def draw_point(point, color, size, down = False):
    if (not down):
        t.up()
    else:
        t.down()
    t.goto(point)
    t.dot(size, color)
"""
point_1 = (100, 0)
point_2 = (200, 0)
point_3 = (300, 0) 
point_4 = (400, 0)
point_5 = (500, 0)
point_6 = (600, 0)
point_7 = (700, 0)
point_8 = (800, 0)
point_9 = (900, 0)
"""
#end of link
#list_points = [point_9, point_8, point_7, point_6, point_5, point_4, point_3, point_2, point_1, origin_point]
list_points = []
for i in range(0, 36):
    list_points.append((25 * (36 - i + 1), 0))
list_points.append(origin_point)
tscreen.screensize(2000, 1000)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add_links(self, pointlink_back, pointlink_front):
        self.pointlink_back = pointlink_back
        if (not pointlink_back == None):
            self.originaldist_back = m.sqrt(pow(self.x - pointlink_back.x, 2) + pow(self.y - pointlink_back.y, 2)) 
        self.pointlink_front = pointlink_front
        if (not pointlink_front == None):
            self.originaldist_front = m.sqrt(pow(self.x - pointlink_front.x, 2) + pow(self.y - pointlink_front.y, 2))
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.pointlink_back})"
class_points = [] 
for i in range(0, len(list_points)):
    point = list_points[i]
    class_points.append(Point(point[0], point[1]))
for i in range(0, len(class_points)):
    point = class_points[i]
    if (i == 0):
        point.add_links(class_points[i + 1], None)
    elif (i == len(class_points) - 1):
        point.add_links(None, class_points[i - 1])
    else:
        point.add_links(class_points[i + 1], class_points[i - 1])
def reach_target(point_object, targetx, targety):
    refer_back = point_object.pointlink_back
    point_object.x = targetx
    point_object.y = targety
    if (refer_back == None):
        return
    refer_back_dist = m.sqrt(pow(targetx - refer_back.x, 2) + pow(targety - refer_back.y, 2))
    distance_ratio = point_object.originaldist_back / refer_back_dist
    new_targetx = targetx + distance_ratio * (refer_back.x - targetx)
    new_targety = targety + distance_ratio * (refer_back.y - targety)
    reach_target(refer_back, new_targetx, new_targety)
def reach_origin(point_object, targetx, targety):
    refer_front = point_object.pointlink_front
    point_object.x = targetx
    point_object.y = targety
    if (refer_front == None):
        return
    current_dist = m.sqrt(pow(targetx - refer_front.x, 2) + pow(targety - refer_front.y, 2))
    distance_ratio = point_object.originaldist_front / current_dist
    new_targetx = targetx + distance_ratio * (refer_front.x - targetx)
    new_targety = targety + distance_ratio * (refer_front.y - targety)
    reach_origin(refer_front, new_targetx, new_targety)
def click(x, y):
    t.clear()
    target_point = [x, y]
    for i in range(0, 5):
        reach_target(class_points[0], target_point[0], target_point[1])
        reach_origin(class_points[len(class_points) - 1], origin_point[0], origin_point[1])
    draw_point(origin_point, "red", 20)
    draw_point(target_point, "blue", 20)
    for i in class_points:
        draw_point((i.x, i.y), "white", 10, down = True)
    target_turtle.goto(x, y)
    t.update()
click(target_point[0], target_point[1])
target_turtle.ondrag(click)
tscreen.mainloop()