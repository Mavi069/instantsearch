from ._anvil_designer import RegisterTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Register(RegisterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1
    gmail = self.text_box_2
    username = self.text_box_3
    propic = self.file_loader_1
    anvil.server.call('submit', name=name, gmail=gmail, username=username, propic=propic)
    Notification("Registered").show()
    open_form('Register.Discover')
    
