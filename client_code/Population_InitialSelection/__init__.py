from ._anvil_designer import Population_InitialSelectionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Population_InitialSelection(Population_InitialSelectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    global pop_selection
    # Any code you write here will run before the form opens.

  # def slider__change(self, **event_args):
  #   """This method is called when the slider is moved"""
  #   self.label_20.text = self.slider_20.level

  def percent_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.percent_label.text = self.percent_slider.level

  # def save_btn_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   global textbox_6_end
  #   textbox_6_end = (int(self.textbox_6.text)*4)
  #   global pop_selection
  #   pop_selection = {self.textbox_6.text,
  #                    self.slider_7.level,
  #                    self.slider_8.level,
  #                    self.slider_9.level,
  #                    self.dropdown_10.selected_value}
    
  # def show_btn_click(self, **event_args):
  #   """This method is called when the button is clicked"""
    
  #   print(pop_selection)
  #   print(textbox_6_end)

  



 
