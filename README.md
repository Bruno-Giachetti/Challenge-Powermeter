# Challenge-Powermeter

Prueba tecnica realizada para la empresa Powermeter.

**Ejercicio 1:**

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

- http://localhost:8000/maximoConsumo/(Aca se escribe la llave del medidor que se requiere)/

Sirve para recibir la medicion con el maximo consumo del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/maximoConsumo/A1/

- http://localhost:8000/minimoConsumo/(Aca se escribe la llave del medidor que se requiere)/

Sirve para recibir la medicion con el minimo consumo del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/minimoConsumo/A1/

- http://localhost:8000/consumoTotal/(Aca se escribe la llave del medidor que se requiere)/

Sirve para recibir el consumo total del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/consumoTotal/A1/

- http://localhost:8000/consumoPromedio/(Aca se escribe la llave del medidor que se requiere)/

Sirve para recibir el consumo promedio del medidor ingresado por llave en la URL.

Ejemplo de URL: http://localhost:8000/consumoPromedio/A1/


Consideraciones:
-No se pueden agregar medidores con la misma llave, en la base de datos esto ya esta controlado por ser Primary Key, pero ademas
hay una validacion a la hora de crear el medidor

-No se pueden agregar mediciones a medidores que no existen

-La unidad de kwh esta seteada y no se puede elegir otra, de todos modos si hubiera que agregar mas unidades hay un enum de 
unidades para que en un futuro haya un desplegable para elegir unidades si hiciera falta

-No se pueden agregar mediciones negativas.

