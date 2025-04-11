
candidato1 = 0.0
candidato2 = 0.0
candidato3 = 0.0
candidato4 = 0.0
voto = -1
while voto != 0:
     voto = int(input('Cual va a ser tu voto? (1,2,3,4)\n'))
     if voto == 1.0:
               candidato1 += 1
               print("Voto registrado\n")
     elif voto == 2.0:
               candidato2 += 1
               print("Voto registrado\n")
     elif voto == 3.0:
               candidato3 += 1
               print("Voto registrado\n")
     elif voto == 4.0:
               candidato4 += 1
               print("Voto registrado\n")
print("Sistema finalizado")
cantvotos = candidato1 + candidato2 + candidato3 + candidato4
p1 = (candidato1*100) / cantvotos
p2 = (candidato2*100) / cantvotos
p3 = (candidato3*100) / cantvotos
p4 = (candidato4*100) / cantvotos           
print(f"La cantidad de votos del candidato 1 es {candidato1} y el porcentaje que obtuvo es {p1}" )             
print(f"La cantidad de votos del candidato 2 es {candidato2} y el porcentaje que obtuvo es {p2}" ) 
print(f"La cantidad de votos del candidato 3 es {candidato3} y el porcentaje que obtuvo es {p3}" ) 
print(f"La cantidad de votos del candidato 4 es {candidato4} y el porcentaje que obtuvo es {p4}" )

"""GRUPO 3:
-ELIAS DE LA CRUZ, JOSUE FABRIZIO
-GARCIA TORIBIO, HAMER JOEL
-MENDOZA HUAMAN, RODRIGO ANDERSON
-OQUENDO CLEMENTE, WILLIAM DIEGO
-RIVERA GAMARRA, JHOVANNI DONOVAN
"""
