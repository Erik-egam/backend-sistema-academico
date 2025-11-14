<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">


# BACKEND-SISTEMA-ACADEMICO

<em>Empowering Education Through Seamless Digital Innovation</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/Erik-egam/backend-sistema-academico?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/Erik-egam/backend-sistema-academico?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/Erik-egam/backend-sistema-academico?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## 📄 Table of Contents

- [Overview](#-overview)
- [Getting Started](#-getting-started)
    - [Prerequisites](#-prerequisites)
    - [Installation](#-installation)
    - [Usage](#-usage)
    - [Testing](#-testing)
- [Project Structure](#-project-structure)
    - [Project Index](#-project-index)
- [Acknowledgment](#-acknowledgment)

---

## ✨ Overview

backend-sistema-academico is a comprehensive backend solution built with FastAPI, tailored for educational institutions to manage users, courses, grades, and academic programs efficiently. Its modular design ensures maintainability and scalability, making it ideal for developing robust academic management platforms.

**Why backend-sistema-academico?**

This project aims to simplify the development of educational management systems by providing a secure, scalable, and well-structured backend. The core features include:

- **🛠️ Role-Based API Endpoints:** Secure access for students, teachers, and admins with role-specific functionalities.
- **📚 Data Models for Academic Entities:** Structured representations for courses, programs, semesters, and grades.
- **🌐 FastAPI & MySQL Integration:** High-performance API with reliable database support.
- **🔒 Authentication & Authorization:** Built-in user management with JWT tokens for secure sessions.
- **🧩 Modular Architecture:** Clear separation of concerns for routes, models, and core logic.
- **🚀 Seed Data & Configurations:** Ready-to-use setup for initial deployment and testing.

---

## 📁 Project Structure

```sh
└── backend-sistema-academico/
    ├── inserts_pruebas.txt
    ├── main.py
    ├── models
    │   ├── Admin_functions.py
    │   ├── Asignatura.py
    │   ├── Notas.py
    │   ├── Programa.py
    │   ├── Semestre.py
    │   ├── Usuario.py
    │   ├── __pycache__
    │   ├── config.py
    │   ├── estudiantes_functions.py
    │   └── profesor_functions.py
    ├── requirements.txt
    └── routes
        ├── __pycache__
        ├── admin.py
        ├── estudiantes.py
        ├── profesores.py
        └── usuarios.py
```

---

### 📑 Project Index

<details open>
	<summary><b><code>BACKEND-SISTEMA-ACADEMICO/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>- Establishes the main entry point for the FastAPI application, configuring core middleware and integrating route modules for user management, administration, students, and teachers<br>- Facilitates seamless API routing and cross-origin resource sharing, serving as the central hub that orchestrates the applications endpoints and ensures smooth communication across different user roles within the overall system architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Defines project dependencies essential for building a secure, scalable FastAPI application with MySQL integration<br>- Facilitates authentication, password hashing, and multipart data handling, supporting core functionalities such as user management and data processing within the overall architecture<br>- Ensures consistent environment setup for development and deployment, aligning with the systems modular and service-oriented design.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/inserts_pruebas.txt'>inserts_pruebas.txt</a></b></td>
					<td style='padding: 8px;'>- Defines the foundational data structures and seed data for an educational management system, establishing roles, programs, users, semesters, courses, enrollments, and grades<br>- Supports core functionalities such as user authentication, course registration, and academic performance tracking, enabling a comprehensive platform for managing university operations and student progress within the broader application architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- models Submodule -->
	<details>
		<summary><b>models</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ models</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/Asignatura.py'>Asignatura.py</a></b></td>
					<td style='padding: 8px;'>- Defines data models for academic subjects within the application, enabling structured representation and validation of course information<br>- Facilitates seamless data handling for course management features, supporting interactions with other system components such as program associations and course catalog functionalities<br>- Ensures consistent data integrity and clarity across the codebase related to academic offerings.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/profesor_functions.py'>profesor_functions.py</a></b></td>
					<td style='padding: 8px;'>- Provides core functionalities for managing university courses, students, and grades within the academic system<br>- Facilitates retrieval of current courses taught by a professor, lists enrolled students in a course, and handles student grade records<br>- Integrates seamlessly into the broader architecture to support academic administration and instructor workflows.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/Notas.py'>Notas.py</a></b></td>
					<td style='padding: 8px;'>- Defines the data model for student grades and attendance, enabling structured validation and management of academic records within the application<br>- Facilitates consistent data handling for subjects, grades, and attendance metrics, supporting the overall architectures focus on accurate and reliable educational data processing.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/Programa.py'>Programa.py</a></b></td>
					<td style='padding: 8px;'>- Defines data models for representing program entities within the application architecture<br>- The Programa model captures essential program details such as name and description, while InfoPrograma extends this with a unique identifier, facilitating data validation, serialization, and seamless integration across different system components<br>- These models underpin consistent data handling throughout the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/estudiantes_functions.py'>estudiantes_functions.py</a></b></td>
					<td style='padding: 8px;'>- Provides core functionalities for managing student academic records, including course enrollment, retrieving semester histories, fetching grades, and listing enrolled subjects<br>- Integrates with the database to support student progress tracking within the broader educational platform architecture, enabling seamless access and manipulation of student-related academic data.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/Admin_functions.py'>Admin_functions.py</a></b></td>
					<td style='padding: 8px;'>- Provides administrative functionalities for managing users, programs, courses, and semesters within the platform<br>- Facilitates creation, activation, deactivation, and assignment of roles, as well as retrieving detailed information about academic structures and personnel, ensuring seamless integration and data consistency across the educational architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/Usuario.py'>Usuario.py</a></b></td>
					<td style='padding: 8px;'>- Defines user data models for the application, facilitating structured representation of user information and database interactions<br>- The models support validation, serialization, and data consistency across the system, enabling seamless handling of user-related data throughout the project architecture<br>- These models serve as the foundation for user management, authentication, and authorization processes within the overall system.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/Semestre.py'>Semestre.py</a></b></td>
					<td style='padding: 8px;'>- Defines the Semestre data model to represent academic semester details within the application<br>- It facilitates structured data handling for semester attributes such as name, start date, and end date, supporting validation and serialization across the system<br>- This model integrates into the broader architecture to manage and process semester-related information efficiently.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/models/config.py'>config.py</a></b></td>
					<td style='padding: 8px;'>- Establishes database connection parameters and provides a function to initiate a connection to the academic systems MySQL database<br>- Facilitates seamless data access and manipulation across the application, supporting core functionalities such as user management, course handling, and record keeping within the overall system architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- routes Submodule -->
	<details>
		<summary><b>routes</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ routes</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/routes/estudiantes.py'>estudiantes.py</a></b></td>
					<td style='padding: 8px;'>- Defines API endpoints for student-related operations, enabling authenticated students to access academic history, view enrolled and available courses, and manage course enrollments<br>- Integrates role-based access control to ensure only authorized students perform these actions, supporting the broader system architecture by facilitating student interactions within the educational platform.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/routes/admin.py'>admin.py</a></b></td>
					<td style='padding: 8px;'>- Defines administrative API endpoints for user, program, subject, and semester management within the FastAPI application<br>- Facilitates creation, activation, deletion, and assignment operations, ensuring only authorized admin users perform these actions<br>- Integrates with core admin functions to maintain and retrieve data related to users, academic programs, and course assignments, supporting overall system governance and data integrity.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/routes/usuarios.py'>usuarios.py</a></b></td>
					<td style='padding: 8px;'>- Provides user authentication and authorization functionalities within the application<br>- Manages user login, token generation, and validation processes, enabling secure access to protected endpoints<br>- Integrates database queries to retrieve user data and employs JWT tokens for session management, supporting a robust security layer aligned with the overall system architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend-sistema-academico/blob/master/routes/profesores.py'>profesores.py</a></b></td>
					<td style='padding: 8px;'>- Defines API endpoints for managing professor-related functionalities, including retrieving current courses, accessing student lists per course, viewing student grades, and recording new grades<br>- Integrates user authentication and role verification to ensure authorized access, facilitating seamless interaction between professors and academic data within the overall system architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 📋 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### ⚙️ Installation

Build backend-sistema-academico from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/Erik-egam/backend-sistema-academico
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd backend-sistema-academico
    ```

3. **Install the dependencies:**

**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt
```

### 💻 Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**

```sh
python {entrypoint}
```

### 🧪 Testing

Backend-sistema-academico uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**

```sh
pytest
```

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---
