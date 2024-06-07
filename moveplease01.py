
#!/usr/bin/env python3

import shutil # imports shuttle util mod


import os # import os module 


os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')


xname = input('What is the new name for kerrigan.obj? ')  # prompts user for a file name. 

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  # rename current file. 



