User Management API

Backend Assessment Project

📌 Overview

This project is a User Management REST API built using Django REST Framework, implementing authentication, authorization, role management, and CRUD operations for users.

The system supports:

User Registration

User Login with JWT Tokens

List All Users (Admin Only)

Retrieve Single User

Update User

Delete User

Role Management (User / Admin)

Data Validation

JWT Authentication

Database: SQLite (configurable)

📌 Technologies Used

Python 3

Django

Django REST Framework

SimpleJWT

SQLite

Postman (for testing)

📌 API Endpoints Documentation
🔐 Authentication
1️⃣ Register User

POST /api/register/
http://127.0.0.1:8000/api/register/?Content-Type=application/json
Request Body:
{
  "username": "abood",
  "email": "abood@test.com",
  "password": "Test1234",
  "confirm_password": "Test1234",
  "first_name": "Abd",
  "last_name": "Salam",
  "role": "user"
}

Response JSON Body: 
{
    "message": "User registered successfully"
}

{
  "username": "ali",
  "email": "ali@test.com",
  "password": "abcdefgh",
  "confirm_password": "abcdefgh",
  "first_name": "ali",
  "last_name": "Salam",
  "role": "user"
}



{
    "non_field_errors": [
        "Password must contain a number."
    ]
}


 

{
  "username": "tala",
  "email": "",
  "password": "abcdefgh",
  "confirm_password": "abcdefgh",
  "first_name": "tala",
  "last_name": "ali",
  "role": "user"
}


{
    "email": [
        "This field may not be blank."
    ]
}


{
  "username": "tala",
  "email": "ali@test.com",
  "password": "abc22defgh",
  "confirm_password": "abc22defgh",
  "first_name": "tala",
  "last_name": "ali",
  "role": "user"
}


{
    "non_field_errors": [
        "Password must contain a capital letter."
    ]
}


{
  "username": "sami",
  "email": "ali@test.com",
  "password": "abc22Defgh",
  "confirm_password": "abc22Defgh",
  "first_name": "tala",
  "last_name": "ali",
  "role": "user"
}



{
    "email": [
        "user with this email already exists."
    ]
}


2️⃣ Login

POST /api/login/
http://127.0.0.1:8000/api/login/
Request Body:
{
  "email": "ali@test.com",
  "password": "abc22Defgh"
}
{
    "message": "Login successful",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1MzcxOTUxLCJpYXQiOjE3NjUzNzE2NTEsImp0aSI6ImJjYzJkYTU2MTFjYjQzZThiNWM4NzFlN2RiMTAxODEwIiwidXNlcl9pZCI6IjIifQ.O6o2L_Tmr3-ZmjSQ7jFD1Ye5vvJhEG56G40nHyGOR-s",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2NTQ1ODA1MSwiaWF0IjoxNzY1MzcxNjUxLCJqdGkiOiJjYmU3MGQzYTdkMWM0NTlhYTkzNTUzZGNjODgxYTY4OSIsInVzZXJfaWQiOiIyIn0.JS6VOJ3dMdzZLnomfH9H7_EyR6_SqW45iIs5973qgHU",
    "role": "user",
    "email": "ali@test.com"
}

{
  "email": "souad@test.com",
  "password": "abc22Defgh"
}

{
    "non_field_errors": [
        "Invalid email or password."
    ]
}


👥 User Endpoints
3️⃣ Get All Users (Admin Only)

GET /api/users/
http://127.0.0.1:8000/api/users/ 

Requires:
Authorization: Bearer <access_token>
[
    {
        "id": 1,
        "username": "abood",
        "email": "abood@test.com",
        "role": "user",
        "is_staff": false
    },
    {
        "id": 2,
        "username": "tala",
        "email": "ali@test.com",
        "role": "user",
        "is_staff": false
    },
    {
        "id": 3,
        "username": "souad",
        "email": "souad@admin.com",
        "role": "user",
        "is_staff": true
    },
    {
        "id": 4,
        "username": "souad1234",
        "email": "souad1234@admin.com",
        "role": "admin",
        "is_staff": false
    }
]
 
4️⃣ Get User by ID

GET /api/users/<id>/
Requires authentication
http://127.0.0.1:8000/api/users/5/

{
    "username": "souad1234",
    "email": "souad1234@admin.com",
    "role": "admin",
    "is_staff": true
}

5️⃣ Update User

PUT /api/users/<id>/
http://127.0.0.1:8000/api/users/5/

Allowed when:

The authenticated user is updating their own account, or

The authenticated admin is updating any user

Request Body:
    {
        "id": 5,
        "username": "souad1234",
        "email": "souad1234@admin.com",
        "password" : "Souad1234",
        "role": "admin",
        "is_staff": true
    }

{
    "message": "User updated successfully"
}

6️⃣ Delete User

DELETE /api/users/<id>/
http://127.0.0.1:8000/api/users/3/

Allowed for:

Admin only

{
    "message": "User deleted successfully"
}

🛡 Validation Rules

All fields are required

Email must be valid

Password must contain:

Minimum 8 characters

At least 1 uppercase letter

At least 1 number

Password fields must match

Role must be either user or admin

👑 Role Management

The system supports two main roles:

Role	Permissions
User	Can view & update only their own account
Admin	Can view, update, and delete any user
🧪 Postman Collection

A full Postman collection is included inside the project:

project_root/
   └── postman_collection.json


Import this file in Postman to test all endpoints easily.

📦 Installation & Running the Project
1️⃣ Clone the repository
git clone https:https://github.com/souadroumani/User-Management-API.git
cd User-Management-API

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Migrations
python manage.py migrate

4️⃣ Start the Server
python manage.py runserver