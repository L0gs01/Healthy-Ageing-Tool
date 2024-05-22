from ._anvil_designer import Population_ViewSelectionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.designer import in_designer



class Population_ViewSelection(Population_ViewSelectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.pop_repeating_panel.items = app_tables.pop_info.search()

