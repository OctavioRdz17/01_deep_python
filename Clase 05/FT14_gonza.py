import random 

class juegoPila(object):

    def __init__(self):
        self.__list = []
        while len(self.__list) < 20:
             numero = random.randint(1,20)
             if numero not in self.__list:
                self.__list.append(numero)
    
    # Quitar el ultimo elemento de la pila
    def __pop(self):
        return self.__list.pop()
    
    # Imprimir la pila completa
    def __mostrar(self):
        if self.__list: # -> if self.__list == True -> if len(self.__list) > 0:
            for item in self.__list:
                print(item)
        else:
            print('No hay elementos')
    
    # Creamos el metodo jugar

    def jugar(self):
        # Empieza el juego
        while True:
            nro = input('Ingrese la cantidad de elementos a retirar: ')

            if not nro.isdecimal(): # .isdecimal devuelve True o False, si no es numero -> condicion = False -> va a entrar al if
                nro = input('Ingresar la cantidad de elementos a retirar nuevamente: ')
            else:
                nro = int(nro)
                break
        
        # Empieza la logica 
        print('Pila original: ')
        self.__mostrar()

        calificacion = 10
        suma = 0 

        for i in range(nro):
            suma += self.__pop()
        print('Pila Obtenida: ')
        self.__mostrar()

        print(f'Se sumo la cantidad total de: {suma}')

        if suma > 50: # Si la suma es mayor a 50, el usuario pierde
            print('No cumpliste el objetivo, perdiste :((')
        else:  # Si no, tenemos que seguir sumando
            while suma <= 50: # Mientras que la suma no supere el valor de 50
                suma += self.__pop() # Sumamos un elemento mas
                if suma <= 50: # Nos preguntamos si ahora superamos a 50
                    calificacion -= 1 # Si no superamos a 50, se quita un punto de calificacion
            print(f'OBJETIVO CUMPLIDO !! FELICITACIONES :))) tu calificacion fue de: {calificacion}')

class Jarra():
    def __init__(self, cap):
        self.__elemento_agua = '*'
        self.__elemento_vacio = ' '
        self.__capacidad = cap
        self.__lista = []
        i = 0
        while (i < cap):
            self.__lista.append(self.__elemento_vacio)
            i += 1
    
    def vaciar(self):
        i = 0
        while(i < self.__capacidad):
            self.__lista[i] = self.__elemento_vacio
            i += 1
    
    def llenar(self):
        i = 0
        while (i < self.__capacidad):
            self.__lista[i] = self.__elemento_agua
            i += 1
        """
        for i in range(self.__capacidad):
            self.__lista[i] = self.__elemento_agua
        """
    def mostrar_jarra(self):
        print(f'Jarra de {self.__capacidad} litros')
        for elemento in self.__lista:
            print('|',elemento,'|')
        print('-----')

    def cantidadLitros(self):
        cantidad = 0
        for elemento in self.__lista:
            if (elemento == self.__elemento_agua):
                cantidad += 1
        return cantidad
    
    def quitar_litros(self, litros):
        i = 0
        encontrado = False
        while (not encontrado): # encontrado = False
          
            if (self.__lista[i] == self.__elemento_agua):
                encontrado = True
            i += 1
        
        i -= 1
        while (litros > 0):
            self.__lista[i] = self.__elemento_vacio
            i += 1
            litros -= 1

    def agregar_litros(self, litros):
        i = 0
        while((i < self.__capacidad) and (self.__lista[i] == self.__elemento_vacio)):
            i += 1
        while (litros > 0):
            i -= 1
            self.__lista[i] = self.__elemento_agua
            litros -= 1


class JuegoJarras():
    def __init__(self):
        self.__j3L = Jarra(3)
        self.__j5L = Jarra(5)
        self.__opciones_validas = ['1','2','3','4','5','6','7']

        
    def jugar(self):
        nro = 0
        counter = 0
        while nro < 7:
            print('JUEGO DE LAS JARRAS !!!:')
            print('************************************')
            print('1- LLenar la jarra de 3L')
            print('2- Llenar la jarra de 5L')
            print('3- Vacia la jarra de 3L')
            print('4- Vaciar la jarra de 5L')
            print('5- Verter el contenido de la jarra de 3L en la de 5L')
            print('6- Verter el contenido de la jarra de 5L en la de 3L')
            print('7- SALIR')
            print('************************************')

            self.__j3L.mostrar_jarra()
            self.__j5L.mostrar_jarra()
            print('************************************')
            nro = input('Ingrese una opcion: ')
            counter += 1
            if nro not in self.__opciones_validas:
                nro = 0
            else:
                nro = int(nro)
            
            if nro == 1:
                self.__j3L.llenar()
            elif nro == 2:
                self.__j5L.llenar()
            elif nro == 3:
                self.__j3L.vaciar()
            elif nro == 4:
                self.__j5L.vaciar()
            elif nro == 5:
                jarra3L = self.__j3L.cantidadLitros()
                jarra5L = self.__j5L.cantidadLitros()
                disponible_5L = 5 - jarra5L
                if disponible_5L < jarra3L:
                    intercambio = disponible_5L
                else:
                    intercambio = jarra3L
                
                self.__j3L.quitar_litros(intercambio)
                self.__j5L.agregar_litros(intercambio)
            elif nro == 6:
                jarra3L = self.__j3L.cantidadLitros()
                jarra5L = self.__j5L.cantidadLitros()
                disponible_3L = 3 - jarra3L
                if disponible_3L < jarra5L:
                    intercambio = disponible_3L
                else:
                    intercambio = jarra5L
                
                self.__j3L.agregar_litros(intercambio)
                self.__j5L.quitar_litros(intercambio)
            
            if (self.__j5L.cantidadLitros() == 4):
                print(f'FELICITACIONES !!! TU PUNTAJE ES DE: {100 - counter * 10}')
                print('******************************')
                self.__j3L.mostrar_jarra()
                self.__j5L.mostrar_jarra() # Aca tiene que haber 4Lts
                print('*************************')
                print('1- Jugar de nuevo')
                print('2- Terminar')
                nro = input('Porfavor ingrese una opcion: ')
                if nro not in self.__opciones_validas:
                    nro = 0
                else:
                    nro = int(nro)
                    if nro == 1:
                        self.__j3L.vaciar()
                        self.__j5L.vaciar()
                    elif nro == 2:
                        nro = 7

j = JuegoJarras()
j.jugar()