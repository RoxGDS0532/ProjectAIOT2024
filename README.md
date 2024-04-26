# Tecnotails

## Integrantes
- Mata Hernández José Manuel 1222100430
- Ortega Renteria Maria Roxana 1222100822
  
## Carta de liberación del proyecto (imagen)
- Dirgida al docento
- Expresar las funcionalidades que tiene el proyecto
- Nombre de los integrantes que particparon en el proyecto
- Firmada por el empresario o docenete ageno a la UTNG, agradeciendo la contribucion de la UTNG.
- Hoja Membretada (Logo de la empresa, direccion y contacto)

## Lista del Hardware utilizada
| Id | Componente | Descripcion |Imagen |Cantidad |Costo total|
|----|------------|-------------|-------| :---:  | :---: |
| 1  | MQ2 Sensor de gas| El sensor de gas MQ2 es un sensor electrónico que detecta la concentración de gases en el aire123. Es utilizado para medir concentraciones de gas en el aire, como GLP, propano, metano, hidrógeno, alcohol, humo y monóxido de carbono.|![image](https://th.bing.com/th/id/OIP.tJ_XQXFZ9nyScl1avS5ywwHaHa?w=208&h=208&c=7&r=0&o=5&dpr=1.5&pid=1.7)| 1 | $139.00 |
| 2  | Buzzer Activo |Un buzzer activo es un dispositivo que puede generar sonido por sí mismo cuando se le aplica energía eléctrica. Se utiliza en dispositivos electrónicos para producir diferentes tonos y alertas.|![image](https://github.com/RoxGDS0532/ProjectAIOT2024/assets/141853929/fcb56cc2-f907-467a-b145-2c4e0f913099)| 2 |$40.00|
| 3  | Led | El LED es un diodo emisor de luz (en inglés, LightYmitón reyodo), un componente capaz de transformar la energía eléctrica en energía luminosa.|![image](https://th.bing.com/th/id/OIP.wBeviiMCRZC3HXgocOtHJAAAAA?w=236&h=179&c=7&r=0&o=5&dpr=1.5&pid=1.7)| 1 | $2.00|
| 4 | KY-026 Flame |El sensor de llama KY-026 (flame sensor Arduino) permite detectar la presencia de una llama abierta mediante un receptor de infrarrojos. El sensor puede utilizarse para crear una alarma de incendio en la casa y muchos otros dispositivos útiles.|![image](https://th.bing.com/th/id/OIP.AKYbGy91Cm68LBitbNUGJwHaHa?w=167&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7)| 1 | $49.00|
| 5 | ky-004 Button | También conocidos como interruptores de pulsación, son dispositivos electromecánicos que se utilizan para abrir o cerrar circuitos eléctricos temporalmente mediante una acción de presión. Su diseño básico consiste en un mecanismo de contacto que se activa al ser presionado y que, al liberar la presión, retorna a su posición original.|![image](https://th.bing.com/th/id/OIP.fDhukQZX36Zz-IO-_xsPEwHaHa?w=183&h=183&c=7&r=0&o=5&dpr=1.5&pid=1.7)| 1 | $3.50|
|6 | ky-024 Linear Hall | es un módulo que los permite detectar el campo magnético de un imán artificial o de algún material ferromagnético. | ![image](https://th.bing.com/th/id/OIP.Mr4DXMhPUnWEG8JCQGZoqQHaGW?w=218&h=187&c=7&r=0&o=5&dpr=1.5&pid=1.7) | 1 | $89.50|
|7| Ky-016 RGB Led| es un componente que consta de un LED RGB de 5 mm y es capaz de emitir luz de diferentes colores mediante la mezcla de los colores primarios del sistema RGB (rojo, verde y azul). | ![image](https://th.bing.com/th/id/OIP.ygAFlEGyH92msHL3_LakzQHaHa?w=208&h=209&c=7&r=0&o=5&dpr=1.5&pid=1.7) | 1| $61.00|
|8| Teclado numérico matricial 4x4| Un teclado matricial 4×4 es un dispositivo que agrupa varios pulsadores y permite controlarlos empleando un número de conductores inferior al que necesitaríamos al usarlos de forma individual.|![image](https://th.bing.com/th/id/OIP.pG6YHPeKnGuRO-AEatIYwgHaFj?w=243&h=182&c=7&r=0&o=5&dpr=1.5&pid=1.7)|1|$69.00|



## Lista de Software Utilizado

|Id |Software |Version |Tipo|
|:---:|:---:|:---:|:---:|
| 1 |Node-RED |2.0|Software Libre|
| 2 |MQTT     |3.1|Protocolo de mensajería ligero|
| 3 |MicroPython|3.4|Lenguaje de programación|
| 4 |Raspbian|11|Sistema Operativo|
| 5 |Thonny| 4.1.2|Software Libre|

## Visión del producto 
"Para los propietarios de hamburgueserías que buscan elevar la calidad y eficiencia de su servicio, BurgerTech ofrece un sistema de gestión integral diseñado específicamente para la industria de la comida rápida. Este sistema aprovecha tecnologías avanzadas para optimizar todos los aspectos del servicio. A diferencia de los métodos convencionales que pueden resultar en tiempos de espera prolongados y variabilidad en la calidad del servicio, nuestro sistema asegura una experiencia consistente y de alta calidad para cada persona. Hi - Tech Burger es la solución tecnológica que transforma y moderniza tu hamburguesería."


## Conexiones 
- Imagenes de Wokwi, Fritzing o de otro software que me permita mostrar las conexiones del circuito.
- Raspberry Pi
- Imagen Led
- ![image](https://github.com/RoxGDS0532/ProjectAIOT2024/blob/main/Captura%20de%20pantalla%202024-04-23%20082306.png)
- Imagen(MQ2 sensor de gas y Flame)
- ![image](https://github.com/RoxGDS0532/ProjectAIOT2024/blob/main/Captura%20de%20pantalla%202024-04-23%20084318.png)

## Funcionalidades del proyecto
|Id | Historia de ususario | Prioridad | Estimación | Como probarlo | Respondsable|
|---|----------------------|:---:|:---:|--- |:---: |
| 1 |Con el sensor de gas quiero que el sistema detecte gases peligrosos para segurar un ambiente segur | Alta | Alta | Realizar prubas con gases controlados | Manuel |
| 2 |Con el buzzer activo sonará una alerta cuando se detecte gas | Media | Alta |comprobar que el buzzer emite sonidos cuanda se active el sensor de gas| Manuel | 
| 3 |Con el led quiero que los trabajadores se den cuenta que algun cliente necesita algun servicio  | Alta | Alta | Testaer los 2 diferentes esados del led para comprobar que si funciona bien | Manuel |
| 4 |Usaremos un KY-026 Flame que detectara llamas para prevenir un incendio |Alta|Alta| Realizar pruebas con una llama controlada para comprobar la sensibilidad del sensor. |Roxana|
| 5 |Conn el Button queremos interactuar con el les para el servicio al cliente|Media|Alta|Asegurar que el botón responde a pulsaciones para cambiar configuraciones | Manuel |
| 6 | Los dueños del lugar no dijeron que aveces el congelador se queda un poco abierto lo que ocasiona qeu las carnes se descongelen es por eso que decidimos utilizar el KY-024 Lineal Hall para detectar que la puerta este cerrada correctamente |Alta|Alta| Probar con  campos magnéticos y verificar la respuesta del sensor. | Roxana |
| 7 |El RGB Led ira junto con el KY-024 para detectar la respuesta del iman y cambie de color | Media | Alta | Comprobar que el LED RGB cambia de color según el tipo de alerta o estado. |Roxana|

## Prototipo en Dibujo
- Coloca una imagen de tu proyecto al iniciar el desarrollo

## Evidencias 
- Captura de pantalla de los flujos de node RED
- Captura de pantalla del proyecto DASHBOARD Y pantalla de la ESP32
- Video demostrativo de las funcionalidades del proyecto
- Codigo fuente (PROHIBIDO PONER COMPRIMIDOS)
  
