
class Binary:
    def __init__(self,list,target):
        self.list = list 
        self.target = target 
    
    def search(self):
        left = 0
        right = len(self.list) - 1
        while left <= right:
            mid = (left + right) // 2
            guess = self.list[mid]
            if guess == self.target:
                return "yes"
            if guess > self.target:
                right = mid-1
            else:
                left = mid + 1
        return None  
l = [2,3,4,10,12,13,100,101]     
b = Binary(l,10)
print(b.search()) 


