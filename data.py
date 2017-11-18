#     def __init__(self, label, priority=1, isChecked=False, tags=[]):

def checkFile(fname):
    importTaskList = []
    try:
        with open(fname, 'r') as taskFile:
            for task in taskFile:
                importTaskList.append(task.split(','))
    except:
        # test dummy data
        # to do: rewrite parameters in Pythonic params pattern
        # (need to figure out how to do this!)
        importTaskList.append(["Write a Python program"])
        importTaskList.append(["Visit Ithaca"])
        importTaskList.append(["Eat a buritooooooo"])
    
    return importTaskList

# add writeFile() function to save To Do items before close