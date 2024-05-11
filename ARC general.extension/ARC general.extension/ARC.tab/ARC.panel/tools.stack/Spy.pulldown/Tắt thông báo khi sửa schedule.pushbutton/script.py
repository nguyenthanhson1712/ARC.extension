# -*- coding: utf-8 -*-
from Autodesk.Revit.UI import UIApplication, TaskDialogCommonButtons
from pyrevit import script
import Autodesk
import sys
# from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox,
#                             Separator, Button, CheckBox)
# components = [Label('Nhập Ok hoặc Cancel'),
#                 TextBox('textbox1', Text="Ok."),
#             #   CheckBox('checkbox1', 'Check this'), (khong can check box)
#                 Separator(),
#                 Button('Ok')]
# form = FlexForm('ARC tools', components)
# form.show()
# form.values
# out_put = str(form.values["textbox1"])

doc = __revit__.ActiveUIDocument.Document
app = doc.Application
uiapp = UIApplication(app)
def register_warning_suppression():

    uiapp.DialogBoxShowing += dismiss_task_dialog

def dismiss_task_dialog(sender, args):
    e = args
    # print e.Message
    if not e or not isinstance(e, Autodesk.Revit.UI.Events.TaskDialogShowingEventArgs):
        return
    if e.Message.startswith("This change will be applied to all elements of type"):
        e.OverrideResult(int(TaskDialogCommonButtons.Ok))
register_warning_suppression()



