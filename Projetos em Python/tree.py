# coding: utf-8
import os
 
prefix = u"└── "
prefix_subitem = u"│   └── "
 
dir_items = os.listdir('.')
dir_items.sort()
 
total_files = 0
total_dirs = 0
 
for item in dir_items:
    if not item.startswith("."):
        print(prefix + item)
        if os.path.isdir(item):
           total_dirs += 1
           subdir_items = os.listdir(item)
           for subitem in subdir_items:
               total_files += 1
               print(prefix_subitem + subitem)
        else:
            total_files += 1
 
print("{0} directory, {1} files".format(total_dirs, total_files))