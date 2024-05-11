
__doc__ = 'python for revit api'
__author__ = 'SonKawamura'
from Autodesk.Revit.UI.Selection.Selection import PickObject
from Autodesk.Revit.UI.Selection  import ObjectType
from Autodesk.Revit.DB import*
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import Element
from System.Collections.Generic import *
import math
from rpw import revit, db, ui
from rpw.ui.forms import Alert
from collections import Counter
#The inputs to this node will be stored as a list in the IN variables.
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
import os
import clr
import os.path as op
import sys

def get_selected_elements():
    selection = uidoc.Selection
    selection_ids = selection.GetElementIds()
    elements = []
    for element_id in selection_ids:
        elements.append(doc.GetElement(element_id))
    return elements
ele = get_selected_elements()
lstpoint = []
listok=[]
listnotok= []
acview= doc.ActiveView
try:
    if len(ele) == 0:
        Alert('You need select all framings need to check',title="Warning",header= "Something wrong")
        Alert("Please select again", exit= True)
    else:
        # Place your code below this line
        t = Transaction(doc, "Check Mirrored Beam")
        t.Start()
        for i in ele:
            # cur = i.Location.Curve.Direction
            # Point1 = i.Location.Curve.GetEndPoint(0)
            # Point2 = i.Location.Curve.GetEndPoint(1)
            # lstpoint.append(Point1)
            # lstpoint.append(Point2)
            is_mirrored = i.Mirrored
            if is_mirrored:
                listnotok.append(i)
            # else:
            #     if abs(cur.X) < abs(cur.Y):
            #         # if Point1.Y < Point2.Y:
            #         if Point1.Y < Point2.Y:
            #             listok.append(i)            
            #         else:
            #             listnotok.append(i)
            #     elif Point1.X < Point2.X:
            #         listok.append(i)
            #     else: 
                    # listnotok.append(i)
        def TempIsolate(view, items):
            ielements = List[ElementId]([x.Id for x in items])
            view.IsolateElementsTemporary(ielements)
        TempIsolate(acview, listnotok)
        t.Commit()
except:
    Alert('Just select framings',title="Warning",header= "Something wrong")
    Alert("Please select again", exit= True)
