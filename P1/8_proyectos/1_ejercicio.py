
# class Calculadora():
#     def __init__(self,num1,num2):
#         self.num1=int(input("Valor 1: "))
#         self.num2=int(input("Valor 2: "))
        
#     def suma(self):
#         resultado=self.num1 + self.num2    
#         return f"El resultado de la suma es: {resultado}"
    
#     def suma(self):
#         resultado=self.num1 + self.num2    
#         return f"El resultado de la suma es: {resultado}"
    
#     def resta(self):
#         resultado=self.num1 - self.num2    
#         return f"El resultado de la resta es: {resultado}"
    
#     def multi(self):
#         resultado=self.num1 * self.num2    
#         return f"El resultado de la multiplicación es: {resultado}"
    
#     def division(self):
#         resultado=self.num1 / self.num2    
#         return f"El resultado de la division es: {resultado}"
    
    
# producto=Calculadora(suma(1,2))
# print(producto)




class Calculadora:
    def __init__(self):
        self._num1=int(input("Numero1: "))
        self._num2=int(input("Numero2: "))
    
    @property
    def num1(self):
        return self._num1
    num1.setter
    def num1(self,num1):
        self._num1=num1
        
    @property
    def num2(self):
        return self._num2
    num1.setter
    def num2(self,num2):
        self._num2=num2
    
    
    
    def suma(self):
        return self.num1 + self._num2   
        
    def resta(self):
        return self.num1 - self._num2   
    
    def multi(self):
        return self.num1 * self._num2   
    
    def division(self):
        return self.num1 / self._num2   
        
operacion=Calculadora()   
print(f"{operacion._num1} + {operacion._num2})={operacion.suma()}")
print(f"{operacion._num1} - {operacion._num2})={operacion.resta()}")
print(f"{operacion._num1} * {operacion._num2})={operacion.multi()}")
print(f"{operacion._num1} / {operacion._num2})={operacion.division()}")
