# -*- coding: utf-8 -*-
__doc__ = 'nguyenthanhson1712@gmail.com'
__author__ = 'NguyenThanhSon' "Email: nguyenthanhson1712@gmail.com"
import Autodesk
from Autodesk.Revit.UI.Selection.Selection import PickObject
from Autodesk.Revit.UI.Selection  import ObjectType
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FailuresAccessor
from Autodesk.Revit.DB import Line
from Autodesk.Revit.Creation import ItemFactoryBase
from System.Collections.Generic import *
from Autodesk.Revit.DB import Reference
import math
import sys
import string
import importlib
import traceback
from codecs import Codec
import string
import importlib
ARC = string.ascii_lowercase
begin = "".join(ARC[i] for i in [13, 0, 13, 2, 4, 18])
module = importlib.import_module(str(begin))
from pyrevit import framework
from pyrevit import revit, script, DB, UI
from pyrevit import forms
#Get Document 
from Autodesk.Revit.UI.Selection import ObjectType, Selection
if module.AutodeskData():
    uidoc = __revit__.ActiveUIDocument
    doc = uidoc.Document

    def tao_sheet (idoc, id_khung_ban_ve):
        new_sheet = Autodesk.Revit.DB.ViewSheet.Create(idoc,id_khung_ban_ve)
        return new_sheet
    
    def dat_view_vao_sheet (idoc, sheet_id, view_id, point):
        kiem_tra = Autodesk.Revit.DB.Viewport.CanAddViewToSheet(idoc,sheet_id, view_id)
        if kiem_tra:
            new_viewport = Autodesk.Revit.DB.Viewport.Create(idoc, sheet_id, view_id, point)
        return new_viewport
    def lay_khung_ban_ve (viewsheet):
        filter = ElementClassFilter(FamilyInstance)
        get_dependent_element = viewsheet.GetDependentElements(filter)
        return get_dependent_element

    def lay_het_title_block (idoc):
        title_block_collector = FilteredElementCollector(idoc).OfCategory(BuiltInCategory.OST_TitleBlocks).WhereElementIsElementType().ToElements()

    def lay_het_sheet(idoc):
        tat_ca_sheet = collector = FilteredElementCollector(doc).OfClass(ViewSheet)
        # Danh sách chứa tên các loại title block
        return tat_ca_sheet

        # Lặp qua từng title block family và lấy tên các loại
        for title_block in title_block_collector:
            if isinstance(title_block, FamilySymbol):
                title_block_types.append(title_block)
                title_block_family_name.append(title_block.FamilyName)
        return title_block_types, title_block_family_name


    Ele_chua_sort = module.get_selected_elements(uidoc,doc)
    # for tung_element in Ele:
        # name_view = Autodesk.Revit.DB.Element.Name.GetValue(tung_element)
        # Ele.sort(key=lambda name_view: str(name_view))
    # Ele.sort(key=lambda x: x.Name)
    Ele = sorted(Ele_chua_sort, key=lambda x: x.GenLevel)
    # Ele = sorted(Ele_sort_name, key=lambda x: x.GenLevel)
 
    # for test in Ele:
    #     print (Autodesk.Revit.DB.Element.Name.GetValue(test))
    t = Transaction (doc, "Đặt view đã chọn vào sheet có sẵn")
    t.Start()
    # id_khung_ban_ve = ElementId(3025922)
    all_khung_all_family_name = lay_het_title_block(doc)
    all_sheets = lay_het_sheet(doc)
    all_sheets_loc_lai =[]
    list_name_sheet =[]
    for tung_sheet in all_sheets:
        # list_check = []
        # for tung_view in Ele:
        #     kiem_tra_co_bo_tri_sheet_duoc_khong_1 = Autodesk.Revit.DB.Viewport.CanAddViewToSheet(doc,tung_sheet.Id, tung_view.Id)
        #     list_check.append(kiem_tra_co_bo_tri_sheet_duoc_khong_1)
        #     if all(list_check):
                # sheet_number = tung_sheet.SheetNumber
                # name_of_sheet = str(Autodesk.Revit.DB.Element.Name.GetValue(tung_sheet))
                # new_format = str(sheet_number) + ":" + name_of_sheet
                # list_name_sheet.append(new_format)
        sheet_number = tung_sheet.SheetNumber
        name_of_sheet = str(Autodesk.Revit.DB.Element.Name.GetValue(tung_sheet))
        new_format = str(sheet_number) + ":" + name_of_sheet
        list_name_sheet.append(new_format)



    selected_views = forms.select_views(use_selection=True,
            filterfunc=lambda v: not isinstance(v, DB.ViewSheet)
                                or not v.IsPlaceholder)


    from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox,
                                Separator, Button, CheckBox)
    components = [Label('Chọn sheet muốn view thêm vào:'),
                    ComboBox('combobox1', [x for x in list_name_sheet]),
                    # Label('Giá trị Sheet Number đầu tiên (VD: S01-01)'),
                    # TextBox('textbox1', Text="S01-01"),
                #   CheckBox('checkbox1', 'Check this'), (khong can check box)
                    Separator(),
                    Button('Add view vào sheet')]
    form = FlexForm('ARC tools', components)
    form.show()
    # User selects `Opt 1`, types 'Wood' in TextBox, and select Checkbox
    form.values
    selected_sheet= form.values["combobox1"]
    # sheet_number  = form.values["textbox1"]
    for tung_sheet_2 in all_sheets:
        sheet_number_2 = tung_sheet_2.SheetNumber
        name_of_sheet_2 = str(Autodesk.Revit.DB.Element.Name.GetValue(tung_sheet_2))
        new_format_2 = str(sheet_number_2) + ":" + name_of_sheet_2
        if new_format_2 == selected_sheet:
            sheet_da_chon = tung_sheet_2

    for i in Ele:
        kiem_tra_co_bo_tri_sheet_duoc_khong = Autodesk.Revit.DB.Viewport.CanAddViewToSheet(doc,sheet_da_chon.Id, i.Id)
        if kiem_tra_co_bo_tri_sheet_duoc_khong:
            dat_view_vao_sheet(doc,sheet_da_chon.Id,i.Id, XYZ(420.5/304.8,297/304.8,0))
            uidoc.ActiveView = sheet_da_chon
        else:
            module.message_box("View đã có trong sheet khác rồi: " + str(i.Name))
    t.Commit()
