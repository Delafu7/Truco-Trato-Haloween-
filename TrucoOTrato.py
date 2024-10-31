"""/*
 * Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
 * o Trato" y un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 * - En caso contrario retornará un error.
 */"""

import random 
import re 

class ErrorHalloween(Exception):
    """Error causado por no introducir los atributos necesarios"""
class Niño ():
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura=altura
    def identificate(self,trucoOtrato):
        print( f"Hola, soy {self.nombre} y me llevo {trucoOtrato} : \n")
    def numLetras(self):
        return len([letra for letra in str(self.nombre).lower() if r"[a-z]".find(letra)])
    def numSustos(self):
        sustos=self.numLetras()//2
        if self.edad%2==0:
            sustos+=2
        sustos+=self.altura//100*3
        return  sustos
    def numDulces(self):
        dulces=self.numLetras()
        if self.edad<10:
            dulces+=self.edad//3
        else:
            dulces+=3
        if self.altura<150:
            dulces+=self.altura//50*2
        else:
            dulces+=6
        return dulces
def trucoTrato(trickOrTrack, listaNinnos):
    """Calcula el número de caramelos y sustos de cada niño, 
    devolverá la cantidad de sustos por cada niño e imprimirá por pantalla los sustos o  los caramelos"""
    try:
        if all(isinstance(ninno,Niño)for ninno in listaNinnos) and isinstance(trickOrTrack,str) and re.match(r"^truco|trato$",trickOrTrack):
            misSustos=["🎃" ,"👻" ,"💀" ,"🕷" ,"🕸" ,"🦇"]
            misDulces=[ "🍰" ,"🍬", "🍡", "🍭", "🍪", "🍫","🧁", "🍩"]
            esTrato=trickOrTrack.lower().strip()=="trato"
            lista=[]#Solo se usa para saber si está correcto
            for ninno in listaNinnos:
                ninno.identificate(trickOrTrack)
                if esTrato:
                    cuenta= ninno.numSustos() 
                    for i in range(cuenta):
                            print(random.choice(misSustos))
                else:
                    cuenta= ninno.numDulces() 
                    for i in range(cuenta):
                        print(random.choice(misDulces))
                lista.append(cuenta)
            return lista
        else:
            raise  ErrorHalloween("Feliz Halloween")
    except ErrorHalloween:
        print("Si llegaste aqui feliz Halloween\n")
        return "Si llegaste aqui feliz Halloween"