# TAREA 2 CIFRADO homofónico

## Explicación básica
El cifrado homofónico es un tipo de cifrado de función one way donde solo se puede pasar del dominio al codominio y para descifrar se requeriría de una tabla.
La tabla es generada por nosotros y usualmente se hace un análisis lingüistico para poder determinar qué letra se repite más y añadir más valores al codominio volviendo más seguro el encriptado.

## Descripción del proyecto

El proyecto fue realizado en python, por desgracia, pero con suerte y tiempo libre espere que lo suba en lenguaje C.

Se realizó un preprocesamiento a la entrada para que se ajustase al alfabeto utilizado, podríamos agregar las letras al alfabeto para cambiar esto, posteriormente se hace un ciclo for donde se tomará un número aleatorio del arreglo que le corresponde a la tabla y se cambiará a binario, al resultar la tabla con 91 números el binario es de 7 bits. 

## Ejecución del proyecto

El proyecto puede ejecutarse en cualquier ambiente de python ya sea visual studio code pero confío en que tendrá instalado python y por lo tanto podrá ejecutarlo desde terminal de la siguiente manera:

python3 Homofonico.py

Le aparecerá algo como lo siguiente:

Ingrese la frase a cifrar:_

Puede poner cualquier frase 

El cifrado es: ['1011010', '1011010', '0010101', '0010110' , '0010010' , '0000000' , '1111111' , '1011010' , '1011001' ]

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
