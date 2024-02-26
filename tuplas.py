Nombre=input("Ingrese su Nombre")
Edad=input("Ingrese su Edad")
Direccion=input("Ingrese su Direccion")
Experiencia_laboral=input("Ingrese si tiene experiencia (S/N)")
informacion= tuple((Nombre, Edad, Direccion, Experiencia_laboral))

print("Los datos del seleccionado es :",informacion)

Cursos1=0

Curso=int(input("Ingrese el numero de cursos,si no tiene coloque 0 :"))
for i in range(Curso):
    if Curso==0:
        print("No ha realizado curso")
    else:
        Cursos1=input("Ingrese los cursos que ha realizado")
        print(Cursos1)

Cursorealizados=tuple((Cursos1))        
print("los cursos realizados por el aspirante son :", Cursorealizados)
        