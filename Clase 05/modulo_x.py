
# Clase para la estructura de pila
class Pila(object): #LIFO Last inn, First out
    def __init__(self):
        self.__list = []

    def push(self,item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()
    
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None
    
    def is_empty(self):
        return self.__list == []
    
    def size(self):
        return len(self.__list)
    
    
    def mostrar(self):
        # if self.__list:
        #     for item in self.__list:
        #         print(item)
        #     else:
        #         print('No hay elementos')
        return self.__list
    

# Clases para la estructura de cola    
# FIFO //first in First out
class Cola(object):
    def __init__(self):
        self.__list = []

    #agregar elemento a la cola
    def enqueue(self,item):
        self.__list.append(item)
    
    #quitar un elemento de la cola
    def dequeue(self):
        return self.__list.pop(0)
    
    #obtener el elemento superior de la lista
    def first(self):
        if self.__list:
            return self.__list[0]
        else:
            return None

    # revisar si esta vacia
    def is_empty(self):
        return self.__list == []
    
    #regresa el len de la lista
    def size(self):
        return (len(self.__list))
    
    # regresa los elementos dentro de la lista
    def mostrar(self):
        # if self.__list:
        #     for item in self.__list:
        #         print(item)
        #     else:
        #         print('No hay elementos')
        return self.__list

