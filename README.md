# Python-Django-PostgreSQL-Cancha

Aplicación web para la gestión y alquiler de canchas deportivas. La aplicación permite a los usuarios buscar, reservar y valorar canchas, así como gestionar sus propias reservas y perfiles. Además, proporciona funcionalidades administrativas para gestionar usuarios, canchas, reservas y comentarios.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)

## Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (versión 3.12.2)
- PostgreSQL (versión 16)
- pip (administrador de paquetes de Python)

### Pasos de Instalación

1. **Clona este repositorio:**

```bash
git clone https://github.com/JohannGaviria/Python-Django-PostgreSQL-Cancha.git
```

2. **Crear el entorno virtual:**

Utiliza `virtualenv` o otro gestor de entornos virtuales

```bash
pip install virtualenv
python -m virtualenv nombre_del_entorno
```

3. **Instalar las dependencias:**

```bash
cd Python-Django-PostgreSQL-Cancha
pip install -r requirements.txt
```

4. **Configurar la base de datos:**

- Crea una base de datos PostgreSQL en tu entorno.
- Crea un archivo `.env` en la ruta raiz de tu proyecto y crea las variables de entorno con los datos correpodientes:
    - SECRET_KEY=tu_clave_secreta
    - ENGINE=tu_base_de_datos
    - NAME=tu_nombre_de_la_base_de_datos
    - USER=tu_usuario_de_la_base_de_datos
    - PASSWORD=tu_contraseña_de_la_base_de_datos
    - HOST=tu_host
    - PORT=tu_port

5. **Crea las migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crea los roles por defecto:**

```bash
python manage.py create_default_rol
```

7. **Ejecutar el servidor:**

```bash
python manage.py runserver
```

¡Listo! El proyecto ahora debería estar en funcionamiento en tu entorno local. Puedes acceder a él desde tu navegador web visitando `http://localhost:8000`.

## Uso

1. Ejecuta el servidor de desarrollo: 

```
python manage.py runserver
```

2. Accede a la API a través de las URL definidas.

## API Endpoints

### Crear nuevo usuario

```http
POST /api/auth/signUp
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `full_name` | `string` | **Requerido**. Nombre completo del usuario |
| `email` | `string` | **Requerido**. Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |
| `phone` | `string` | **Requerido**. Numero celular del usuario |
| `birth_date` | `string` | **Requerido**. Fecha de nacimiento del usuario |
| `rol` | `int` | **Requerido**. Rol del usuario|

#### Registro de un nuevo usuario

```http
POST /api/auth/signUp
Content-Type: application/json

{
	"full_name": "test fullname",
	"email": "test@email.com",
	"password": "testpassword",
	"phone": "+57 321 987 6543",
	"birth_date": "1999-09-09",
	"rol": 2
}
```

#### Respuesta exitosa al registro

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Successful registration",
	"data": {
		"token": {
			"token_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		},
		"user": {
			"id": 1,
			"full_name": "test fullname",
			"email": "test@email.com",
			"phone": "+57 321 987 6543",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": false,
			"is_superuser": false,
			"rol": 2
		}
	}
}
```

### Inciar sesión de usuario

```http
POST /api/auth/signIn
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Requerido**. Email del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

#### Inicio de sesión de un usuario

```http
POST /api/auth/signIn
Content-Type: application/json

{
	"email": "test@email.com",
	"password": "testpassword"
}
```

#### Respuesta exitosa al inicio de sesión

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "succes",
	"message": "Successful login",
	"data": {
		"token": {
			"token_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
			"token_expiration": "2024-06-10T02:27:34.039747Z"
		},
		"user": {
			"id": 1,
			"full_name": "test fullname",
			"email": "test@email.com",
			"phone": "+57 321 987 6543",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": false,
			"is_superuser": false,
			"rol": 2
		}
	}
}
```

### Cierre de sesión

```http
GET /api/auth/signOut
```

### Cerrar sesión de usuario

```http
GET /api/auth/signOut
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**. Token de autenticación |

#### Cierre de sesión de un usuario

```http
GET /api/user/signOut
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Respuesta exitosa al cierre de sesión

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
	"status": "succes",
	"message": "Successful logout"
}
```

### Crear nuevo usuario

```http
POST /api/auth/signUp
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `full_name` | `string` | Nombre completo del usuario |
| `email` | `string` |. Correo electrónico del usuario |
| `password` | `string` |. Contraseña del usuario |
| `phone` | `string` |. Numero celular del usuario |
| `birth_date` | `string` |. Fecha de nacimiento del usuario |
| `rol` | `int` |. Rol del usuario|

#### Registro de un nuevo usuario

```http
POST /api/users/update
Content-Type: application/json
Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

{
	"full_name": "test new fullname",
	"email": "testnew@email.com",
	"password": "testnewpassword",
	"phone": "+57 321 987 6543",
	"birth_date": "1999-09-09",
	"rol": 2
}
```

#### Respuesta exitosa al registro

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Successful update",
	"data": {
		"token": {
			"token_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
			"token_expiration": "2024-06-10T20:37:44.026227Z"
		},
		"user": {
			"id": 1,
			"full_name": "test new fullname",
			"email": "testnew@email.com",
			"phone": "+57 320 476 9010",
			"birth_date": "1999-09-09",
			"is_active": true,
			"is_staff": false,
			"is_superuser": false,
			"rol": 2
		}
	}
}
```