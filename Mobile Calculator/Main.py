from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Mainapp(App):
    def build(self): #designing the constractor
        self.operators = ["/","+","*","-"] # initialising the operators inside a variable
        self.last_was_operator = None #defining a variable
        self.last_button= None  #defining a variable

        main_layout = BoxLayout(orientation = "vertical")
        #creating an interface with text input and then desisgning that text input
        self.solution = TextInput(background_color = "black",foreground_color = "white" , multiline = False , halign = "right" ,font_size = 55 , readonly = True)
        #adding the screen into main_layout
        main_layout.add_widget(self.solution)
        #creating button
        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","+"],
            [".","0","c","-"],
        ]
#arranging thebuttons in a boxlayout
        for row in buttons:
            h_layout = BoxLayout()
#intergrating buttons with labels and then designing them into a more attractive aperiance             
            for Label in row:
                button = Button(
                    text = Label ,font_size = 30 , background_color = "grey",
                    pos_hint = {"center_x":0.5, "center_y":0.5},
                )
#adding the buttons inside the layout
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
  #every time we press the = button we run a function      
        equal_button = Button(
            text = "=", font_size = 30 , background_color = "grey",
            pos_hint = {"center_x":0.5, "center_y":0.5}
        )
        equal_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_button)
        return main_layout

    def on_button_press(self,instance):
        #arranging for the values to show on the screen when one press a button 
        current = self.solution.text
        button_text = instance.text

        #arranging for the clear button to start working
        if button_text == "c":
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current ==""and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self,instance):
            text= self.solution.text
            if text:
                solution = str(eval(self.solution.text))  
                self.solution.text = solution


    



#if __name__ == "__main__":
 #   app = Mainapp()
  #  app.run()



Mainapp().run()
