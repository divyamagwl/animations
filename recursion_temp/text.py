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
        r"\raggedright \quad if(n$\geq$0):\\"
        r"\raggedright \quad \quad return n*fact(n-1)\\"
        r"\raggedright \quad else:\\"
        r"\raggedright \quad \quad return 1\\")
        function.scale(1.3)

        self.play(ReplacementTransform(example, function))
        self.wait(3)
        self.play(ApplyMethod(function.move_to,1.2*UP))
        
        n = TextMobject("Consider", "n = 4")
        n.scale(1.5)
        n.set_color_by_tex_to_color_map({"n = 4": BLUE})
        n.shift(2*DOWN+0.5*LEFT)
        self.play(Write(n))
        self.wait(2)
        

        
