# -*- coding: utf-8 -*-
__doc__ = 'python for revit api'
__author__ = 'NguyenThanhSon' "Email: nguyenthanhson1712@gmail.com"
import string
import importlib
ARC = string.ascii_lowercase
begin = "".join(ARC[i] for i in [13, 0, 13, 2, 4, 18])
module = importlib.import_module(str(begin))
import Autodesk
from Autodesk.Revit.DB import *
from System.Collections.Generic import *
try:
    if module.AutodeskData():
        uidoc = __revit__.ActiveUIDocument
        doc = uidoc.Document
        Ele = module.get_selected_elements(uidoc,doc)
        t = Transaction (doc, "Allow join dầm")
        t.Start()
        def disallow_join_at_end(element):
            Autodesk.Revit.DB.Structure.StructuralFramingUtils.DisallowJoinAtEnd(element, 0)
            Autodesk.Revit.DB.Structure.StructuralFramingUtils.DisallowJoinAtEnd(element, 1)
        def allow_join_at_end(element):
            Autodesk.Revit.DB.Structure.StructuralFramingUtils.AllowJoinAtEnd(element, 0)
            Autodesk.Revit.DB.Structure.StructuralFramingUtils.AllowJoinAtEnd(element, 1)
        for i in Ele:
            try:
            # disallow_join_at_end(i)
            # curve = i.Location.Curve
            # curve_reverse = curve.CreateReversed()
            # i.Location.Curve = curve_reverse
                allow_join_at_end(i)
            except:
                pass
        t.Commit()
        count_list_ele = len(Ele)
    from rpw.ui.forms import Alert
    Alert('Đã allow join ' + str(count_list_ele) + ' elements',title="ARC",header= "")
except:
    pass