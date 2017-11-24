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
        self.animateGarden()
    
    def animateGarden(self):
        for item in self.compost:
            print (item + ': ' + '*'*self.compost[item])

# loadCompost()
# generateGarden()
# etc