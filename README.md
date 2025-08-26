# myproject3
# 🛒 Django Products Management Project  

## 📌 Description  A simple 
**Django web application** built as a practice project. The main goal of this project is to learn:  
* How to create a Django project & apps.
* * Using **HTML Template Inheritance** (`base.html`).
* * Connecting **Models** with a database.
* * Managing data through the **Django Admin Panel**.
* * Applying a **Dark Style** design with custom CSS.  The project allows users (via admin panel) to:
* * Add new products (name, price, description). * View products on a public page (`/products/`).
* * Display a clean **dark-themed interface** with reusable templates.  ---  ## ⚙️ Features  * Django project setup with a custom app (`products`). * Template inheritance using `base.html`.
* * Product model with name, description, price, and created date.
* * Admin panel integration to manage products.
* * Dark theme styling using CSS.
* * Product list page (`/products/`) that shows products if available, otherwise displays a "No products available" message.
* * Security: **SECRET\_KEY is removed from settings.py**, and must be set manually as an environment variable.
## 🔑 Setting up SECRET\_KEY  For security reasons, the `SECRET_KEY` is not included in the repository. You need to set it up manually before running the project.
    1. Open your terminal and set the environment variable:     * On **Windows (PowerShell):**       ```bash      setx DJANGO_SECRET_KEY "your-secret-key-here"      ```    * On **Linux/Mac:**       ```bash      export DJANGO_SECRET_KEY="your-secret-key-here"      ```
       2. In `settings.py`, replace the old key with this code:     ```python    import os     SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "fallback-secret-key")    ```     * `"DJANGO_SECRET_KEY"` → يجيب المفتاح من environment.
## 🛠️ Technologies Used
* **Python 3.13** * **Django 5.2.5** * **SQLite3** (default database) * **HTML5 / CSS3** *
## 🚀 How to Run
1. Clone the repository:     ```bash    git clone https://github.com/your-username/products-management.git    cd products-management    ```
2. Create a virtual environment and activate it.
3. Install dependencies:     ```bash    pip install -r requirements.txt    ```
4. Set your **SECRET\_KEY** (see instructions above).
5. Apply migrations:     ```bash    python manage.py migrate    ```
6. Create a superuser (for admin panel):     ```bash    python manage.py createsuperuser    ```
7. Run the development server:     ```bash    python manage.py runserver    ```
8. Open in browser:     * Home Page → `http://127.0.0.1:8000/`    * Products Page → `http://127.0.0.1:8000/products/`    * Admin Panel → `http://127.0.0.1:8000/admin/`  ---   
