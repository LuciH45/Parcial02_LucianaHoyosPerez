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
```
Para implementar esta comunicación, podría usarse la librería requests en Flask:
``` python 
import requests

requests.post("http://historial-service:5000/api/historial", json=respuesta)

```
Además, la URL del servicio externo se almacenaría en una variable de entorno (por ejemplo, mediante un archivo .env) para mantener la configuración desacoplada y fácilmente modificable.

En resumen, se separarían responsabilidades:

- Microservicio A: realiza los cálculos.

- Microservicio B: guarda el historial en la base de datos.

La comunicación sería a través de HTTP REST (POST), se usarían variables de entorno para configurar direcciones o puertos.

Esto mantiene la modularidad, escalabilidad y bajo acoplamiento, principios clave de los microservicios.

### Para ejecutar sigue los siguientes pasos
1. Descarga Flask
   ``` bash
      pip install flask
   ```
2. Ejecuta la app
    ``` bash
      py app.py
   ```
3. Entra al navegador y ve a:
   
http://127.0.0.1:5000/numero/5



