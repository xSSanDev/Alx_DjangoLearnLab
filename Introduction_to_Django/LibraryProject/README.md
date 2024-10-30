# LibraryProject

LibraryProject is a web application built using Django, a high-level Python web framework. This project serves as an introduction to Django and demonstrates the basic setup and configuration of a Django project.

## Features

- Admin interface for managing the application
- User authentication and authorization
- Basic CRUD operations
- SQLite database integration

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/LibraryProject.git
    ```
2. Navigate to the project directory:
    ```sh
    cd LibraryProject
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Apply migrations:
    ```sh
    python manage.py migrate
    ```
2. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```
3. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.