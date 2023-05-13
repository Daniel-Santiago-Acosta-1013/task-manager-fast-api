# Task Manager en FastAPI

## Descripción
Este proyecto implementa un sistema de gestión de tareas utilizando el framework FastAPI.

## Configuración del entorno

Para instalar y configurar el entorno, realice los siguientes pasos:

1. Clonar el repositorio:

    ```
    git clone https://github.com/Daniel-Santiago-Acosta-1013/task-manager-fast-api
    ```
2. Instalar dependencias:

    ```
    pip install -r requirements.txt
    ```

## Cómo ejecutar la aplicación

- Para ejecutar la aplicación, utilice el comando uvicorn como se muestra a continuación:

    ```
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

## Documentación

Una vez que el servidor esté en marcha, se puede acceder a la documentación de la API de dos maneras:

- Navegando a `http://localhost:8000/docs` para la documentación de Swagger UI.
- Navegando a `http://localhost:8000/redoc` para la documentación de ReDoc.

## Contribuir

Las contribuciones son siempre bienvenidas. Consulte las [guías de contribución](CONTRIBUTING.md) para obtener más información.

## Licencia

Este proyecto está licenciado bajo los términos de la [Licencia MIT](LICENSE).


