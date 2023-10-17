import math
import numpy

def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r>0 and h>0:
        return h*math.pi*2*r + 2*math.pi*r*r
    return math.nan

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if type(n) is not int:
        return None
    if n ==1:
        return [1]
    if n >0:
        vector = numpy.ndarray(shape = (n), dtype=int)
        vector[0], vector[1] = 1, 1
        for i in range(n-2):
            vector[i+2] = vector[i+1] + vector[i]
        return [vector]
    return None

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    matrix = numpy.array([[a, 1.0, -a], [0.0, 1.0, 1.0], [-a, a ,1.0]])
    Mdet = numpy.linalg.det(matrix)
    Minv = numpy.linalg.inv(matrix )if Mdet !=0 else math.nan
    Mt = numpy.transpose(matrix)
    return (Minv, Mt, Mdet)

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania  7.
    """
    if m<0 or n<0 or type(n)!=int or type(m)!=int:
        return None
    matrix = numpy.zeros([m,n])
    for i in range(m):
        for j in range(n):
            matrix[i,j] = i if i>j else j
    return matrix
