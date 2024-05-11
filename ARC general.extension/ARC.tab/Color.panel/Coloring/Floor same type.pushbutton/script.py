__doc__ = 'python for revit api'
__author__ = 'SonKawamura'
from Autodesk.Revit.DB import (Transaction, FilteredElementCollector,
                                Element, View, ElementId, FamilyInstance, 
                                FillPatternElement, Color, OverrideGraphicSettings,FilteredElementCollector, BuiltInCategory)
from Autodesk.Revit.UI import UIDocument, Selection
from Autodesk.Revit.UI.Selection.Selection import PickObject 
from Autodesk.Revit.UI.Selection import ObjectType
import random
# Get UIDocument
uidoc = __revit__.ActiveUIDocument

# Get Document 
doc = uidoc.Document

# Get the active view of the current document
view = doc.ActiveView
#Overrides in view
# Set Color
Red = Color(165,42,42)
Green_1 = Color(127,255,212)
Green_2 = Color(64,224,208)
Purple = Color(221,160,221)
Green_3 = Color(127,255,0)
Pink = Color(255,192,203)
Orange = Color (255, 99, 71)
Yellow = Color (255,255,0)
Cream = Color (245, 222, 179)
Blue_1 = Color (70, 130, 180)
Blue_2 = Color (176, 196, 222)
Blue_3 = Color (25, 25, 112)
color_ele_base = [Red, Green_1, Green_2, Green_3,Purple, Pink, Orange, Yellow, Cream, Blue_1, Blue_2, Blue_3]
# Set Fill Pattern
name_pattern = "<Solid fill>"
patterns = FilteredElementCollector(doc).OfClass(FillPatternElement)
t = Transaction(doc,"Coloring floor same type")
t.Start()
for pattern in patterns:
    if pattern.Name == name_pattern:
        solidPatternId = pattern.Id
override = OverrideGraphicSettings()
# Sets the projection surface fill color
#override.SetSurfaceForegroundPatternColor(color_ele[0])
# Sets the projection surface fill pattern
#override.SetSurfaceForegroundPatternId(solidPatternId)
def all_elements_of_category(category):
	return FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElements()
#All Elements Of beam Category.
Beam = all_elements_of_category(BuiltInCategory.OST_Floors)
TypeBeam = []
for i in Beam:
    TypeId = i.GetTypeId()
    TypeBeam.append(TypeId)
#Remove duplicate in list TypeBeam
Remove_duplicate_TypeBeam = list(dict.fromkeys(TypeBeam))
Same_type = []
Range =[]
New_beam = []
List_tong = []
for i in Beam:
    New_beam.Add(i)
x = (len (Remove_duplicate_TypeBeam)/ len (color_ele_base))
y = int (round (x) + 1 )
color_ele = color_ele_base * y
for a in Remove_duplicate_TypeBeam:
    j = Remove_duplicate_TypeBeam.index(a)
    # if j > (len ((color_ele))-1):
    #     j = random.choice(range(0, len(color_ele)))
    for b in New_beam:
        if b.GetTypeId() == a:
            Same_type.append (b)
            override.SetSurfaceForegroundPatternColor(color_ele[j])
            override.SetSurfaceForegroundPatternId(solidPatternId)
            view.SetElementOverrides(b.Id, override)
    Same_type.Clear
t.Commit()