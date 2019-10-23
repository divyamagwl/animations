from manimlib.imports import *

class Union(Scene):
    def construct(self):
        circle1 = Circle(radius = 1.5, color= YELLOW, fill_color = YELLOW,  fill_opacity=0.2)
        circle1.shift(2*LEFT)
        A = TextMobject("A")
        A.shift(3*LEFT)
        self.play(ShowCreation(circle1))
        self.play(Write(A))
        self.wait(0.5)

        circle2 = Circle(radius = 1, color = BLUE, fill_color = BLUE, fill_opacity=0.2)
        circle2.shift(2*RIGHT)
        B = TextMobject("B")
        B.shift(2.5*RIGHT)
        self.play(ShowCreation(circle2))
        self.play(Write(B))
        self.wait(0.5)

        self.play(ApplyMethod(circle1.move_to, 1*LEFT), ApplyMethod(circle2.move_to, 0.5*RIGHT), ApplyMethod(A.move_to, 2*LEFT), ApplyMethod(B.move_to, 1*RIGHT)) 

        circle3 = Circle(radius = 1.5, color= GREEN, fill_color = GREEN,  fill_opacity=0.2)
        circle3.shift(1*LEFT)
        circle4 = Circle(radius = 1, color= GREEN, fill_color = GREEN,  fill_opacity=0.2)
        circle4.shift(0.5*RIGHT)
        
        self.play(Transform(circle1,circle3), Transform(circle2,circle4))
 
        AUB = TextMobject(r"A $\cup$ B")
        AUB.shift(2*DOWN)
        self.play(Write(AUB))
        self.wait(3)
       

