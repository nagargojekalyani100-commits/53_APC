DJANGO LOGIN PROJECT WITH VALIDATION

1. Extract this ZIP file.
2. Open the extracted loginDjango_correct folder in VS Code.
3. Open the terminal in that folder (the folder containing manage.py).
4. Optional but recommended: create and activate a virtual environment:
   Windows:
     py -m venv venv
     venv\Scripts\activate
5. Install dependencies:
     py -m pip install -r requirements.txt
6. Create database tables:
     py manage.py migrate
7. Create a login user:
     py manage.py createsuperuser
   Enter a username and password when prompted. Use a username with 3–20 letters,
   numbers or underscores, and a password of at least 8 characters.
8. Start the server:
     py manage.py runserver
9. Open http://127.0.0.1:8000/

The login form authenticates Django users. It does not automatically create a user.
Use the superuser you create in step 7, or create a normal user through Django admin.

Validation:
- Username: 3–20 letters, digits, or underscores.
- Password: at least 8 characters.
- CSRF protection is enabled.
- Home page requires login.
