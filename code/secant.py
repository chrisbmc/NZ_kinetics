from manimlib.imports import *

class ExpVsLn(GraphScene):
    CONFIG = {
            "x_min" : -10,
            "x_max" : 10,
            "y_min" : -10,
            "y_max" : 10,
            "y_labeled_nums" : list(range(-10,10,2)),
            "x_labeled_nums" : list(range(-10,10,2)),
            "x_axis_label" : "x",
            "y_axis_label" : "y",
            #"y_tick_frequency" : 10,
            "graph_origin" : UP+DOWN, 
            }
    def construct(self):
        self.setup_axes(animate=True)
        self.comp()

    def comp(self):
        self.graph_exp = self.get_graph(np.exp, x_max = 2.3)
        self.graph_ln = self.get_graph(np.log, x_min = 0.01)
        self.graph_x = self.get_graph(lambda x: x)
        self.play(ShowCreation(self.graph_exp, run_time=2))
        self.play(ShowCreation(self.graph_ln, run_time=2))
        self.play(ShowCreation(self.graph_x, run_time=2))
        self.wait(2)
class ExpGrad(GraphScene):
    CONFIG = {
            "x_min" : -3,
            "x_max" : 3,
            "y_min" : -3,
            "y_max" : 3,
            "y_labeled_nums" : list(range(-3,3,1)),
            "x_labeled_nums" : list(range(-3,3,1)),
            "x_axis_label" : "x",
            "y_axis_label" : "y",
            "graph_origin" : UP+DOWN,
            }
    def construct(self):
        self.setup_axes(animate=True)
        self.ex_grad()
        self.ln_grad()
        self.graph_linear = self.get_graph(lambda x: x, color=YELLOW)
        graph_label = self.get_graph_label(
                self.graph_linear, "x", color=YELLOW, direction=RIGHT)
        self.play(ShowCreation(self.graph_linear),
                Write(
                    graph_label,
                    rate_func = squish_rate_func(smooth, 0.5,1)
                    )
                )
        self.wait(5)

    def ln_grad(self):
        self.graph_ln = self.get_graph(np.log, x_min = 0.05, color=GREEN)
        graph_label = self.get_graph_label(
                self.graph_exp, "\\ln(x)", color=GREEN, direction = RIGHT
                )
        graph_label.shift(1.8*DOWN+RIGHT)
        coord_label = TexMobject("(0.5,-0.69)").shift(2*RIGHT+DOWN).set_color(RED)
        self.play(ShowCreation(self.graph_ln, run_time=2),
                Write(
                    graph_label,
                    rate_func = squish_rate_func(smooth, 0.5, 1),
                    )
                )
        self.wait(2)
        self.h_line = Line(self.coords_to_point(0,-0.69),self.coords_to_point(0.5,-0.69), color=WHITE)
        self.v_line = self.get_vertical_line_to_graph(
                0.5, self.graph_ln,
                color=WHITE,
                )
        self.add(self.h_line,self.v_line)
        self.play(Write(coord_label))
        self.wait(4)
        self.slope_1 = self.get_graph(lambda x: 2*x -1.69, x_min=0, x_max= 1)
        slope_label = self.get_graph_label(
                self.slope_1, "Gradient = 2", direction = LEFT
                )
        slope_label.shift(5.2*DOWN+5*LEFT)
        self.play(ShowCreation(self.slope_1,run_time=2),
                Write(
                    slope_label,
                    rate_func = squish_rate_func(smooth,0.5,1)
                    )
                )
        self.wait(2)

        coord_label_2 = TexMobject("(2,0.69)").shift(2*RIGHT+UP).set_color(RED)
        self.h_line_2 = Line(self.coords_to_point(0,0.69),self.coords_to_point(2,0.69), color=WHITE)
        self.v_line_2 = self.get_vertical_line_to_graph(
                2, self.graph_ln,
                color=WHITE,
                )
        self.add(self.h_line_2,self.v_line_2)
        self.play(Write(coord_label_2))
        self.slope_2 = self.get_graph(lambda x: 0.5*x -0.31, x_min=1, x_max=3, color=YELLOW )
        slope_label_2 = self.get_graph_label(
                self.slope_2, "Gradient = 0.5", direction = RIGHT
                )
        slope_label_2.shift(3.2*DOWN+1.4*LEFT)
        self.play(ShowCreation(self.slope_2,run_time=2),
                Write(
                    slope_label_2,
                    rate_func = squish_rate_func(smooth,0.5,1)
                    )
                )
        self.wait(2)

        self.deriv_1 = TexMobject("\\frac{dy}{dx} =\\frac{1}{x}").shift(1.5*DOWN+5.5*LEFT).set_color(GREEN)
        self.play(Write(self.deriv_1))
        self.wait(5)
        self.remove(slope_label,slope_label_2,
                self.h_line,self.h_line_2,
                self.v_line,self.v_line_2,
                self.slope_1,self.slope_2,
                coord_label,coord_label_2
                )
        self.wait(1)

    def ex_grad(self):
        self.graph_exp = self.get_graph(np.exp, x_max = 1.1)
        graph_label = self.get_graph_label(
                self.graph_exp, "\\exp(x)", direction = RIGHT
                )
        coord_label = TexMobject("(-0.69,0.5)").shift(2*LEFT+UP).set_color(RED)
        self.play(ShowCreation(self.graph_exp, run_time=2),
                Write(
                    graph_label,
                    rate_func = squish_rate_func(smooth, 0.5, 1),
                    )
                )
        self.wait(2)
        self.h_line = Line(self.coords_to_point(0,0.5),self.coords_to_point(np.log(0.5),0.5), color=WHITE)
        self.v_line = self.get_vertical_line_to_graph(
                -np.log(2), self.graph_exp,
                color=WHITE,
                )
        self.add(self.h_line,self.v_line)
        self.play(Write(coord_label))
        self.wait(4)
        self.slope_1 = self.get_graph(lambda x: 0.5*x +0.847, x_min=-2, x_max= 0.62)
        slope_label = self.get_graph_label(
                self.slope_1, "Gradient = 0.5", direction = LEFT
                )
        slope_label.shift(3.2*DOWN+5*LEFT)
        self.play(ShowCreation(self.slope_1,run_time=2),
                Write(
                    slope_label,
                    rate_func = squish_rate_func(smooth,0.5,1)
                    )
                )
        self.wait(2)

        coord_label_2 = TexMobject("(0.69,2)").shift(2*RIGHT+2*UP).set_color(RED)
        self.h_line_2 = Line(self.coords_to_point(0,2),self.coords_to_point(np.log(2),2), color=WHITE)
        self.v_line_2 = self.get_vertical_line_to_graph(
                np.log(2), self.graph_exp,
                color=WHITE,
                )
        self.add(self.h_line_2,self.v_line_2)
        self.play(Write(coord_label_2))
        self.slope_2 = self.get_graph(lambda x: 2*x +0.61, x_min=0.08, x_max= 1.31)
        slope_label_2 = self.get_graph_label(
                self.slope_2, "Gradient = 2", direction = RIGHT
                )
        slope_label_2.shift(4.2*DOWN+1.4*LEFT)
        self.play(ShowCreation(self.slope_2,run_time=2),
                Write(
                    slope_label_2,
                    rate_func = squish_rate_func(smooth,0.5,1)
                    )
                )
        self.wait(2)

        self.deriv_1 = TexMobject("\\frac{dy}{dx} =y").shift(UP+5.5*LEFT).set_color(BLUE)
        self.play(Write(self.deriv_1))
        self.wait(5)
        self.remove(slope_label,slope_label_2,
                self.h_line,self.h_line_2,
                self.v_line,self.v_line_2,
                self.slope_1,self.slope_2,
                coord_label,coord_label_2
                )
        self.wait(1)



class XSquared(GraphScene):
    CONFIG = {
            "x_min" : -1,
            "x_max" : 4,
            "y_min" : -1,
            "y_max" : 8,
            "x_axis_label" : "x",
            "y_axis_label" : "y",
            "graph_origin" : 2*DOWN + 5*LEFT,
            "example_inputs" : [1,2],
            "small_dx" : 0.01,
            "x_labeled_nums" : list(range(-1,4)),
            "y_labeled_nums" : list(range(-1,8,2))
            }
    def construct(self):
        self.setup_axes(animate=True)
        self.deriv()

    def deriv(self):
        self.graph = self.get_graph(self.func_to_graph, color = BLUE_C) 
        graph_label = self.get_graph_label(
                self.graph, "\\frac{1}{2}x^2", direction = LEFT
                )
        graph_label.shift(MED_SMALL_BUFF*LEFT)
        self.play(
                ShowCreation(self.graph, run_time = 2),
                Write(
                    graph_label,
                    rate_func = squish_rate_func(smooth, 0.5, 1),
                    )
                )
        self.wait(2)
        deltaxs = np.arange(self.example_inputs[0]+1,self.example_inputs[0]-0.25, -0.25)
        v_lines = self.get_v_lines(
                self.example_inputs[0], 
                deltaxs
                )
        slope_vals = self.get_slopes(
                self.example_inputs[0],
                deltaxs
                )
        sgraphs = []
        for i in range(len(slope_vals)):
            sgraphs.append(self.get_graph(lambda x: slope_vals[i][0]*x + slope_vals[i][1], x_min = 0, x_max = deltaxs[i]+1, color = RED))
        slope_tex = [TexMobject("gradient\\\=%.1f ~"%i[0]).shift(2*DOWN+5*RIGHT).set_color(RED) for i in slope_vals]
        second_tex = TexMobject("gradient\\\ = \\frac{(2^2-1^2)}{2}").shift(2*DOWN+5*RIGHT).set_color(RED)
        first_tex = TexMobject("gradient\\\ = \\frac{\Delta X}{\Delta Y}").shift(2*DOWN+5*RIGHT).set_color(RED)
        self.add(v_lines[0],v_lines[1])
        self.add(sgraphs[0])
        self.add(first_tex)
        self.wait(4)
        self.play(ReplacementTransform(first_tex,second_tex))
        self.wait(2)
        self.play(ReplacementTransform(second_tex,slope_tex[0]))
        self.wait(1)
        print("%.1f"%(slope_vals[0][0]))
        for i in range(len(v_lines)-2):
            self.play(
                    AnimationGroup(
                        ReplacementTransform(v_lines[i+1],v_lines[i+2]), 
                        ReplacementTransform(sgraphs[i],sgraphs[i+1]),
                        ReplacementTransform(slope_tex[i],slope_tex[i+1])
                        )
                    )
            self.wait(1)
        deltaxs = np.arange(self.example_inputs[1]+1,self.example_inputs[1]-0.25, -0.25)
        v_lines = self.get_v_lines(
                self.example_inputs[1], 
                deltaxs
                )
        slope_vals = self.get_slopes(
                self.example_inputs[1],
                deltaxs
                )
        sgraphs = []
        for i in range(len(slope_vals)):
            sgraphs.append(self.get_graph(lambda x: slope_vals[i][0]*x + slope_vals[i][1], x_min = 1, x_max = deltaxs[i]+1, color = GREEN))
        slope_tex_2 = [TexMobject("gradient\\\=%.1f ~"%i[0]).set_color(GREEN).shift(5*RIGHT) for i in slope_vals]

        self.add(v_lines[0],v_lines[1])
        self.add(sgraphs[0])
        self.add(slope_tex_2[0])
        self.wait(2)
        print("%.1f"%(slope_vals[0][0]))
        for i in range(len(v_lines)-2):
            self.play(
                    AnimationGroup(
                        ReplacementTransform(v_lines[i+1],v_lines[i+2]), 
                        ReplacementTransform(sgraphs[i],sgraphs[i+1]),
                        ReplacementTransform(slope_tex_2[i],slope_tex_2[i+1])
                        )
                    )
            self.wait(1)
        self.remove(slope_tex[-1])
        self.remove(slope_tex_2[-1])
        self.play(Write(TexMobject("\\frac{dy}{dx} = x").shift(5*RIGHT+UP)))
        self.wait(1)
        self.play(Write(TexMobject("\\frac{dy}{dx} = \\frac{1}{x}  ?").shift(5*RIGHT+DOWN)))
        self.play(Write(TexMobject("\\frac{dy}{dx} = y  ?").shift(5*RIGHT+3*DOWN)))
        self.wait(5)

    def get_slopes(self, x_value, deltaxs):
        m = []
        for i in deltaxs:
            if i != x_value:
                dx = i-x_value
                dy = self.func_to_graph(i)-self.func_to_graph(x_value)
                m.append(dy/dx)
            else:
                dx = 0.001
                dy = self.func_to_graph(i+0.001)-self.func_to_graph(i)
                m.append(dy/dx)
        c = []
        for i in m:
            point = self.func_to_graph(x_value)
            c.append(point-(i*x_value))
        return(list(zip(m,c)))
                

    def get_v_lines(self,x_value, deltaxs):
        v_lines = [
                self.get_vertical_line_to_graph(
                    x, self.graph,
                    color=WHITE,
                    )
                for x in ([x_value] + deltaxs.tolist())
                ]
        return v_lines

    def func_to_graph(self, x):
        return (1/2)*x**2



    def sectotan(self):

        v_lines = [
                self.get_vertical_line_to_graph(
                    x, graph,
                    color = WHITE,
                    )
                for x in self.example_inputs
                ]
        height_labels = [
                TexMobject("%.1f"%((x**2)/2)).next_to(vl, RIGHT, SMALL_BUFF)
                    for vl, x in zip(v_lines, self.example_inputs)
                    ]
        slope_labels = [
                TexMobject(
                    "Slope = %d"%x).next_to(vl.get_top(), UP+RIGHT).shift(0.7*RIGHT/x)
                for vl, x in zip(v_lines, self.example_inputs)
                ]
        start_input, target_input = self.example_inputs
        ss_group = self.get_secant_slope_group(
                start_input, graph,
                dx = self.small_dx,
                dx_label = "dx",
                df_label = "\\frac(d(x^2))(2)",
                secant_line_color = YELLOW
                )

        self.play(*list(map(ShowCreation, ss_group)))
        self.play(Write(slope_labels[0]))
        self.play(Write(height_labels[1]))
        self.wait(2)

