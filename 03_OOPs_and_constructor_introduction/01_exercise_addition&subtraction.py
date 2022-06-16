class calculate:
    def add(self, x, y):
        return x+y
    
    def subtract(self,x,y):
        return x-y

problem1 = calculate()
problem1.x = 56
problem1.y = 69

print(problem1.add(problem1.x, problem1.y ))
print(problem1.subtract(problem1.x, problem1.y ))