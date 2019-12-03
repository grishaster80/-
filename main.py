import math

# Уравнение -> ax^3 + bx^2 + cx + d = 0

def solve(a, b, c, d):
    if (a == 0 and b == 0):                     #Линейное уравнение
        return [(-d * 1.0) / c]              
    elif (a == 0):                              #Квадратное уравнение
        D = c * c - 4.0 * b * d                       
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)      
        return [x1, x2]             # Returning Quadratic Roots as numpy array.
    f = findF(a, b, c)                          # Переменная f - описана в статье
    g = findG(a, b, c, d)                       # Переменная g - описана в статье
    h = findH(g, f)                             # Переменная h - описана в статье
    if f == 0 and g == 0 and h == 0:            # Случай, когда все 3 корня равны
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return [x, x, x]  
    elif h <= 0:                                # Случай, когда существуют все 3 корня
        i = math.sqrt(((g ** 2.0) / 4.0) - h)   # проводим вычисления в соответствии с статьей
        j = i ** (1 / 3.0)                      
        k = math.acos(-(g / (2 * i)))           
        L = j * -1                              
        M = math.cos(k / 3.0)                   
        N = math.sqrt(3) * math.sin(k / 3.0)    
        P = (b / (3.0 * a)) * -1                
        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P
        return [x1, x2, x3]      
    elif h > 0:                                 #Один действительный и два комплексных корня, вычисляем и возвращаем только действительный
        R = -(g / 2.0) + math.sqrt(h)          
        if R >= 0:
            S = R ** (1 / 3.0)                  
        else:
            S = (-R) ** (1 / 3.0) * -1          
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))               
        else:
            U = ((-T) ** (1 / 3.0)) * -1        
        x1 = (S + U) - (b / (3.0 * a))
        return [x1]        # Возвращаем действительный корень.
# вычисляем f.
def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0


# вычисляем  g.
def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a **2.0)) + (27.0 * d / a)) /27.0


# вычисляем h.
def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)

print(solve(2,5,1,2))
