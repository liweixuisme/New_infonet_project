import os
def new_report(testreport):
 lists=os.listdir(testreport)
 lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
 file_new=os.path.join(testreport,lists[-1])
 print(file_new)
 return file_new

new_report()