from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image



class calculator(App):
    def build(self):
        self.window =GridLayout()
        self.window.cols=1
        # Add an image
        self.image = Image(source="math.JPG", size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
        self.window.add_widget(self.image)
        self.input_field=TextInput(multiline=False,

                             size_hint=(1,None),
                             font_size=20,
                             readonly=True,
                             height=50,

                             )
        self.window.add_widget(self.input_field)


        button_layout = GridLayout(cols=4)  # Create a 4x4 grid for buttons

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for i in buttons:
            button=Button(
                text=str(i),
                font_size=24,
                size_hint=(1,None),
                height=50,
                background_normal='',
                background_color=(0.2, 0.2, 0.2, 1)


            )
            button.bind(on_press=self.on_button_click)
            button_layout.add_widget(button)

        #Add button laygout to the window
        self.window.add_widget(button_layout)

        return self.window

    def on_button_click(self, instance):
        current_text = self.input_field.text
        i = instance.text

        if i == 'C':
            self.input_field.text = ''  # Clear the input
        elif i == '=':
            try:
                self.input_field.text = str(eval(current_text))  # Calculate the expression
            except:
                self.input_field.text = 'Error'  # In case of error (e.g., division by zero)
        else:
            self.input_field.text += i




if __name__=="__main__":
    calculator().run()







