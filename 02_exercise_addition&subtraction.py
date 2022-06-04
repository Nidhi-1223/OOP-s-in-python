# class calculate:
#     def __init__(self,x,y) :
#         self.x = x
#         self.y = y
    
#     def add(self, x, y):
#         return x+y
    
#     def subtract(self, x, y):
#         return x-y

# problem1 = calculate(56, 69)
# print(problem1.add(problem1.x, problem1.y))

# # problem1 = calculate()
# # print(problem1.add)                   gonna throw an error

# problem2 = calculate(78,90)
# print(problem2.subtract(problem2.x, problem2.y))


#############################   METHOD 2 - THE CORRECT METHOD   ####################################################

class calculate:
    def __init__(self,x:int,y:int) :

        assert x >= 0
        assert y >= 0

        self.x = x
        self.y = y
    
    def add(self):
        return self.x+self.y
    
    def subtract(self):
        return self.x-self.y

problem1 = calculate(56, 69)
print(problem1.add())

# problem1 = calculate()
# print(problem1.add)                   gonna throw an error

problem2 = calculate(78,90)
print(problem2.subtract())