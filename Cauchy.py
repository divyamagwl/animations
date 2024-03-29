from manimlib.imports import *
import numpy as np

def get_definition_text():
    return TextMobject(r"A" ,r"sequence $X = (x_n)$" ,r"of real numbers is said to be a ", r"Cauchy sequence", r"""if\\ $\forall$ $\epsilon$  \textgreater 0 $\exists$ N($\epsilon$) $\in$ natural numbers such that $\forall$ natural numbers\\ $n, m \textgreater$ N($\epsilon$), the terms ($x_n$), ($x_m$) satisfy $| x_n - x_m | \textless \epsilon$.""")

def get_custom_definition_text():
    custom_definition = TextMobject(r"Since $\forall$ $\epsilon$ $\exists$ an index number N($\epsilon$) after which the",
                        r"difference \\between two numbers in the sequence is less than the $\epsilon$ value")
    """custom_definition = TextMobject(r"The ",
                        r"sequence $20 \frac{(-1)^n}{n} + 4$",
                        r"is said to be a ", r"Cauchy sequence ",
                        r"if $\forall$ $\epsilon$ \\", 
                        r"$\exists$ an index number after which the",
                        r"difference between two\\ numbers in the sequence is less than the $\epsilon$ value")"""
    custom_definition.scale(0.6)
    custom_definition.shift(2.6*RIGHT+3*UP)

    return custom_definition

def get_distance_text():    
    return distance
       
class IntroText(Scene):
    def construct(self):
        text1 = get_definition_text()
        text1.set_color_by_tex_to_color_map({r"sequence $X = (x_n)$": YELLOW})
        text1.set_color_by_tex_to_color_map({r"Cauchy sequence": YELLOW})
        text1.scale(0.8)

        title = TextMobject(r"Graphical", r"representaion", r"of a", r"Cauchy", r"Sequence")
        title.shift(3 * UP)
        title.scale(1.35)
        title.set_color_by_tex_to_color_map({
            "Sequence": BLUE,
            "Cauchy": YELLOW,
            "Graphical": YELLOW,
            "representaion": BLUE
        })
        
        self.play(Write(text1))
        self.wait(4)
        self.play(ApplyMethod(text1.move_to, 1*DOWN))
        self.play(Write(title))
        self.wait(3)

        text2 = TextMobject("So how do we depict these sequences on graph?")
        self.play(ReplacementTransform(text1, text2))
        self.wait(2)
        self.play(FadeOut(text2), FadeOut(title))
        self.wait(1)

class ShowEquation(Scene):
    def construct(self):
        text = TextMobject("Consider the sequence")
        text.shift(1*UP)
        eqn = TextMobject(r"$20 \frac{(-1)^n}{n} + 4$")
        self.play(Write(text), Write(eqn))
        self.wait(2)

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 30.5,
        "y_min": -10,
        "y_max": 10,
        "graph_origin": ORIGIN+4*LEFT,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$n$",
        "y_axis_label": "$y_n$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(0, 31, 5),
        "y_labeled_nums": range(-10,11,2)
    }

    def construct(self):
        X_TICKS_DISTANCE = self.x_axis_width / (self.x_max - self.x_min)
        Y_TICKS_DISTANCE = self.y_axis_height / (self.y_max - self.y_min)
        epsilon = 2
        limit = 4
        n = 10

        self.setup_axes(animate=True) # sets up axis on the scene
        points = [ Dot(color = RED, radius = 0.05) for dot in range(3,32) ]
        equation = TextMobject(r"$20 \frac{(-1)^n}{n} + 4$")
        equation.shift(3.5*RIGHT+3*UP)
        self.play(FadeIn(equation))


        mathfunc = lambda x: 20*((-1)**x)/x + 4
        [points[counter].shift(self.graph_origin + counter * (RIGHT * X_TICKS_DISTANCE) +
                               mathfunc(counter) * (UP * Y_TICKS_DISTANCE)) for counter in range(1, len(points))]

        positive_epsilon = DashedLine(start = self.graph_origin, end=4.3*RIGHT, color=DARK_BROWN)
        positive_epsilon.shift(Y_TICKS_DISTANCE*(limit + epsilon)*UP)

        negative_epsilon = DashedLine(start = self.graph_origin, end=4.3 * RIGHT, color=DARK_BROWN)
        negative_epsilon.shift(Y_TICKS_DISTANCE * (limit - epsilon) * UP)

        epsilon_band = VGroup(positive_epsilon, negative_epsilon)

        for point in range(1,len(points)):
            self.add(points[point])
            self.wait(0.1)

        self.wait(1) 

        lim = TextMobject(r"Let $\epsilon$ = $4$")
        lim.shift(2*DOWN+1*RIGHT)
        lim.scale(0.9)        
        self.play(Write(lim))
        self.wait(2)
        self.play(Transform(lim, epsilon_band))

        N_value = TextMobject("$N(\epsilon)$")
        N_value.set_color_by_tex_to_color_map({"$N(\epsilon)$":YELLOW})
        N_value.shift(self.graph_origin + RIGHT*X_TICKS_DISTANCE*n + UP*(Y_TICKS_DISTANCE*mathfunc(n)+0.3))
        N_value.scale(0.8)
        N =  Dot(color = YELLOW, radius = 0.1)
        N.shift(self.graph_origin + RIGHT*X_TICKS_DISTANCE*n + UP*Y_TICKS_DISTANCE*mathfunc(n))
        self.play(ShowCreation(N))
        self.play(ShowCreation(N_value))
        self.wait(0.5)

        midtext = TextMobject("""$\\forall$""", r"n,m \textgreater $N(\epsilon)$")
        midtext.set_color_by_tex_to_color_map({r"n,m \textgreater $N(\epsilon)$":PINK})
        midtext.scale(0.6); midtext.shift(2.1*UP+0.2*RIGHT)
        self.play(Write(midtext))

        more_dots = [ Dot(color = BLUE_A, radius = 0.06) for index in range(11,30)]
        [more_dots[counter].shift(self.graph_origin + (counter+10) * (RIGHT * X_TICKS_DISTANCE) + mathfunc(counter+10) * (UP * Y_TICKS_DISTANCE)) for counter in range(1,19)]

        for point in range(1,len(more_dots)):
            self.add(more_dots[point])
            self.wait(0.2)
        self.wait(0.5)

        distance1 = TextMobject(r"""Notice that for all points after N""" )
        distance1.scale(0.7) 
        distance1.shift(2.3*DOWN+1*RIGHT)
        self.play(Transform(midtext, distance1))

        newdots =  Dot(color = GREEN, radius = 0.065)
        newdots.shift(self.graph_origin + RIGHT*X_TICKS_DISTANCE*(n+3) + UP*Y_TICKS_DISTANCE*mathfunc(n+3))
        self.play(ShowCreation(newdots))

        XN_value = TextMobject("$x_n$")
        XN_value.set_color_by_tex_to_color_map({"$x_n$":GREEN})
        XN_value.shift(self.graph_origin + RIGHT*X_TICKS_DISTANCE*(n+3) + UP*(Y_TICKS_DISTANCE*mathfunc(n+3)-0.34))
        XN_value.scale(0.7)
        self.play(ShowCreation(XN_value))

        newdots2 =  Dot(color = GREEN, radius = 0.065)
        newdots2.shift(self.graph_origin + RIGHT*X_TICKS_DISTANCE*(n+6) + UP*Y_TICKS_DISTANCE*mathfunc(n+6))
        self.play(ShowCreation(newdots2))

        XM_value = TextMobject("$x_m$")
        XM_value.set_color_by_tex_to_color_map({"$x_m$":GREEN})
        XM_value.shift(self.graph_origin + RIGHT*(X_TICKS_DISTANCE*(n+6)+0.1) + UP*(Y_TICKS_DISTANCE*mathfunc(n+6)+0.4))
        XM_value.scale(0.7)
        self.play(ShowCreation(XM_value))

        distance2 = TextMobject(r"""The distance between $x_n$ and $x_m$ remains inside the \\given band. \textit{i.e} $| x_n - x_m | \textless 4$ $\forall$ $n,m \textgreater N(\epsilon)$""")
        distance2.scale(0.7) 
        distance2.shift(2.3*DOWN+1*RIGHT)
        self.play(Transform(midtext,distance2))

        band_rectangle = Rectangle(color=GOLD_B, color_opacity=0.2, fill_color=GOLD_B, fill_opacity=0.2, height=Y_TICKS_DISTANCE*4, width=X_TICKS_DISTANCE*30)
        band_rectangle.shift(self.graph_origin+X_TICKS_DISTANCE*RIGHT*15 + Y_TICKS_DISTANCE * UP*4)

        self.play(ShowCreation(band_rectangle))
        self.wait(3)

        similar = TextMobject(r"""Similarly this is true for all values of $\epsilon$""")
        similar.scale(0.7) 
        similar.shift(3.3*DOWN+1*RIGHT)
        self.play(Write(similar))
        self.wait(2)

        custom_definition = get_custom_definition_text()
        self.play(Transform(equation, custom_definition))
        self.wait(3)

        explanation = TextMobject(r"Therefore the sequence is a ", r"Cauchy Sequence")
        explanation.scale(0.7); explanation.shift(3.3*DOWN+1*RIGHT)
        explanation.set_color_by_tex_to_color_map({r"Cauchy Sequence": RED})
        self.play(Transform(similar,explanation))
        self.wait(3)

