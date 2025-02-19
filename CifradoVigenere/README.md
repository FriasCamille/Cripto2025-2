# TAREA 2 CIFRADO Vigenere

## Explicación básica
El cifrado Vigenere es un cesar con esteroides, está vez la llave será una palabra, cualquier palabra pero solo 1, esta será codificada y se usará cada número de la codificación para hacer un caesar a cada letra de la palabra que queremos cifrar.

## Descripción del proyecto

El proyecto fue realizado en python, por desgracia, pero con suerte y tiempo libre espere que lo suba en lenguaje C.

Se separaron en funciones de forma que la codificación y el desplazamiento son funciones independientes.Esto para llamarlas en un ciclo cuando sea necesario. 

## Ejecución del proyecto

El proyecto puede ejecutarse en cualquier ambiente de python ya sea visual studio code pero confío en que tendrá instalado python y por lo tanto podrá ejecutarlo desde terminal de la siguiente manera:

python Vigenere.py

Le aparecerá algo como lo siguiente:

Ingrese la frase a cifrar:_

Puede poner cualquier frase con cualquier letra del abecedario americano, es decir, no ñ ni acentos ni caracteres extraños, ni números, aún así si lo desea puede modificarlo en el código agregando dichos caracteres.
Posterioremente le aparecerá lo siguiente:

Ingrese la llave:_

aquí podra elegir cualquier palabra con cualquier letra del abecedario americano, es decir, no ñ ni acentos ni caracteres extraños, ni números, aún así si lo desea puede modificarlo en el código agregando dichos caracteres.

Y le debería de dar un resultado similar al siguiente:

El cifrado es: ['R', 'E', 'S', 'U' , 'L' , 'T' , 'A' , 'D' , 'O' ]

## Enserio aún sin python?

Bueno aquí hay unas instrucciones rápidas en linux para cualquier distribución de Ubunutu o Debian

sudo apt update
sudo apt install python3

## Y además aún sin linux? 

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
