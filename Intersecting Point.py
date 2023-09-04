"""
Khanh Vu
Intersecting Points (with classes) program
"""
class LinearEquations:
    
    def __init__(self, point1, point2, point3, point4):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3
        self.__point4 = point4
    
    def __calculate_a(self):
        return self.__point1[1] - self.__point2[1]
    
    def __calculate_b(self):
        return -(self.__point1[0] - self.__point2[0])
    
    def __calculate_c(self):
        return self.__point3[1] - self.__point4[1]
    
    def __calculate_d(self):
        return -(self.__point3[0] - self.__point4[0])
    
    def __calculate_e(self):
        return (self.__point1[1] - self.__point2[1]) * self.__point1[0] - (self.__point1[0] - self.__point2[0]) * self.__point1[1]
    
    def __calculate_f(self):
        return (self.__point3[1] - self.__point4[1]) * self.__point3[0] - (self.__point3[0] - self.__point4[0]) * self.__point3[1]
    
    def __str__(self):
        return f'{self.__calculate_a()}x + {self.__calculate_b()}y = {self.__calculate_e()}\n{self.__calculate_c()}x + {self.__calculate_d()}y = {self.__calculate_f()}'
    
    def is_solvable(self):
        return self.__calculate_a() * self.__calculate_d() - self.__calculate_b() * self.__calculate_c() != 0
    
    def intersecting_point(self):
        if self.is_solvable():
            x = (self.__calculate_e() * self.__calculate_d() - self.__calculate_b() * self.__calculate_f()) / (self.__calculate_a() * self.__calculate_d() - self.__calculate_b() * self.__calculate_c())
            y = (self.__calculate_a() * self.__calculate_f() - self.__calculate_e() * self.__calculate_c()) / (self.__calculate_a() * self.__calculate_d() - self.__calculate_b() * self.__calculate_c())
            return round(x, 1), round(y, 1)
        else:
            return None
def main():
    point1 = tuple(map(float, input('Enter point 1 (x,y): ').split(' ')))
    point2 = tuple(map(float, input('Enter point 2 (x,y): ').split(' ')))
    point3 = tuple(map(float, input('Enter point 3 (x,y): ').split(' ')))
    point4 = tuple(map(float, input('Enter point 4 (x,y): ').split(' ')))
    
    linear_equations = LinearEquations(point1, point2, point3, point4)
    #print(f'The equation of the first
    if linear_equations.is_solvable():
        print('The intersecting point is:', linear_equations.intersecting_point())
    else:
        print('There is no intersection.')

if __name__ == '__main__':
    main()
