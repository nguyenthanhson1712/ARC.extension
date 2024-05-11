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
        import clr
        clr.AddReference('System.Windows.Forms')
        from System.Windows.Forms import MessageBox
        from System.Windows.Forms import MessageBox, MessageBoxButtons, DialogResult, MessageBoxIcon
        import System.Windows.Forms.Clipboard as Clipboard

        check = module.checklicense_for_info()
        if check == 'OK':
            title = "nguyenthanhson1712@gmail.com"
            content = "Successful unlock"

        else:
            title = "nguyenthanhson1712@gmail.com"
            content = "Click button Get info"
        result = MessageBox.Show(content, title, MessageBoxButtons.OK, MessageBoxIcon.Information)
        # Check if the user clicked 'Copy to clipboard'
except:
    pass        
