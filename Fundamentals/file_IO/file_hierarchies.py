import os

# make a sub-directory within current directory scope
os.mkdir('./file_hierarchies_dir')

# make several sub-directories inside the above directory
os.mkdir('./file_hierarchies_dir/dir1')
os.mkdir('./file_hierarchies_dir/dir2')
os.mkdir('./file_hierarchies_dir/dir3')

# to delete the directory trees, you cannot directly remove the root "file_hierarchies_dir"
# the valid way is to first remove the leaves "dir1 - 3" and then the root "file_hierarchies_dir"
os.removedirs('./file_hierarchies_dir/dir1')
os.removedirs('./file_hierarchies_dir/dir2')
os.removedirs('./file_hierarchies_dir/dir3')

# actually, if the file_hierarchies is null, the previous command will remove the root automatically