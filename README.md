# Tecnotails

## Integrantes
- Mata Hernández José Manuel 1222100430
- Ortega Renteria Maria Roxana 1222100822
- Ramirez Sanchez Oscar 1222100812
  
## Carta de liberación del proyecto (imagen)
- Dirgida al docento
- Expresar las funcionalidades que tiene el proyecto
- Nombre de los integrantes qu eparticparon en el proyecto
- Firmada por el empresario o docenete ageno a la UTNG, agradeciendo la contribucion de la UTNG.
- Hoja Membretada (Logro de la empresa, direccion y contacto)

## Lista del Hardware utilizada
| Id | Componente | Descripcion |Imagen |Cantidad |Costo total|
|----|------------|-------------|-------| :---:  | :---: |
| 1  |Sensor de Flujo| Un sensor de flujo es un dispositivo que detecta y mide la cantidad de líquido, gas o vapor que pasa por un conducto en un tiempo determinado. Es crucial para controlar y optimizar procesos en una variedad de aplicaciones industriales y comerciales.|![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/275241b1-92dd-43be-bbd7-e692496a6b7f)| 1 | $135.00 |
| 2  | Buzzer Activo |Un buzzer activo es un dispositivo que puede generar sonido por sí mismo cuando se le aplica energía eléctrica. Se utiliza en dispositivos electrónicos para producir diferentes tonos y alertas.|![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/fcb56cc2-f907-467a-b145-2c4e0f913099)| 2 |$40.00|
| 3  | Relay KY-019 | El módulo Relay KY-019 es un interruptor controlado por señales eléctricas de bajo voltaje, utilizado para controlar dispositivos de alto voltaje o corriente en proyectos electrónicos.|![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/074781e2-bf03-4986-aa22-d19a952635b7)| 1 | $170.00|
| 4 | KY-001 Temperature Sensor Module|El módulo KY-001 es un sensor de temperatura digital que utiliza el sensor DS18B20. Se conecta fácilmente a microcontroladores como Arduino y es ideal para medir temperaturas con precisión.|![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/d3c5a114-ba8e-464e-812e-a292e80ad57a)| 1 | $42.00|
| 5 | Potenciometro | El potenciómetro es un componente electrónico de tres terminales que se utiliza para controlar la resistencia eléctrica ajustando un valor variable. Se utiliza comúnmente para ajustar el brillo de una luz, el volumen de un dispositivo de audio o el rango de movimiento de un motor, entre otras aplicaciones.|![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/47387f4a-390d-4b31-9800-f3ce7267724c)| 1 | $53.50|
|6 | Motor a Pasos | Un motor a pasos es un tipo de motor que convierte impulsos eléctricos en movimientos discretos o pasos angulares. Estos motores son utilizados en aplicaciones donde se requiere precisión en el posicionamiento, como impresoras 3D, máquinas CNC y sistemas de automatización. | ![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/97a806aa-c7e3-4a98-8c9a-ddafefa69665) | 1 | $60.00|
|7| Sensor Relé| Un relé es un interruptor controlado eléctricamente que permite controlar circuitos de alta potencia con señales de baja potencia. | ![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/44963d48-b002-4db7-93ca-21cb41be68b7) | 1| $100.00|
|8| Sensor de movimiento PIR HC-SR501| El sensor de movimiento PIR HC-SR501 detecta el movimiento mediante la radiación infrarroja y se utiliza en proyectos de seguridad y automatización.|![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/5d142779-7623-43f5-8dfe-5010f5e21952)|1|$50.00|



## Lista de Software Utilizado

|Id |Software |Version |Tipo|
|:---:|:---:|:---:|:---:|
| 1 |Node-RED |2.0|Software Libre|
| 2 |MQTT     |3.1|Protocolo de mensajería ligero|
| 3 |MicroPython|3.4|Lenguaje de programación|
| 4 |Raspbian|11|Sistema Operativo|
| 5 |Thonny| 4.1.2|Software Libre|

## Visión del producto 
"Para artistas y artesanos de la talavera que buscan mejorar la eficiencia y calidad en la producción tradicional de la talavera, EL sistema Tecnotails es un sistema de IoT integrado que optimiza el proceso de producción mediante la monitorización en tiempo real y la regulación automatizada. A diferencia de los métodos tradicionales que pueden llevar a errores y desperdicio de materiales, nuestro sistema proporciona una solución tecnológica innovadora que preserva la autenticidad del arte de la talavera mientras mejora la eficiencia y calidad en cada etapa del proceso."


## Conexiones 
- Imagenes de Wokwi, Fritzing o de otro software que me permita mostrar las conexiones del circuito
- Raspberry Pi
- ESP 32

## Funcionalidades del proyecto
|Id | Historia de ususario | Prioridad | Estimación | Como probarlo | Respondsable|
|---|----------------------|:---:|:---:|--- |:---: |
| 1 |Con el sensor de flujo se medirá la cantidad de agua al usar en la mezcla de esmalte| Alta | Alta | Preparar mezcla de esmalte | Oscar |
| 2 |Con el buzzer activo sonará una alerta cuando se pase el tiempo de cocción | Media | Alta |Prender el horno y hornear| Roxana | 
| 3 |Con un relay KY-019 controlará la velocidad del motor de la batidora | Alta | Alta | Una preparación de esmalte | Manuel |
| 4 |Usaremos un KY-001 Temperature Sensor Module que detectara cuando exista una temperatura elevada y mandara una alerta al controlador para que active los ventiladores del cuarto de decoraciones |Alta|Alta|Al detectar calor en el area |Roxana|
| 5 |Con un potenciometro controlaremos un motor a pasos que hara la funcion de mezclar esmalte con los distintas tonalidades de colores|Media|Alta|Se evaluara distintas mediciones para evitar que se muy rapido el movimiento |Manuel|
| 6 |Con un reele controlaremos el flujo de agua hasta la batidora de esmalte |Alta|Alta|Probando con una mangera el abierro y cerado del paso de agua|Roxana|
| 7 |Sensor de movimiento PIR HC-SR501 que detecte movimiento al salir o entrar al taller| Media | Alta | Activando al detectar movimiento en la salida del personal |Oscar|

## Prototipo en Dibujo
- Coloca una imagen de tu proyecto al iniciar el desarrollo

## Evidencias 
- Captura de pantalla de los flujos de node RED
- Captura de pantalla del proyecto DASHBOARD Y pantalla de la ESP32
- Video demostrativo de las funcionalidades del proyecto
- Codigo fuente (PROHIBIDO PONER COMPRIMIDOS)
  
