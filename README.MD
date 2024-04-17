# README

## Autores
* Tatiana Murillo Mosquera
* David López Rivera

# ¿Para qué sirve?

Este código proporciona una herramienta para calcular la nómina de los empleados de una empresa en función de una serie de parámetros, como el salario básico, los días laborables, los días de licencia médica, las horas extras, entre otros. Al proporcionar estos datos, el programa calcula tanto los valores devengados como los valores deducidos de la nómina de cada empleado. Los valores devengados incluyen el salario base, el subsidio de transporte (si corresponde), y los pagos por horas extras, mientras que los valores deducidos abarcan las contribuciones a la seguridad social, el fondo de pensiones y las retenciones salariales.

Además de realizar cálculos básicos de nómina, el código también implementa una serie de validaciones para asegurarse de que los parámetros ingresados sean coherentes y cumplan con ciertas reglas establecidas, como por ejemplo, que el salario base sea mayor que el salario mínimo legal, que el porcentaje de seguro de salud no sea cero, y que el porcentaje de fondo de pensiones se ajuste según el rango salarial del empleado. Estas validaciones garantizan la integridad de los cálculos y ayudan a prevenir errores comunes en el procesamiento de la nómina.

# Propósito

Este código proporciona una herramienta completa y robusta para gestionar eficientemente la nómina de los empleados de una empresa, automatizando cálculos precisos y asegurando el cumplimiento de las regulaciones laborales pertinentes.

# Prerrequisitos

* **Instalación de Python**: Python es el lenguaje de programación utilizado en este programa, por lo que la persona que desee ejecutarlo deberá tener Python instalado en su sistema. Puede descargar Python desde el sitio web oficial de Python ([Instalador de Python](https://www.python.org/)) e instalarlo siguiendo las instrucciones proporcionadas.

* **Instalación de la libreria kivy**: Es un framework de código abierto en Python para desarrollar aplicaciones multitáctiles. Se utiliza principalmente para crear aplicaciones con interfaces de usuario (UI) atractivas y dinámicas que pueden funcionar en varias plataformas, incluyendo Windows, macOS, Linux, iOS y Android.

* **Instalacion de la extención kivymd**: Esta es una extensión de Kivy que proporciona una implementación de los principios de Material Design de Google para el framework Kivy. Material Design es un sistema de diseño desarrollado por Google que se centra en la usabilidad y la estética, proporcionando una guía visual coherente para el diseño de interfaces de usuario.

* **Datos de entrada relevantes**: Al ejecutar el programa se necesitará tener acceso a los datos necesarios para proporcionar los parámetros requeridos por el programa, como el salario básico, los días laborables, los días de licencia médica, entre otros.

# ¿Cómo está hecho?

El proyecto presenta una arquitectura modular y bien estructurada, diseñada para calcular la nómina de los empleados de una empresa de manera eficiente y precisa. El programa cuenta con 5 archivos, los cuales son:

1. MonthlyPaymentLogic.py
2. MonthlyPaymentTest.py
3. ExtraordinaryCasesTest.py
4. ErrorCaseTest.py
5. Console.py

* **MonthlyPaymentLogic.py**:

Es el archivo principal, aquí se guarda la lógica que el programa debe realizar. Al inicio contiene algunas constantes (`EXTRA_HOUR_DAYSHIFT`, `EXTRA_HOUR_NIGHTSHIFT`, `EXTRA_HOUR_DAYSHIFT_HOLIDAYS`, `EXTRA_HOUR_NIGHTSHIFT_HOLIDAYS`) que se requieren para el cálculo de la nómina. Luego están las clases de error, las cuales se aseguran de avisarle al usuario cuáles errores ha cometido. Después de esto sigue la clase `SettlementParameters` la cual se encarga de almacenar las variables ingresadas por el usuario y revisar que estas estén bien. Por último, están todas las funciones complementarias que nos ayudan a calcular los valores devengados y deducidos y calcular la nómina del trabajador.

**MonthlyPaymentTest.py**:

En este archivo se usa la biblioteca `unittest` para llevar a cabo los casos de prueba donde el programa debe correr perfectamente.

**ExtraordinaryCasesTest.py**:

En este archivo se usa la biblioteca `unittest` para llevar a cabo los casos de prueba donde el programa debe correr casos que no son muy comunes y si no se tratan de forma diferente pueden causar errores.

**ErrorCaseTest.py**:

En este archivo se usa la biblioteca `unittest` para llevar a cabo los casos de prueba donde el programa debe fallar, cuando el usuario ingrese datos erróneos.

**Console.py**:

Esta es la interfaz por consola, donde el usuario interactúa con el programa sin ver el código fuente.

El código utiliza la biblioteca estándar de Python, `math`, que proporciona funciones matemáticas básicas, como la función `trunc()` utilizada para truncar valores decimales. Esta biblioteca es fundamental para realizar cálculos precisos dentro del programa, como calcular porcentajes o redondear valores según sea necesario.

Además, el código hace uso de la biblioteca `unittest`, que es un marco de pruebas unitarias integrado en Python. Las pruebas unitarias son esenciales para verificar la corrección del código y garantizar su funcionamiento esperado a medida que se realizan cambios o actualizaciones en el proyecto.

# Estructura sugerida:

* Carpeta MonthlyPayment: Carpeta en la cual se guarda la lógica del proyecto.
* Carpeta test: Carpeta en la cual se guardan las pruebas unitarias.
* Carpeta console: Carpeta en la cual estará la interfaz con la cual el usuario podrá manejar el código sin ver el código fuente.

# Como ejecutar la interfaz gráfica

1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Luego en esta carpeta abra una terminal de Git y pega el siguiente codigo `git init`

3) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

4) Ahora en la terminal copia  `cd Calculadora_de_nomina`

5) ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/Gui/Interfaz.py`

# Como ejecutar las pruebas unitarias
1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Luego en esta carpeta abra una terminal de Git y pega el siguiente codigo `git init`

3) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

4) Ahora en la terminal copia  `cd Calculadora_de_nomina`

Dependiendo del caso de prueba se copia lo siguiente:
5) Casos normales: ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/test/MonthlyPaymentTest.py`
6) Casos extraordinarios: ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/test/ExtraordinaryCasesTest.py`
7) Casos de error: ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/test/ErrorCaseTest.py`

# Como ejecutar la interfaz por consola

1) Dirijase a la pantalla de escritorio y en ese lugar cree una carpeta con el nombre: <Calculadora_de_nomina>

2) Luego en esta carpeta abra una terminal de Git y pega el siguiente codigo `git init`

3) Ahora copia  `git clone https://github.com/Tmurillo23/Liquidador_para_nomina.git`

4) Ahora en la terminal copia  `cd Calculadora_de_nomina`

5) ahora copia el siguiente codigo en la terminal `python ./Liquidador_para_nomina/src/Console/Console.py`