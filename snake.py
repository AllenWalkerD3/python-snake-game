
from turtle import Turtle, pos


STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90) 
    def move_down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(270)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)

    def check_wall_collions(self):
        if self.head.xcor() < -280 or self.head.xcor() > 280 or self.head.ycor() < -280 or self.head.ycor() > 280:
            return True
        return False
    
    def check_tail_collions(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False