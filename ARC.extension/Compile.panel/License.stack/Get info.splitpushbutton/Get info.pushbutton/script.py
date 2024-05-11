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
    import clr
    clr.AddReference('System.Windows.Forms')
    from System.Windows.Forms import MessageBox
    from System.Windows.Forms import MessageBox, MessageBoxButtons, DialogResult, MessageBoxIcon
    import System.Windows.Forms.Clipboard as Clipboard

    newma = module.machine_code()
    if module.checklicense_for_info() == "OK":
        title = "ARC"
        content = "This Add-in work fine"
    else:
        title = "ARC: Click OK to copy the code to Clip board"
        content = newma



    # Show the message box with custom buttons and an icon
    result = MessageBox.Show(content, title, MessageBoxButtons.OKCancel, MessageBoxIcon.Information)

    # Check if the user clicked 'Copy to clipboard'
    if result == DialogResult.OK:
        # Copy the message to clipboard
        Clipboard.SetText(content)
        if module.checklicense_for_info() != "OK":
            MessageBox.Show("Code has been copied to clipboard", "ARC")


except:
    pass      
