import maya.utils

# Load Mech Rig Custom Shelf at Maya startup
from mechRig_toolkit.shelves import shelf_mechRig_utils

def load_mechRig_shelf():
	shelf_mechRig_utils.load(name="MechRig_utils")
	
maya.utils.executeDeferred("load_mechRig_shelf()")