# TAREA 1 CIFRADO CAESAR

## Explicación básica
El cifrado caesar se logra mediante la codificación de nuestro abecedario en números y aplicando un desplazamiento dado a partir de (códigoLetra+K)mod(len(abecedario)) donde K es nuestra llave yy es cualquier número que se nos ocurra, esto siendo posible gracias a la operación modulo que restringe nuestro desplazamiento al universo de números en el rango de 0-len(abecedario)-1

## Descripción del proyecto

El proyecto fue realizado en python, por desgracia, pero con suerte y tiempo libre espere que lo suba en lenguaje C.

Se usa la estructura de diccionario de python para codificar el abecedario así se ahorran un par de líneas pudiendo relacionar inmediatamente un caracter con un número, pero lo cierto es que se podría haber utilizado una lista simple pero tendría que recorrerla cada que tuviera que determinar en qué posición estaba el caracter que buscamos.

La lógica se realiza mediante ciclos for primero cargando la codificación a partir del arreglo del abecedario, que puede ser modificado a voluntad dentro del código, se codifica por medio de la estructura de Diccionario y se aplica el desplazamiento guardando el nuevo código en otro arreglo que se decodificará en un ciclo posterior.

## Ejecución del proyecto

El proyecto puede ejecutarse en cualquier ambiente de python ya sea visual studio code pero confío en que tendrá instalado python y por lo tanto podrá ejecutarlo desde terminal de la siguiente manera:

python Caesar.py

Le aparecerá algo como lo siguiente:

Ingrese la frase a cifrar:_

Puede poner cualquier frase con cualquier letra del abecedario americano, es decir, no ñ ni acentos ni caracteres extraños, ni números, aún así si lo desea puede modificarlo en el código agregando dichos caracteres.
Posterioremente le aparecerá lo siguiente:

Ingrese la llave:_

aquí podra elegir cualquier número entero tanto positivo como negativo, aunque los negativos son para decodificar una frase ya codificada.

Y le debería de dar un resultado similar al siguiente:

El cifrado es: ['R', 'E', 'S', 'U' , 'L' , 'T' , 'A' , 'D' , 'O' ]

## Enserio no tiene python?

Bueno aquí hay unas instrucciones rápidas en linux para cualquier distribución de Ubunutu o Debian

sudo apt update
sudo apt install python3

## Y además no tiene linux? 

Bueno está bien igual se puede instalar en Windows

Descargar el instalador
Ve a la página oficial de Python:
https://www.python.org/downloads/windows/

Descarga la última versión de Python 3 para Windows.

Ejecutar el instalador
Abre el archivo .exe que descargaste.
IMPORTANTE: Marca la opción "Add Python to PATH" (para poder usar Python desde la terminal).
Haz clic en "Install Now" y espera a que termine la instalación.

Verificar la instalación
Después de instalar, abre el Símbolo del sistema (CMD) o PowerShell y escribe:

powershell
Copy
Edit
python --version
Si ves algo como Python 3.x.x, significa que la instalación fue exitosa. 🎉

(Opcional) Instalar pip y probarlo
Python ya viene con pip (el administrador de paquetes), pero puedes verificarlo con:

powershell
Copy
Edit
pip --version
Para probar pip, instala una librería como requests:

powershell
Copy
Edit
pip install requests
