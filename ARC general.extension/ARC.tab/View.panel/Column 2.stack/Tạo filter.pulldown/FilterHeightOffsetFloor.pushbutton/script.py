import clr
clr.AddReference("System")
from System import Array
import System
import sys
from System.Drawing import Size, Color, Font, FontStyle
from System import Drawing
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox, Form, CheckedListBox, Button, TextBox, Label, Panel, ComboBox
from System.Collections.Generic import List
import Autodesk
from Autodesk.Revit import DB
from Autodesk.Revit.DB import FilteredElementCollector, Transaction, BuiltInParameter, BuiltInCategory, WallType, CeilingType, FloorType, ElementId, FilterRule, ParameterFilterElement, ElementParameterFilter, ParameterFilterRuleFactory
# try:
#     from Autodesk.Revit.DB import ForgeTypeId
# except:
#     print "Only avalable from version 2021.1"
#     sys.exit()
import Autodesk.Revit.UI.Selection
uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document
import sys
import string
import importlib
ARC = string.ascii_lowercase
begin = "".join(ARC[i] for i in [13, 0, 13, 2, 4, 18])
module = importlib.import_module(str(begin))
if module.AutodeskData():
    t = Transaction (doc, "Create filter: Height offset Floor")
    t.Start()
    def all_type (ofClass, string_OST):
        all_OST_type = FilteredElementCollector(doc).OfClass(ofClass).OfCategory(string_OST)
        return all_OST_type


    collector_floor = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType()
    collector_floor.ToElements()
    list_floorS = []
    list_type = all_type(FloorType, BuiltInCategory.OST_Floors)

    def get_builtin_parameter_by_name(element, built_in_parameter):
        param = element.get_Parameter(built_in_parameter)
        return param    

    for i in collector_floor:
        isstruc = module.get_builtin_parameter_by_name(i, BuiltInParameter.FLOOR_PARAM_IS_STRUCTURAL)
        if isstruc.AsInteger() == 1:
            list_floorS.append(i)

    height_offset = []
    for i in list_floorS:
        parameter_floor_height = module.get_builtin_parameter_by_name(i, BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM)
        value_height_offset = parameter_floor_height.AsValueString()
        height_offset.append(str(value_height_offset))
    for i in height_offset:
        unique_height_offset = list(set(height_offset))
        unique_height_offset.sort(key=lambda x: float(x))
    class MyForm(Form):
        def __init__(self):
            self.Text = "ARC"
            self.ShowIcon = False  #An icon nho
            self.Size = Size(520, 500)

            # Create a CheckedListBox to display the list
            self.checkedListBox = CheckedListBox()
            # items = Array[object](i for i in list_ceiling )
            items = Array[object](list(unique_height_offset))
            self.checkedListBox.Items.AddRange(items)
            self.checkedListBox.Size = Size(400, 300)
            self.checkedListBox.CheckOnClick = True
            self.checkedListBox.Location = Drawing.Point(10, 50)

            self.label1 = Label()
            self.label1.Text = "Prefix"
            self.label1.Location = Drawing.Point(10, 5)

            self.textBox_1 = TextBox()
            self.textBox_1.Location = Drawing.Point(10, 20)
            self.textBox_1.Size = Size(250, 20)
            self.textBox_1.Text = "FloorS_height_e_"

            self.label2 = Label()
            self.label2.Text = "Suffix"
            self.label2.Location = Drawing.Point(360, 5)

            self.typeNameLabel = Label()
            self.typeNameLabel.Text = "height offset"
            self.typeNameLabel.Location = Drawing.Point(275, 22)
            self.typeNameLabel.AutoSize = True
            self.typeNameLabel.ForeColor = Color.Gray
            self.typeNameLabel.Font = Font(self.typeNameLabel.Font, FontStyle.Bold)



            self.typeNamePanel = Panel()
            self.typeNamePanel.Location = Drawing.Point(270, 20)
            self.typeNamePanel.Size = Size(80, 20)
            self.typeNamePanel.BackColor = Color.Transparent
            self.typeNamePanel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle


            self.textBox_2 = TextBox()
            self.textBox_2.Location = Drawing.Point(360, 20)
            self.textBox_2.Size = Size(50, 20)
            self.textBox_2.Text = "_kw"


            self.selectAllButton = Button()
            self.selectAllButton.Text = "Select All"
            self.selectAllButton.Location = Drawing.Point(420, 50)
            self.selectAllButton.Click += self.on_select_all_button_click

            self.nonebutton = Button()
            self.nonebutton.Text = "None"
            self.nonebutton.Location = Drawing.Point(420, 80)
            self.nonebutton.Click += self.on_none_click

            self.signatureLabel = Label()
            self.signatureLabel.Text = "nguyenthanhson1712@gmail.com"
            self.signatureLabel.Size = Size(485, 20)
            self.signatureLabel.Location = Drawing.Point(320, 440)



            # Ham nay de chon tat ca type tuong khi hien windowform
            default_checked = Array[object](list(unique_height_offset))
            for item in default_checked:
                index = self.checkedListBox.FindStringExact(item)
                if index != -1:
                    self.checkedListBox.SetItemChecked(index, False)

            # self.checkedListBox.ItemCheck += self.on_item_check
            self.printButton = Button()
            self.printButton.Text = "Create filter"
            self.printButton.Location = Drawing.Point(420, 400)
            self.printButton.Click += self.on_print_button_click
            # Add the CheckedListBox to the Form
            self.Controls.Add(self.checkedListBox)
            self.Controls.Add(self.printButton)
            self.Controls.Add(self.textBox_1)
            self.Controls.Add(self.textBox_2)
            self.Controls.Add(self.selectAllButton)
            self.Controls.Add(self.nonebutton)
            self.Controls.Add(self.signatureLabel)
            self.Controls.Add(self.label1)
            self.Controls.Add(self.label2)
            self.Controls.Add(self.typeNameLabel)
            self.Controls.Add(self.typeNamePanel)

        def on_select_all_button_click(self, sender, e):
            for i in range(self.checkedListBox.Items.Count):
                self.checkedListBox.SetItemChecked(i, True)

        def on_none_click(self, sender, e):
            for i in range(self.checkedListBox.Items.Count):
                self.checkedListBox.SetItemChecked(i, False)

        def on_item_check(self, sender, e):
            checked_items = [self.checkedListBox.GetItemText(item) for item in self.checkedListBox.CheckedItems]
            print("Checked items:", checked_items)

        def on_print_button_click(self, sender, e):
            checked_items = [self.checkedListBox.GetItemText(item) for item in self.checkedListBox.CheckedItems]
            category = List[ElementId]()
            category.Add(ElementId(BuiltInCategory.OST_Floors))
            sym_name_param = ElementId(BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM)
            list_floorS_tem = []
            count = []  
            for i in list_floorS:
                list_floorS_tem.append(i)
            for i_height in checked_items:
                for floor in list_floorS_tem:
                    rules = List[FilterRule]()
                    # floor_height = floor.GetParameter(ForgeTypeId('autodesk.revit.parameter:floorHeightabovelevelParam-1.0.0')).AsValueString()
                    floor_height = module.get_builtin_parameter_by_name(floor, BuiltInParameter.FLOOR_HEIGHTABOVELEVEL_PARAM).AsValueString()
                    try:
                        if float(i_height) == float(floor_height):
                            new_name = str(self.textBox_1.Text) + i_height + str(self.textBox_2.Text) 
                            rules.Add(ParameterFilterRuleFactory.CreateEqualsRule(sym_name_param, float(floor_height)/304.8, False)) #Doi don vi sang feet
                            pfilter = ElementParameterFilter(rules, False)
                            filters_and = List[DB.ElementFilter]()
                            filters_and.Add(pfilter)
                            rule_set_and = DB.LogicalAndFilter(filters_and)
                            filter = ParameterFilterElement.Create(doc, new_name, category, rule_set_and)
                            # filter = ParameterFilterElement.Create(doc, new_name, category, pfilter)
                            count.append(filter)
                            index = list_floorS_tem.index(floor)
                            list_floorS_tem.pop(index)
                    except:
                        pass
            self.Close()
            filter_count = len(count)
            MessageBox.Show(str(filter_count) + " filters created")
    form = MyForm()
    # Run the application
    form.ShowDialog()
    t.Commit() 
