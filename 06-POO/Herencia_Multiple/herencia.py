class A:
    def __init__(self):
        print('Soy la clase A')
    def a(self):
        print('Soy metodo de A')

class B:
    def __init__(self):
        print('Soy la clase B')
    def b(self):
        print('Soy metodo de B')

class C(B,A):
    def c(self):
        print('Soy metodo de C')
