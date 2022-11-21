from persona import Cliente, Empleado

# cliente1 = Cliente('Angel' , 25)
# cliente2 = Cliente('Ramon', 33)

# cliente1.detalle_persona() 
# print(cliente2)


empleado1 = Empleado('Angel', 25, 1500)
empleado2 = Empleado('Ramon', 25, 2000)

empleado1.detalle_persona()
empleado1.detalle_empleado()

print(empleado2)