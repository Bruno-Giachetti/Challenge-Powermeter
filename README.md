# Challenge-Powermeter

Prueba tecnica realizada para la empresa Powermeter.

**Ejercicio 2:**
Correr el archivo Ejercicio 2.py

**Ejercicio 1:**

Para correr la api:

-Con Docker: abrir la terminal adentro del directorio Challenge-Powermeter y escribir docker-compose up


-Sin Docker: abrir la terminar adentro del directorio Challenge-Powermeter y correr los siguientes comandos:
1- source ./ejercicio-1-venv/bin/activate
2- cd ejercicio_1
3- pip install -r requirements.txt
4- python manage.py migrate
5- python manage.py runserver

URL Documentacion Swagger: http://localhost:8000/docs/

Endpoints:
- http://localhost:8000/medidores/

Sirve para crear los medidores con la llave y el nombre del medidor con metodo POST.
Tambien se pueden listar todos los medidores con el metodo GET.
Json de ejemplo para el body:
{
        "llaveIdentificadora": "A1",
        "nombre": "Medidor 1"
}

- http://localhost:8000/mediciones/

Sirve para crear las mediciones indicando fecha y hora (datetime), consumo y medidor con metodo POST.
Tambien se pueden listar todas las mediciones con el metodo GET.
Json de ejemplo para el body:
{
        "fechaYHora": "2023-01-05T23:53:40Z",
        "consumo": 900.3,
        "medidor": "A1"
}

- http://localhost:8000/medidores/(Aca se escribe la llave del medidor que se requiere)/maximoConsumo/

Sirve para recibir la medicion con el maximo consumo del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/medidores/A1/maximoConsumo/

- http://localhost:8000/medidores/(Aca se escribe la llave del medidor que se requiere)/minimoConsumo/

Sirve para recibir la medicion con el minimo consumo del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/medidores/A1/minimoConsumo/

- http://localhost:8000/medidores/(Aca se escribe la llave del medidor que se requiere)/consumoTotal/

Sirve para recibir el consumo total del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/medidores/A1/consumoTotal/

- http://localhost:8000/medidores/(Aca se escribe la llave del medidor que se requiere)/consumoPromedio/

Sirve para recibir el consumo promedio del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/medidores/A1/consumoPromedio/


**Consideraciones:**

-No se pueden agregar medidores con la misma llave, en la base de datos esto ya esta controlado por ser Primary Key, pero ademas
hay una validacion a la hora de crear el medidor

-No se pueden agregar mediciones a medidores que no existen

-La unidad de kwh esta seteada y no se puede elegir otra, de todos modos si hubiera que agregar mas unidades hay un enum de 
unidades para que en un futuro haya un desplegable para elegir unidades si hiciera falta

-El campo Unidad cuando se crea una medicion es opcional, si no se lo llena automaticamente se usa kwh y si se ingresa una unidad incorrecta, no se
podra crear la medicion. En este caso la unica unidad aceptable es kwh.

-No se pueden agregar mediciones negativas.

-No se pueden utilizar medidores inexistentes o sin mediciones para calcular el consumo promedio, ni el consumo total, ni el minimo o maximo consumo

**Cuestiones de diseño**

-La llave identificadora de los medidores la considero Primary Key de la tabla medidores, por el contexto del ejercicio.

-En el modelo de datos la Foreign Key que relaciona medicion con medidor necesariamente tiene que ir del lado de medicion, diseñé el dominio siendo
fiel a esta restricción.

-Tanto el consumo total como el promedio seria prudente guardarlos como campos en el medidor, esto es porque son calculos que pueden ser muy demandantes
en recursos si hay muchas mediciones en el medidor. Este modelo es simplificado y solo busca resolver los puntos mencionados, pero ayudaria a la performance este cambio propuesto.
