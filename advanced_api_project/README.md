# API Documentation

## Book API Endpoints

### List Books
- **URL:** `/api/books/`
- **Method:** `GET`
- **Permissions:** Public

### Retrieve Book
- **URL:** `/api/books/<int:pk>/`
- **Method:** `GET`
- **Permissions:** Public

### Create Book
- **URL:** `/api/books/create/`
- **Method:** `POST`
- **Permissions:** Authenticated Users

### Update Book
- **URL:** `/api/books/<int:pk>/update/`
- **Method:** `PUT`
- **Permissions:** Authenticated Users

### Delete Book
- **URL:** `/api/books/<int:pk>/delete/`
- **Method:** `DELETE`
- **Permissions:** Authenticated Users

## Custom Settings and Hooks

### Custom Create Logic
In `BookCreateView`, the `perform_create` method is overridden to include custom logic before saving the instance.

### Custom Update Logic
In `BookUpdateView`, the `perform_update` method is overridden to include custom logic before updating the instance.curl -X GET curl -X GET 