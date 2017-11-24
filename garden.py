import string

class Garden():
    
    def __init__(self):
        self.compost = {}
    
    def addCompost(self, task):
        words = task.split()
        for word in words:
            for l in word:
                l = l.lower()
                if l in self.compost:
                    self.compost[l] += 1
                else:
                    self.compost[l] = 1
        # for testing
        for item in self.compost:
            print (item + ' has ' + str(self.compost[item]) + ' units of compost!')

# loadCompost()
# generateGarden()
# etc