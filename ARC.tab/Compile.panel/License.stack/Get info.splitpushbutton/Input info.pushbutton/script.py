import pickle
import os.path as op
import os
import pyrevit
from pyrevit import coreutils
from pyrevit import revit
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox, MessageBoxButtons
clr.AddReference("System.Drawing")
from System.Windows.Forms import *
from System.Drawing import *
PYREVIT_ADDON_NAME = 'pyRevit'
PYREVIT_FILE_PREFIX = '{}_'.format(PYREVIT_ADDON_NAME)
USER_ROAMING_DIR = os.getenv('appdata')
PYREVIT_APP_DIR = op.join(USER_ROAMING_DIR, PYREVIT_ADDON_NAME)
PYREVIT_VERSION_APP_DIR = op.join(PYREVIT_APP_DIR)

def _get_app_file(file_id, file_ext,
                  filename_only=False, stamped=False, universal=False):
    appdata_folder = PYREVIT_VERSION_APP_DIR
    file_prefix = PYREVIT_FILE_PREFIX
    # print (PYREVIT_VERSION_APP_DIR)
    
    if stamped:
        file_prefix = pyrevit.PYREVIT_FILE_PREFIX_STAMPED
    elif universal:
        appdata_folder = PYREVIT_APP_DIR
        file_prefix = pyrevit.PYREVIT_FILE_PREFIX_UNIVERSAL

    full_filename = '{}{}.{}'.format(file_prefix, file_id, file_ext)
    # print (file_id)
    if filename_only:
        return full_filename
    else:
        return op.join(
            appdata_folder,
            coreutils.cleanup_filename(full_filename)
            )



def get_data_file(file_id, file_ext, name_only=False):
    return _get_app_file(file_id, file_ext, filename_only=name_only)




def get_document_data_file(file_id, file_ext, add_cmd_name=False):
    proj_info = revit.query.get_project_info()
    # print (proj_info)
    if add_cmd_name:
        script_file_id = '{}_{}'.format(EXEC_PARAMS.command_name,
                                           file_id)
    else:
        script_file_id = '{}'.format(file_id)
    return get_data_file(script_file_id, file_ext)
    
datafile = get_document_data_file("pyrevit", "dll")

from rpw.ui.forms import TextInput
input = TextInput('Please enter the code', default="")
f = open(datafile, 'w')
pickle.dump(input, f)
f.close()

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
        check = module.checklicense_for_info()
        if check == 'OK':
            result = MessageBox.Show("Unlocked successfully", "ARC", MessageBoxButtons.OK, MessageBoxIcon.Information)
except:
    pass    

