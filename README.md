Si el microservicio necesitara comunicarse con otro servicio encargado de almacenar el historial de cálculos en una base de datos externa, modificaría el diseño para implementar comunicación entre microservicios mediante peticiones HTTP o mensajería asíncrona.

En este caso, el microservicio actual (que calcula factorial y par/impar) actuaría como cliente, y el otro microservicio (de historial) como servidor que expone una API para guardar los resultados.

Después de calcular el número, su factorial y si es par o impar, el microservicio enviaría una solicitud POST al servicio de historial con un JSON como este:

``` json
{
  "numero": 5,
  "factorial": 120,
  "tipo": "impar",
  "fecha": "2025-11-10T18:55:00"
}
