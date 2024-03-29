from manimlib.imports import *

def definition_text():
    return TextMobject(r"A", r"recursive function", r"is a function that calls itself during its", r"execution" ,r".\\ This enables the function to repeat itself ",r"several times", r",\\outputting the result and the end of each iteration.")


class IntroText(Scene):
    def construct(self):
        
        title = TextMobject(r"Recursive" , "Functions")
        title.shift(3*UP)
        title.scale(1.5)
        title.set_color_by_tex_to_color_map({
        "Recursive" : YELLOW,
        "Functions" : BLUE 
        })

        self.play(Write(title))
        self.wait(2)

        definition = definition_text()
        definition.set_color_by_tex_to_color_map({
        "recursive function": YELLOW,
        "execution": BLUE
        })
        definition.scale(0.8)
        
        self.play(Write(definition))
        self.wait(4)
        
        self.play(FadeOut(title))

        utext = TextMobject("Let us try to", "understand recursion", "through an example")
        utext.set_color_by_tex_to_color_map({"understand recursion": YELLOW})
        self.play(ReplacementTransform(definition,utext))
        self.wait(3)

        example = TextMobject("Consider a function which outputs", "factorial", "of a number")
        example.set_color_by_tex_to_color_map({"factorial": BLUE})
        self.play(ReplacementTransform(utext,example))
        self.wait(3)

        function = TextMobject(r"\raggedright def fact(n):\\",
        r"\raggedright \quad if(n$>$0):\\"
        r"\raggedright \quad \quad return n*fact(n-1)\\"
        r"\raggedright \quad else:\\"
        r"\raggedright \quad \quad return 1\\")
        function.scale(1.3)

        self.play(ReplacementTransform(example, function))
        self.wait(3)
        self.play(ApplyMethod(function.move_to,1.2*UP))
        
        n = TextMobject("Consider", "n = 4")
        n.scale(1.4)
        n.set_color_by_tex_to_color_map({"n = 4": BLUE})
        n.shift(2*DOWN+0.5*LEFT)
        self.play(Write(n))
        self.wait(2)
        
class Boxes(Scene):
  def construct(self):
    
    rectangle1 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)
    text1 = TextMobject(r"n = 4\\ return 4*fac(3)")
    text1.scale(0.7)
    Box1 = VGroup(rectangle1,text1)
    Box1.shift(5*LEFT + 2.7*UP)
    curved1 = CurvedArrow(start_point = 5*LEFT + 2.075*UP ,end_point = 1.3*UP + 3.75*LEFT, color = BLUE)

    self.play(ShowCreation(Box1))
    self.play(ShowCreation(curved1))
    self.wait(1)

    rectangle2 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)
    text2 = TextMobject(r"n = 3\\ return 3*fac(2)")
    text2.scale(0.7)
    Box2 = VGroup(rectangle2,text2)
    Box2.shift(2.5*LEFT + 1.3*UP)
    curved2 = CurvedArrow(start_point = 2.5*LEFT + 0.675*UP ,end_point = 0.1*DOWN + 1.25*LEFT, color = BLUE)
    
    self.play(ShowCreation(Box2))
    self.play(ShowCreation(curved2))
    self.wait(1)

    rectangle3 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)
    text3 = TextMobject(r"n = 2\\ return 2*fac(1)")
    text3.scale(0.7)
    Box3 = VGroup(rectangle3,text3)
    Box3.shift(0.1*DOWN)
    curved3 = CurvedArrow(start_point = 0.675*DOWN ,end_point = 1.5*DOWN + 1.25*RIGHT, color = BLUE)

    self.play(ShowCreation(Box3))
    self.play(ShowCreation(curved3))
    self.wait(1)

    rectangle4 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)
    text4 = TextMobject(r"n = 1\\ return 1*fac(0)")
    text4.scale(0.7)
    Box4 = VGroup(rectangle4,text4)
    Box4.shift(2.5*RIGHT + 1.5*DOWN)
    curved4 = CurvedArrow(start_point = 2.5*RIGHT + 2.125*DOWN ,end_point = 2.9*DOWN + 3.75*RIGHT, color = BLUE)
 
    self.play(ShowCreation(Box4))
    self.play(ShowCreation(curved4))
    self.wait(1)

    rectangle5 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)
    text5 = TextMobject(r"n = 0\\ return 1")
    text5.scale(0.7)
    Box5 = VGroup(rectangle5,text5)
    Box5.shift(5*RIGHT + 2.9*DOWN)
    
    self.play(ShowCreation(Box5))
    self.wait(1)
   
    text6 = TextMobject("1")
    text6.shift(5*RIGHT + 2.9*DOWN)
    text6.scale(1.5)
    curved5 = CurvedArrow(start_point = 2.8*DOWN + 5*RIGHT, end_point = 3.75*RIGHT + 1.5*DOWN, color = BLUE)
    self.play(Transform(Box5,text6))
    self.play(Transform(curved4,curved5))
    self.wait(1) 

    rectangle7 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)    
    text7 = TextMobject(r"n = 1\\ return 1*1")
    text7.scale(0.7)
    Box7 = VGroup(rectangle7,text7)
    Box7.shift(2.5*RIGHT + 1.5*DOWN)
    self.play(Transform(Box4,Box7))
    self.wait(1)

    text8 = TextMobject("1")
    text8.shift(2.5*RIGHT + 1.5*DOWN)
    text8.scale(1.5)
    curved6 = CurvedArrow(start_point = 1.4*DOWN + 2.5*RIGHT, end_point = 1.25*RIGHT + 0.1*DOWN, color = BLUE)
    self.play(Transform(Box4,text8))
    self.play(Transform(curved3,curved6))
    self.wait(1)

    rectangle8 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)    
    text9 = TextMobject(r"n = 2\\ return 2*1")
    text9.scale(0.7)
    Box8 = VGroup(rectangle8,text9)
    Box8.shift(0.1*DOWN)
    self.play(Transform(Box3,Box8))
    self.wait(1)
    
    text10 = TextMobject("2")
    text10.shift(0.1*DOWN)
    text10.scale(1.5)
    curved7 = CurvedArrow(start_point = 0.1*UP, end_point = 1.25*LEFT + 1.3*UP, color = BLUE)
    self.play(Transform(Box3,text10))
    self.play(Transform(curved2,curved7))
    self.wait(1)

    rectangle9 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)    
    text11 = TextMobject(r"n = 3\\ return 3*2")
    text11.scale(0.7)
    Box9 = VGroup(rectangle9,text11)
    Box9.shift(2.5*LEFT + 1.3*UP)
    self.play(Transform(Box2,Box9))
    self.wait(1)
    
    text12 = TextMobject("6")
    text12.shift(2.5*LEFT + 1.3*UP)
    text12.scale(1.5)
    curved8 = CurvedArrow(start_point = 2.5*LEFT + 1.5*UP, end_point = 2.7*UP + 3.75*LEFT, color = BLUE)
    self.play(Transform(Box2,text12))
    self.play(Transform(curved1,curved8))
    self.wait(1)

    rectangle10 = Rectangle(height = 1.25, width = 2.5, color=YELLOW, color_opacity=0.2, fill_color=YELLOW, fill_opacity=0.05)    
    text13 = TextMobject(r"n = 4\\ return 4*6")
    text13.scale(0.7)
    Box10 = VGroup(rectangle10,text13)
    Box10.shift(5*LEFT + 2.7*UP)
    self.play(Transform(Box1,Box10))
    self.wait(1)
    
    text14 = TextMobject("24")
    text14.shift(5*LEFT + 2.7*UP)
    text14.scale(1.5)
    self.play(Transform(Box1,text14))
    self.wait(1)

