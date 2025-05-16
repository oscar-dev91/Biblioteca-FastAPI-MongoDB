# 🚀 **API Biblioteca - MongoDB**

Una API REST desarrollada con **FastAPI** y conectada a **MongoDB**, que permite gestionar los distintos elementos de una biblioteca: libros, revistas, DVDs y otros recursos.

Este sistema permite la administración completa de los siguientes recursos:
- 📚 Libros
- 📰 Revistas
- 💿 DVDs
- 📦 Elementos generales de la biblioteca

---

## 🚀 ¿Qué puedes hacer con esta API?

- 📘 Registrar, consultar, actualizar y eliminar **libros**.
- 📀 Manejar información de **DVDs**.
- 📰 Gestionar **revistas**.
- 🧱 Manipular **elementos generales de biblioteca**.
- 🔍 Buscar por título en todos los recursos.

## 🔌 **Rutas incluidas:**
- `/libros`: Endpoints para gestión de libros.
- `/revistas`: Endpoints para gestión de revistas.
- `/dvds`: Endpoints para gestión de DVDs.
- `/elementos`: Endpoints para listar o buscar cualquier tipo de elemento.

## 🗂️ Estructura del Proyecto

```bash
biblioteca_mongodb/
│
├── main.py                   # Punto de entrada de la aplicación FastAPI
├── database.py               # Conexión a MongoDB
├── .env                      # Variables de entorno (URI MongoDB, etc.)
│
├── crud/                     # Operaciones CRUD con la base de datos
│   ├── dvd.py
│   ├── elemento.py
│   ├── libro.py
│   └── revista.py
│
├── models/                   # Modelos de datos Pydantic usados internamente
│   ├── dvd.py
│   ├── elemento.py
│   ├── libro.py
│   └── revista.py
│
├── routers/                  # Rutas de la API organizadas por recurso
│   ├── dvd.py
│   ├── elemento.py
│   ├── libro.py
│   └── revista.py
│
├── schemas/                  # Esquemas de validación para la entrada/salida
│   ├── dvd.py
│   ├── libro.py
│   └── revista.py
│
└── services/                 # Lógica de negocio separada de los routers
    ├── dvd.py
    ├── elemento.py
    ├── libro.py
    └── revista.py
```
## ▶️ Cómo ejecutar el proyecto
1. 📦 Instalar dependencias

Asegúrate de tener Python 3.10+ instalado. Luego ejecuta:
```bash
pip install -r requirements.txt
```
2. ⚙️ Configurar variables de entorno

Crea un archivo .env en la raíz del proyecto con la siguiente variable (ejemplo):
```yaml
MONGODB_URI=mongodb+srv://usuario:contraseña@tucluster.mongodb.net/biblioteca
```
3. 🚀 Ejecutar la API

Usa uvicorn para iniciar el servidor FastAPI:
```
uvicorn main:app --reload
```
4. 🌐 Probar la API en el navegador

Una vez iniciado el servidor, puedes ir a:
* Documentación interactiva (Swagger): http://127.0.0.1:8000/docs
* Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc

## 🧠 Tecnologías usadas
* FastAPI – para crear la API.
* MongoDB – como base de datos NoSQL.
* Pydantic – para validación de datos.
* Motor – cliente asincrónico para MongoDB.
* Uvicorn – servidor ASGI para desarrollo local.