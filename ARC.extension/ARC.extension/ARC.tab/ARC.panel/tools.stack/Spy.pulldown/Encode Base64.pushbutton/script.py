
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, Form, TextBox, Button
from System.Drawing import Point, Size
import base64

def encode_to_base64(input_string):
    input_bytes = input_string.encode('utf-8')
    base64_bytes = base64.b64encode(input_bytes)
    base64_string = base64_bytes.decode('utf-8')  
    return base64_bytes
class MyForm(Form):
    def __init__(self):
        self.Text = "Encode Base64"
        self.InitializeComponents()

    def InitializeComponents(self):
        self.textBox = TextBox()
        self.textBox.Location = Point(10, 10)
        self.textBox.Size = Size(200, 20)

        self.button = Button()
        self.button.Text = "Submit"
        self.button.Location = Point(10, 40)
        self.button.Click += self.button_Click

        self.Controls.Add(self.textBox)
        self.Controls.Add(self.button)
    def button_Click(self, sender, e):
        text = self.textBox.Text
        output = encode_to_base64(text)
        print output
        self.Close()  
if __name__ == "__main__":
    form = MyForm()
    Application.Run(form)     
