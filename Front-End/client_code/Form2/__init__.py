from ._anvil_designer import Form2Template
from anvil import *
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('explanation_techniques_used')
    self.generated_explanation_copy.visible = True
    self.generated_explanation_copy.text = result

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home')


