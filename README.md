# Backend Analítico con Flask y MongoDB

Estructura base del proyecto backend organizada mediante arquitectura por capas para procesamiento y análisis de datos.

## Arquitectura por Capas

- **Routes**: Recibe solicitudes HTTP y expone los endpoints de la API.
- **Services**: Contiene la lógica del negocio, procesamiento de datos e indicadores.
- **Repositories**: Gestiona consultas y operaciones con MongoDB.
- **Models**: Define la estructura de los datos del sistema.
- **Database**: Administra la conexión con MongoDB.
- **Schemas**: Organiza y valida la estructura de los datos de entrada y salida.
- **Config**: Centraliza configuraciones y variables del sistema.
- **Main.py**: Inicializa la aplicación Flask y registra los componentes principales.

## Requisitos e Instalación

1. Crear y activar el entorno virtual:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```powershell
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```powershell
   python -m app.main
   ```

4. Probar la API en `http://127.0.0.1:5000/`
