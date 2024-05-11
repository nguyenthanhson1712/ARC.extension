
# -*- coding: utf-8 -*-
import os
import re

path = "C:\\Users\\ADMIN\\AppData\\Roaming\\pyRevit-Master\\extensions\\pyRevitCore.extension\\ARC.tab"

# Lấy tất cả các thư mục trong đường dẫn
folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

# Lọc ra các thư mục bắt đầu bằng "Version."
version_folders = [folder for folder in folders if folder.startswith("Version.")]

# Lấy thông tin số từ mỗi thư mục
version_numbers = [re.search(r'\d+', folder.split("Version.")[1]).group() for folder in version_folders]

# In tất cả các số
print("Thông tin số từ các thư mục bắt đầu bằng 'Version.':")
for version_number in version_numbers:
    print(version_number)


import webbrowser

url = "https://github.com/nguyenthanhson1712/ARC/blob/main/Version"

# Mở trình duyệt mặc định và mở trang web GitHub
webbrowser.open(url)
