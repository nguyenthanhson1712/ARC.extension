
import string
import importlib
#Get UIDocument

ARC = string.ascii_lowercase
begin = "".join(ARC[i] for i in [13, 0, 13, 2, 4, 18])
module = importlib.import_module(str(begin))
import Autodesk
from Autodesk.Revit.DB import *
from System.Collections.Generic import *
if module.AutodeskData():
    uidoc = __revit__.ActiveUIDocument
    doc = uidoc.Document
    currentview = doc.ActiveView
    
    t = Transaction (doc, "Get Floor's Boundary")
    t.Start()
    Ele = module.get_selected_elements(uidoc,doc)
    select = uidoc.Selection
    detailline= []
#Choose ref of floor, now is choosing Topface
    # for a in Ele:
    a = Ele[0]
    ref = HostObjectUtils.GetTopFaces(a)
    # new_ref = module.flatten_list(ref)
    for i in ref:
        boundaryloops = a.GetGeometryObjectFromReference(i).GetEdgesAsCurveLoops()
        for loop in boundaryloops:   
            sketchloop = []
            sketchloop.append([x for x in loop])
            for a1 in sketchloop:
                for a2 in a1:
                    #need to change to line in plan view because some floor is not on a plane.
                    Startpoint = a2.GetEndPoint(0)
                    Endpoint = a2.GetEndPoint(1)
                    PlaPoint1 = XYZ(Startpoint.X, Startpoint.Y, 0)
                    PlaPoint2 = XYZ(Endpoint.X, Endpoint.Y, 0)
                    L1 = Line.CreateBound(PlaPoint1,PlaPoint2)
                    detailline.append(doc.Create.NewDetailCurve(currentview,L1))
    t.Commit()
    listid = []
    for seg in detailline:
        segid = seg.Id
        listid.append(segid)
    Icollection = List[ElementId](listid)
    select.SetElementIds(Icollection)


    