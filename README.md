# TaskManager API

## 📌 Descripción

Este proyecto es una API y aplicación web de productividad para la gestión de tareas. Permite a los usuarios crear, modificar, eliminar y organizar tareas con funcionalidades avanzadas como temporizador, historial y gráficas.

## 🚀 Tecnologías Utilizadas

- **Backend:** Django REST Framework (DRF)
- **Base de Datos:** MySQL en Amazon RDS
- **Infraestructura:** Docker y Docker Compose
- **Pruebas:** Unitarias e integración con Django TestCase y Postman

---

## 📂 Instalación y Configuración

### 1️⃣ **Clonar el repositorio**

```bash
 git clone https://github.com/tuusuario/taskmanager.git
 cd taskmanager
```

### 2️⃣ **Construir y levantar los contenedores con Docker**

```bash
 docker-compose up -d --build
```

### 3️⃣ **Aplicar migraciones a la base de datos**

```bash
 docker exec -it django_app python manage.py migrate
```

### 4️⃣ **Crear un superusuario para la administración**

```bash
 docker exec -it django_app python manage.py createsuperuser
```

### 5️⃣ **Verificar que la API está corriendo**

```bash
 curl http://localhost:8000/api/tasks/
```

---

## 📌 Endpoints de la API

| Método    | Endpoint                       | Descripción                        |
| --------- | ------------------------------ | ---------------------------------- |
| **POST**  | `/api/tasks/`                  | Crea una nueva tarea               |
| **GET**   | `/api/tasks/`                  | Obtiene todas las tareas           |
| **GET**   | `/api/tasks/?status=Pendiente` | Filtra tareas por estatus          |
| **PUT**   | `/api/tasks/{id}/`             | Modifica una tarea                 |
| **PATCH** | `/api/tasks/{id}/`             | Elimina lógicamente una tarea      |
| **PATCH** | `/api/tasks/{id}/complete/`    | Marca la tarea como completada     |

---

## ✅ Pruebas Automatizadas

### 1️⃣ **Ejecutar pruebas unitarias y de integración**

```bash
 docker exec -it django_app python manage.py test
```

### 2️⃣ **Cargar la Collection de Postman**

- Abre Postman.
- Importa el archivo `postman_collection.json`.
- Ejecuta las pruebas de los endpoints.

---

## 🌐 Despliegue en Producción (Opcional)

Puedes desplegar la aplicación en **Heroku** o un servidor con Docker.

### 📌 **Pasos para despliegue en Heroku**

```bash
 heroku container:login
 heroku create taskmanager-api
 heroku container:push web -a taskmanager-api
 heroku container:release web -a taskmanager-api
```

---

## 📜 Contribuciones

Si deseas contribuir, ¡eres bienvenido! 😊

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m "Agregada nueva funcionalidad"`).
4. Realiza un push a la rama (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

📌 **Autor:** Tu Nombre\
📧 **Contacto:** [tuemail@example.com](mailto\:tuemail@example.com)

