def b1(lista,x):#funcion para buscar por apellidos
    nombres=[]
    nombres2=[]
    nombres_min=[]
    l1=[]
    l2=[]
    l3=[]
    for i in lista:
        l2.append(i)
    for i in lista:
        s=i.split()
        nombres.append(s[0])
    for i in range(0,len(lista)):
            nombres2.append((lista[i])[0:len(nombres[i])+1])
    for i in nombres:
        nombres_min.append(i.lower())
    for i in l2:
        c=0
        while c<len(l2):
            if nombres2[c] in i:
                i=i.replace(nombres2[c],'')
            c+=1
            if c==len(l2):
                break
        l3.append(i)
    for i in range(0,len(l3)):
        if x.lower() in (l3[i]).lower():
            l1.append(lista[i])
    return l1
def b2(lista,x):#funcion para buscar por nombre
    l1=[]
    nombres=[]
    for i in lista:
        s=i.split()
        nombres.append(s[0])
    for i in range(0,len(lista)):
        if x.lower()==nombres[i].lower():
            l1.append(lista[i])
    return l1
def b3(lista,x):#funcion para buscar por parte del nombre
    l1=[]
    nombres=[]
    for i in lista:
        s=i.split()
        nombres.append(s[0])
    for i in range(0,len(lista)):
        if x.lower() in nombres[i].lower() and x.lower()!=nombres[i].lower():
            l1.append(lista[i])
    return l1
