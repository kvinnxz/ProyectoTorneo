# **PROYECTO GESTOR DE TORNEOS BASICO EN PYTHON**

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ESTRUCTURA

```
├── controllers
│   ├── cuerpotecnico.py
│   ├── equipos.py
│   ├── estadisticas.py
│   ├── jugadores.py
│   ├── partidos.py
│   ├── torneos.py
│   └── transferencias.py
├── data
│   ├── cuerpotecnico.json
│   ├── equipos.json
│   ├── estadisticas.json
│   ├── jugadores.json
│   ├── partidos.json
│   ├── torneos.json
│   └── transferencias.json
├── utils
│   ├── helpers.py
│   └── validadores.py
└── menPrin.py
```



## DESCRIPCION GENERAL DEL PROYECTO

Este proyecto es una aplicación en consola que permite gestionar torneos de fútbol de manera sencilla. Está diseñada como una herramienta básica pero funcional que facilita el registro, organización y consulta de información relacionada con equipos, jugadores, cuerpo técnico y partidos. Todo el sistema se opera mediante un menú interactivo por consola, lo que permite al usuario navegar entre distintas opciones sin necesidad de conocimientos avanzados en interfaces gráficas o bases de datos.

## PROPOSITOS Y FUNCIONALIDAD ESPECIFICA

Su propósito principal es brindar una forma práctica de organizar datos relacionados al fútbol sin depender de bases de datos externas ni configuraciones complicadas. El sistema funciona con archivos JSON, lo que permite guardar toda la información directamente en el computador del usuario sin configuraciones adicionales.

Actualmente permite realizar operaciones básicas como:

- Registrar y listar equipos, jugadores y cuerpo técnico.
- Eliminar registros en caso de ser necesario.
- Crear torneos e inscribir equipos participantes.
- Registrar partidos jugados.
- Visualizar una tabla de posiciones por torneo en la sección de estadísticas.
- Realizar transferencias de jugadores entre equipos.

El proyecto busca representar una forma simple pero ordenada de manejar información deportiva desde la terminal. Por ahora se enfoca en funcionalidades esenciales, pero tiene una estructura clara y modular que permite seguir desarrollándolo y adaptarlo según nuevas ideas o necesidades.

Para poder ejecutar este programa se debe hacer desde :

```
menPrin.py
```

 Así mismo se asegura su correcta funcionalidad

