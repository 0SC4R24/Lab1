"""
GEOMETRIA PROYECTIVA

Laboratorio 1

Enunciado:

1. Dispositivo Antes de tomar la foto, obtén los siguientes datos técnicos de tu cámara (por ejemplo, la de tu teléfono móvil):
    • La distancia focal de la cámara.
    • El tamaño del sensor de la cámara.

2. Fotografía: Toma una fotografía de un objeto con altura conocida, situado a una distancia conocida.
    Asegúrate de que la altura del objeto esté alineada con el eje y del sistema de referencia de la cámara y
    la distancia al objeto con el eje z.

3. Cálculo de Proporciones: Utilizando los datos de los apartados 1 y 2, calcula qué porcentaje de la altura
    total de la imagen representará el objeto.

4. Verificación: Mide la proporción de la altura que ocupa el objeto en la imagen para verificar el cálculo
    anterior.


Datos:

    • Dispositivo con el que se ha echo la fotografía: Motorola Edge 20 Pro
    • Sensor de la fotografía: Samsung ISOCELL HM2
    • Datos del sensor:
        • Ancho: 8.3mm
        • Alto: 6.2mm
        • Distancia focal (35mm): 24mm
        • Distancia focal que marca el sensor en la información de la fotografía: 5,88mm
    Altura del objeto: 455mm
    Distancia del objeto a la cámara: 1630mm
"""
from math import sqrt

# Se definen las variables con los datos tomados, necesarios para hacer el cáculo
w = 8.3
h = 6.2
f_35 = 24
f = 5.88
a = 455
d = 1630

# Para hacerlo un poco más elegante, vamos a definir una función que haga el cálculo del porcentaje dependiendo de
# si la distancia focal aportada es la real, o la de referencia con 35mm y de si la foto se ha hecho con el dispositivo
# en vertical u horizontal

def porcentaje(es35mm = True, vertical = False):
    if es35mm:
        print(f"En este cálculo se usa la medida de distancia focal con referencia a un sensor de 35mm")
        diagonal_35mm = sqrt((36 ** 2) + (24 ** 2))  # diagonal del sensor de 35mm
        print(f"Diagonal del sensor de 35mm: {diagonal_35mm}")
        diagonal_real = sqrt((w ** 2) + (h ** 2))  # diagonal con los datos del sensor Samsung ISOCELL HM2
        print(f"Diagonal del sensor utilizado: {diagonal_real}")
        # Se usan las diagonales para calcular el crop factor y la distancia focal real fm
        crop_factor = diagonal_35mm / diagonal_real
        fm = f / crop_factor
        print(f"Crop factor: {crop_factor}")
        print(f"Distancia focal real (fm): {fm}")
    else:
        # Si se aporta la distancia focal real, se usa dicha medida, directamente
        fm = f

    # Se mide la coordenada en el sensor. Se diferencia si es Uccd o Vccd en función de si se ha tomado la fotografía
    # en horizontal o vertical
    medida_ccd = fm * a / d

    if vertical:
        # Al ser tomada en vertical, la medida del sensor es la del eje Uccd y se calcula el porcentaje con
        # la medida del ancho del sensor
        print(f"Uccd : {medida_ccd}")
        return medida_ccd / w * 100
    else:
        # Al ser tomada en horizontal, la medida del sensor es la del eje Vccd y se calcula el porcentaje con
        # la medida del alto del sensor
        print(f"Vccd : {medida_ccd}")
        return medida_ccd / h * 100

porcentaje_35mm = porcentaje(es35mm = True, vertical = True)

porcentaje_real = porcentaje(es35mm = False, vertical = True)

print(f"El porcentaje de un objeto de altura de {a}mm, a una distancia de {d}mm, con la distancia focal de referencia a 35mm en la fotografía es: {porcentaje_35mm}%")
print(f"El porcentaje de un objeto de altura de {a}mm, a una distancia de {d}mm, con la distancia focal real en la fotografía es: {porcentaje_35mm}%")
