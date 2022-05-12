import funciones
import operator
r=[]
d3={}
s2=[]
p =  ["Ernesto Cuadros Vargas", "Jorge Abad Cueva", "Xyoby Chávez Pacheco", "Antuané de la Flor Basterrechea", "Luis Quineche Orellana", "Ruth Canahuire Cabello", "Claudia Antonini", "Samuel Charca Mamani", "Alexander Peña Nevado", "Juan Carlos Rodríguez Reyes", "Luis Humberto Chirif Rivera", "Luis Castillo Campos", "Alejandro Ríos Cuadros", "Rosa Fabiola Jabo Bereche", "José Gaspar de la Puente Maldonado", "José Antonio Larco Martinelli", "Omar Bejarano Grandez", "José Alfredo Diaz León", "Humberto Galvez Perez", "Francisco Daniel Porles Ochoa", "Maria Esther Quintana Caceda", "Giuliana Maria Carrillo ", "Tulio Antonio Antezano Inga", "Carlos Alfredo Rios Perez", "Victor Gonzalo Ramirez Herrera", "Diana Maria Luna Torres", "David Vilca Tomaylla", "Melissa Barrera Tomas", "David Alberto Gallardo Yaya", "Flavio Cesar Ramirez Horna", "Ximena Guardia Muguruza", "César Alberto Cornejo Gómez", "Carlos Diaz Pozzuoli", "Cristina Navarro", "Brenilda Coronel", "Christopher Creighton Cox", "Carlos Marcelo Zorrilla Aranguren", "Sarah Sabina Rehman", "Javier Pizarro Romero", "Hector Bustamante", "Sheyla Montoya Hamoir", "Oriana Vidal De La Torre", "Giovanna Indica", "Fabien Yves Paul Cornillier", "Serapio Estanislao Cazana Canchis", "Barbara Veronica Quiñones Malca", "Alfredo Enrique Ebentreich Aguilar", "Jorge Arturo Castillo Sanchez", "Rosmary Benavente Quicaña", "Eunice Villicaña", "Norvic Chicchon Ugarte", "Juan Carlos Bueno Villanueva", "Marcela Del Rosario Livia Caso", "Lei Zhang", "Lucia Geovanna Rodriguez Wu", "Teofilo Chambilla", "Patricio Morriberón Cornejo", "Jose Antonio Fiestas Iquira", "Maria Hilda Bermejo Rios", "Jaime Farfan", "Jimmy Tarrillo Olano", "Christian Flores Vega", "Julio Valdivia Silva", "Helard Álvarez Sánchez", "Gabriela Pella", "Rafael Vera Pomalaza", "Patricia Araujo Pantoja", "Elmer Ramírez Quiroz", "Francisco Tarazona Vásquez", "Arturo Rojas Moreno", "Jose Ramos Silva", "Alejandra Ratti Parandelli", "Luis Quineche Orellana", "Miguel Angel Torres", "Rósulo Pérez Cupe", "Teresa Torres Bustamante", "Heider Sanchez Enriqquez", "Rubén Rivas", "Jade Isadora Brunsting", "Rocio Giovanna Hoyos Diaz", "Luis Alverto Palomino Marcelo", "Marvin Abisrror Zarate", "Patricio Morriberon Cornejo", "Mariano David Melgar Zavala", "Jorge Luis Alvarado Revata", "Christian Martin Franco Acosta", "Angela Pinedo Flores", "Jose Miguel Renom", "Katia Zegarra Sierra"]
print('-------------RANKING DE PROFESORES-------------')
print('Instrucciones:\nEn este programa usted podrá buscar profesores'
      '\nde la UTEC ya sea por su primer nombre, parte del '
      '\nprimer nombre o por el apellido.'
      '\nDespués tendrá que elegirlo para posteriormente'
      '\ncalificarlo por los siguientes criterios:'
      '\n-Nivel de Comunicación\n-Nivel de exámenes'
      '\n-Control de asistencia\n-Nivel de didáctica'
      '\n-Fácil o jalador')
a=1
o=''
H =input('Ingrese cualquier tecla para comenzar: ')
while o!='no':
    d={}
    print()
    print('1)------------Elegir un profesor--------------')
    print()
    s=[]
    while len(s)==0:
        v=[]
        g=[]
        n=[]
        print('a)Buscar por primer nombre\nb)Buscar por parte del primer nombre\nc)Buscar por apellido')
        x = input('Ingrese opción: ')
        while x!='a' and x!='b' and x!='c':
            x=input('Ingrese la opción correcta: ')
        y = input('Cuadro de búsqueda: ')
        if x=='a':
            g = funciones.b2(p,y)
        elif x=='b':
            g=funciones.b3(p,y)
        elif x=='c':
            g=funciones.b1(p,y)
        if len(g)==0:
            print('Resultados no encontrados.')
            print('---------------------------------------')
        elif len(g)>0:
            print('Profesores encontrados: ')
            for i in range(0,len(g)):
                n.append(i+1)
                v.append(str(i+1))
                print(f'{(i+1)}. {g[i]}')

            z=input('¿Desea elegir al profesor?(si/no): ')
            while z!='si' and z!='no':
                z=input('Ingrese si o no: ')
            if z=='si':
                m=input('Ingrese el numero asignado al profesor: ')
                while m not in v:
                    m=input('Por favor, ingrese el numero asignado al profesor: ')
                if g[int(m)-1] in s2:
                    print('Este profesor ya ha sido elegido')
                elif g[int(m)-1] not in s2:
                    s.append(g[int(m)-1])
                    s2.append(g[int(m)-1])
                print('-------------------------------------')
                if len(s)>0:
                    print(f'Profesor elegido: {s[0]}')
            elif z=='no':
                print('-------------------------------------')
    print()
    if len(s)>0:
        print('2)-----------Calificar al profesor----------------')
        print()
        print('--------Nivel de comunicación en el aula------------')
        print('-Se lleva bien con los alumnos y los incentiva a\n  trabajar '
              'en equipo: 5ptos\n-Se lleva bien con los alumnos: 4ptos\n-De vez en cuando se relaciona'
              ' con los alumnos: 3ptos\n-Casi nunca habla con los alumnos y solo se enfoca en dictar: 2ptos'
              '\n-No habla con ningun alumno ni resuelve las dudas que tengan: 1pto')
        m=input('Ingrese la cantidad de puntaje que desea asignarle: ')
        while m!='1' and m!='2' and m!='3' and m!='4' and m!='5':
            m=input('Por favor, ingrese una cantidad correcta: ')
        d['Nivel de comunicación en el aula']= int(m)
        print()
        print('--------Nivel de exámenes------------')
        print('-Muy difíciles: 5ptos\n-difíciles: 4ptos\n-Regulares: 3ptos\n-Fáciles: 2ptos\n'
              '-Demasiado Fáciles: 1pto')
        m=input('Ingrese la cantidad de puntaje que desea asignarle: ')
        while m!='1' and m!='2' and m!='3' and m!='4' and m!='5':
            m=input('Por favor, ingrese una cantidad correcta: ')
        d['Nivel exámenes']= int(m)
        print()
        print('--------Control de asistencia------------')
        print('-El profesor siempre toma asistencia'
              ': 5ptos\nEl profesor casi siempre toma asistencia: 4 ptos'
              '\n-De vez en cuando toma asistencia: 3ptos\n-Muy pocas veces toma asistencia'
              ': 2ptos\n-Nunca toma asistencia: 1pto')
        m=input('Ingrese la cantidad de puntaje que desea asignarle: ')
        while m!='1' and m!='2' and m!='3' and m!='4' and m!='5':
            m=input('Por favor, ingrese una cantidad correcta: ')
        d['Control de asistencia']= int(m)
        print()
        print('--------Nivel de didáctica------------')
        print('-Sus clases son muy entendibles, entretenidas y '
              'motiva a los\n alumnos a trabajar en clases'
              ': 5ptos\n-Sus clases son entendibles e interesantes: 4ptos\n-Sus clases '
              'son entendibles: 3ptos\n-Solo algunos le entienden y'
              ' no motiva a los alumnos: 2ptos\n-Sus clases no se entienden y no le interesan los alumnos: 1pto')

        m=input('Ingrese la cantidad de puntaje que desea asignarle: ')
        while m!='1' and m!='2' and m!='3' and m!='4' and m!='5':
            m=input('Por favor, ingrese una cantidad correcta: ')
        d['Nivel de didáctica']= int(m)
        print()
        print('--------¿Fácil o Jalador?------------')
        print('-Jalador: 1pto\n-Fácil: 2ptos')
        m=input('Ingrese la cantidad de puntaje que desea asignarle: ')
        while m!='1' and m!='2':
            m=input('Por favor, ingrese una cantidad correcta: ')
        if m=='1':
            d['Curso jalador']= int(m)
        elif m=='2':
            d['Curso fácil']= int(m)
        r.append(d)
        if len(r)>1:
            o=input('¿Desea continuar eligiendo profesores?(si/no): ')
            while o!='si' and o!='no':
                o=input("Ingrese 'si' o 'no': ")
        print('---------------------------------------------')
print('-----------RESULTADOS DEL RANKING------------')
t=[]
for i in r:
    C=0
    for j in i.keys():
        C+=i[j]
    t.append(C)
print('Puntajes: ')
for i in range(0,len(r)):
    d3[s2[i]]=t[i]
    print(f'Profesor {s2[i]}: {t[i]} puntos')
    print()
    for j in r[i].keys():
        print(f'-{j} = {(r[i])[j]}ptos')
    print()
#por ultimo, se imprime el ranking
N=1
d4=dict(sorted(d3.items(), key=operator.itemgetter(1), reverse=True))
for i in d4.keys():
    print(f'PUESTO {N}: {i} con {d4[i]} puntos')
    N+=1
print()
print('Programa realizado por:\n'
      '-Luis Robledo\n-Luis Barboza\n-Pedro Lizarbe')
