__doc__ = 'python for revit api'
__author__ = 'NguyenThanhSon' "Email: nguyenthanhson1712@gmail.com"
import string
import importlib
try:
    ARC = string.ascii_lowercase
    begin = "".join(ARC[i] for i in [13, 0, 13, 2, 4, 18])
    module = importlib.import_module(str(begin))
    import Autodesk
    from Autodesk.Revit.DB import *
    from System.Collections.Generic import *
    if module.AutodeskData():
        import Autodesk
        from Autodesk.Revit.DB import *
        from Autodesk.Revit.UI.Selection.Selection import PickObject
        from Autodesk.Revit.UI.Selection  import ObjectType
        from Autodesk.Revit.DB import Element
        from System.Collections.Generic import *
        #Get UIDocument
        uidoc = __revit__.ActiveUIDocument
        doc = uidoc.Document
        AcView= module.Active_view(doc)
        ids = List[ElementId]()
        wall = []
        collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType()
        collector.ToElements()
        listfloorA = []
        for i in collector:
            isstruc_floor = module.get_builtin_parameter_by_name(i, BuiltInParameter.FLOOR_PARAM_IS_STRUCTURAL)
            if isstruc_floor.AsInteger() == 0:
                listfloorA.append(i)
        t = Transaction(doc, "Hide floorA")
        t.Start()
        for floorA in listfloorA:
            is_hidden = floorA.IsHidden(AcView)
            if is_hidden:
                hide_element = AcView.UnhideElements(List[ElementId]([floorA.Id]))
            else:
                unhide_element = AcView.HideElements(List[ElementId]([floorA.Id]))
        t.Commit()
except:
    pass        
