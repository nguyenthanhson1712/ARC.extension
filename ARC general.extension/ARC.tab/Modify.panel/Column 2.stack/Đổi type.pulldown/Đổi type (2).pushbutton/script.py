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
        import pickle
        from pyrevit.coreutils import appdata
        from pyrevit.framework import List
        from pyrevit import revit, DB
        def get_document_data_file(file_id, file_ext, add_cmd_name=False):
            proj_info = revit.query.get_project_info()

            if add_cmd_name:
                script_file_id = '{}_{}_{}'.format(EXEC_PARAMS.command_name,
                                                file_id,
                                                proj_info.filename
                                                or proj_info.name)
            else:
                script_file_id = '{}_{}'.format(file_id,
                                                proj_info.filename
                                                or proj_info.name)

            return appdata.get_data_file(script_file_id, file_ext)
        datafile = get_document_data_file("Remember_type_2", "txt")
        selection = revit.get_selection()
        try:
            f = open(datafile, 'r')
            current_selection = pickle.load(f)
            f.close()
            element_ids = []
            for elid in current_selection:
                element_ids.append(DB.ElementId(int(elid)))
        except Exception:
            pass    


    uidoc = __revit__.ActiveUIDocument
    doc = uidoc.Document
    def ChangeType(element, typeId):
        try:
            element.ChangeTypeId(typeId)
            return element
        except:
            pass
    def get_selected_elements():
        selection = uidoc.Selection
        selection_ids = selection.GetElementIds()
        elements = []
        for element_id in selection_ids:
            elements.append(doc.GetElement(element_id))
        return elements
    try:
        Ele = get_selected_elements()
        t = Transaction (doc, "Change type 2")
        t.Start()
        for i in Ele:
            ChangeType(i, element_ids[0])
        t.Commit()
    except:
        pass
except:
    pass