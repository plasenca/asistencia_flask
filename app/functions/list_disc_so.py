import win32api
driveslist = win32api.GetLogicalDriveStrings()
print(driveslist.split('\000')[:-1])

#TODO: Create a function to get the drives list.