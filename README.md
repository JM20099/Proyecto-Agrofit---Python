
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)


Sistema en Python conectado a MySQL para la gestión de acondicionamiento físico, asignación de rutinas personalizadas y seguimiento de métricas corporales para aprendices, funcionarios y entrenadores.
---

🏋️‍♂️ AGROFIT — Gestor de Rutinas y Seguimiento Deportivo
📁 Estructura del Proyecto
```text
📁 proyecto_agrofit/
│
├── 📁 usuarios/
│   ├── 📄 conexion.py          # Conexión parametrizada a MySQL
│   ├── 📄 usuario.py           # Modelo de usuario y registro multi-rol 
│   └── 📄 acciones.py          # Flujo de registro y login
│
├── 📁 inicio/
│   ├── 📄 rutina.py            # Operaciones SQL: rutinas, ejercicios, músculos y progreso
│   └── 📄 acciones.py          # Panel interactivo para el Entrenador
│
└── 📁 inicio_usuario/
    ├── 📄 inicio.py            # Consultas de perfil para Aprendices/Funcionario
    └── 📄 acciones.py          # Visualización de rutinas y progresos del usuario
```
---
👥 Roles del Sistema
Rol	Requisitos de Acceso	Funcionalidades
🥇 Entrenador	Registro con especialidad técnica	Crear rutinas, agregar ejercicios/máquinas, asignar rutinas con fecha/hora y registrar progreso físico.
🥈 Aprendiz	Ficha activa + correo `@sena.edu.co`	Consultar la rutina asignada (series/repeticiones) y visualizar el historial de métricas corporales.
🥉 Funcionario	Vinculación por dependencia/centro	Registro según tipo de contrato (Planta o Contratista) y acceso a consulta de perfil.
---
🚀 Funcionalidades Principales
Autenticación y Seguridad:
Cifrado de contraseñas con algoritmo SHA-256.
Validaciones estrictas de correo institucional para aprendices.
Manejo de transacciones seguras (`commit` / `rollback`).
Constructor de Rutinas y Ejercicios:
Catálogo dinámico de partes del cuerpo, músculos y máquinas.
Creación de ejercicios con series, repeticiones y enlaces a recursos (videos/imágenes).
Asignación de rutinas según nivel de dificultad.
Asignación y Seguimiento Biométrico:
Asignación de rutinas por correo institucional indicando fecha, hora y observaciones.
Control y auditoría de progreso físico: peso (Kg), altura (m) y porcentaje de grasa corporal (%).
---
