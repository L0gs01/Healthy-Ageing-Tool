from ._anvil_designer import Individual_InitialSelectionTemplate
from anvil import *

class Individual_InitialSelection(Individual_InitialSelectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
