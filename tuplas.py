Nombre=input("Ingrese su Nombre")
Edad=input("Ingrese su Edad")
Direccion=input("Ingrese su Direccion")
informacion= tuple((Nombre, Edad, Direccion,))

print("Los datos del seleccionado es :",informacion)

cursorea_lizados=[]


Curso=int(input("Ingrese el numero de cursos,si no tiene coloque 0 :"))
for i in range(Curso):
    if Curso==0:
        print("No ha realizado curso")
    else:
        Cursos1=input("Ingrese los cursos que ha realizado")
        cursorea_lizados.append(Cursos1)
        

cursorealizados=tuple((cursorea_lizados))        
print("los cursos realizados por el aspirante son :", cursorealizados)

Experiencia_Laboral=[]

Experiencia=int(input("En cuantos trabajos ha estado, por favor responda con un numero :"))
for i in range(Experiencia):
    if Experiencia==0:
        print("no tiene experiencia")
    else:
        Experiencia1=input("ingrese las empresas en las que ha estado")
        Experiencia_Laboral.append(Experiencia1)

experienciarealizada=tuple((Experiencia_Laboral))
print("El aspirante tiene experiencia en las siguientes empresas", experienciarealizada)       
 