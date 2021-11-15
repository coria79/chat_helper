# https://pythonbros.com/como-controlar-el-mouse-con-python/
# https://pythonbros.com/controlar-el-teclado-con-python/
# https://decodigo.com/python-leer-un-archivo-de-texto


import mouse
from win32api import GetSystemMetrics
import keyboard
import time


def chat_helper():
    with open('Contactos.txt', 'r') as archivo:
        for linea in archivo:
            linea = linea[:-1]

            mouse.move(x=345, y=293, absolute=True, duration=0.4)  # Mover mouse al cuadro de texto de búsqueda

            mouse.click('left')

            keyboard.write(linea, delay=0.2)  # Escribir con teclado el nombre del contacto

            mouse.move(x=360, y=425, absolute=True,
                       duration=0.45)  # Mover el mouse para seleccionar el contacto buscado

            mouse.click('left')

            mouse.move(x=810, y=990, absolute=True, duration=0.4)  # Mover mouse al cuadro de texto de chat del contacto

            f = open('Mensaje.txt', 'r')  # Se busca el texto que se desea enviar de forma masiva
            texto = f.read()
            f.close()

            keyboard.write(texto, delay=0.075)  # Escribir con teclado el mensaje

            keyboard.send("enter")

            mouse.move(x=755, y=989, absolute=True, duration=0.4)  # Mover mouse al icono de adjuntar archivo

            mouse.click('left')

            mouse.move(x=753, y=930, absolute=True, duration=0.4)  # Mover mouse al al icono de adjuntar imagen

            mouse.click('left')

            mouse.move(x=451, y=51, absolute=True, duration=0.4)  # Mover mouse al cuadro de texto de ruta del archivo

            mouse.click('left')

            time.sleep(2)  # Escribir con teclado el nombre del contacto
            keyboard.send("delete")
            keyboard.write("C:\\Users\\Asus\\OneDrive\\PycharmProjects\\2021.10.23 BCH - Business Chat Helper",
                           delay=0.07)

            keyboard.send("enter")

            mouse.move(x=209, y=414, absolute=True, duration=0.4)  # Mover mouse al cuadro de texto de nombre de archivo

            mouse.click('left')

            keyboard.write("Deuda-Icon.png", delay=0.2)  # Escribir con teclado el nombre de la imagen

            keyboard.send("enter")

            time.sleep(2)

            keyboard.send("enter")


if __name__ == '__main__':
    chat_helper()
