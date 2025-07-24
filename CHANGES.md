
# Messy Migration

  

## Project Setup

  

In the root directory, run:

  

```bash
cd  messy-migration

pip  install  -r  requirements.txt

python  init_db.py

python  app.py

```

  

---

  

## 1. Code Organization

  

### Folders

  

-  `services/` — All individual API services.

-  `helpers/` — Helper functions:

-  `auth.py` — for JWT token authentication.

-  `db.py` — for getting the database connection instance.

-  `tests/` — Unit tests for all API checks.

  

### Main Files

  

-  `app.py` — Main file that binds all APIs and launches the server.

-  `init_db.py` — Initializes the database before running the app.

(These files function the same as before.)

  

---

  

##  2. Security Improvements

  

-  **DB Connection Handling**: Previously, a single thread was shared across all API queries, which is not ideal. Now, each API service (e.g. `create_user`) establishes its own database connection before querying. This avoids memory or data leaks during deployment.

  

-  **Parameterized Queries**: All SQL queries are now parameterized to avoid SQL injection.

  

-  **Password Hashing**: Passwords are now hashed before storage, preventing plain-text handling.

  

-  **JWT Authentication**:

	- Only the `createUser` endpoint does not require a JWT token.

	- All other endpoints (`getAllUsers`, `getUser`, `deleteUser`, `searchUser`) require a valid JWT token passed in the headers, to make any successful API call. This prevents any unauthorized access.

  

Example:

  

```http

GET /users

Authorization: Bearer <token>

```

  

_I could have added admin and user role-based tokens for specific API access, but that is beyond the scope of this assessment._

  

---

  

## 3. Best Practices

  

-  **HTTP Status Codes** — Consistent use of `200`, `201`, `400`, `401`, `404`, `409`, and `500`.

  

-  **Code Reusability** — Shared use of `auth.py` and `db.py` across service files.

  

---

  

## Testing

  

### Unit Tests with `pytest`

  

- Implemented using `pytest` and Flask's test client.

	- Covers:

	- User registration

	- Login + JWT

	-  `GET`, `PUT`, `DELETE`  `/user/<id>`

	-  `GET /users` with pagination

	-  `GET /search`

  
To run the unit tests run the following command in terminal from root directory

```bash

pytest  tests/

```

  

---

  

##  Help from AI Chatbots (mostly ChatGPT)

  

-  `auth.py` and the `tests/` folder were written with help from GPT.

- Try-except blocks with proper status codes were also written with GPT assistance.

  

---

  

##  Trade-offs in New Architecture

  

- Each API call creates a new DB instance. For high-frequency APIs, this could become costly in terms of thread creation and memory use.

- In production, an in-memory DB like Redis may be better suited.

  

---

  

##  If More Time Was Available

  

- Implement role-based tokens (e.g. admin vs user) and refresh tokens.
- Add query params for searching like ORDER BY for ascending / descending order etc. as per use case.

- Add test cases for invalid/malformed tokens.

- Use in-memory DB for high-performance environments.

- Handle front-end integration for setting authentication headers.

- Handle CORS properly for cross-origin requests in deployment.
