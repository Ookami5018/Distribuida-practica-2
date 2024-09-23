import simpy
from Nodo import *
from Canales.CanalBroadcast import *


class NodoVecinos(Nodo):

    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.identifiers = set()

    def conoceVecinos(self, env):
        # Envíamos la lista de nuestros vecinos a nuestros vecinos.
        self.canal_salida.envia(self.vecinos, self.vecinos)
        # Y esperamos los mensajes de nuestros vecinos.
        while True:
            mensaje = yield self.canal_entrada.get()
            self.identifiers.update(mensaje)
