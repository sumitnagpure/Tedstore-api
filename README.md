# Tedstore-api

app

- product-master details
- customer-details

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sumitnagpure/Tedstore-api.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Database Setup:**

    - Ensure you have a compatible database installed (e.g., PostgreSQL, SQLite, MySQL).
    - Configure the database settings in `settings.py`.

4. **Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Usage

1. **Running the Development Server:**

    ```bash
    python manage.py runserver
    ```

2. **Accessing the Application:**

    - Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a pull request

