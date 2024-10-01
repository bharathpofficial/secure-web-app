# Secure Web App

## Description

Secure Web App is a Django-based project focused on implementing and demonstrating secure web development practices. The project includes features for input handling and geo IP tracking, with a strong emphasis on security measures.

## Objective

The main objectives of this project are:

1. To showcase best practices in secure web application development using Django.
2. To implement and demonstrate input validation and sanitization techniques.
3. To integrate geo IP tracking functionality for enhanced security and user analytics.
4. To serve as a learning resource for developers interested in web application security.

## Features

- Django 5.1 based project structure
- Custom apps: input_handler and geo_ip_track
- Admin interface for easy management
- Secure settings configuration

## Future TODO

1. Implement comprehensive input validation in the input_handler app
2. Develop the geo_ip_track functionality to log and analyze user locations
3. Enhance security measures, including:
   - Proper secret key management
   - Configuring allowed hosts
   - Implementing HTTPS
4. Add user authentication and authorization features
5. Create detailed documentation for each security feature implemented
6. Develop unit tests and integration tests to ensure security measures are working as expected
7. Implement CSRF protection and other Django security middlewares
8. Conduct regular security audits and penetration testing
9. Optimize for production deployment, including DEBUG mode handling
10. Implement logging and monitoring for security-related events

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- conda 

### Setting up the environment

1. CLONE THE REPO:
```bash
git clone https://github.com/bharathpofficial/secure-web-app.git
```

2. CREATE CONDA ENVIRONMENT
```bash
cd secure-web-app/build && conda env create -f environment.yml
```
```bash
conda activate security-operation-center
```

3. SET ENV VARIABLES
```bash
export SQL_API_KEY=your_sql_api_key && export IPGEO_API_KEY=your_ipgeo_api_key
```

### Running the application

1. Apply database migration:
```bash
python manage.py migrate
```

2. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

3. Run the development server:
```bash
python manage.py runserver
```

4. Access the application at `http://127.0.0.1:8000`

## Contributing

We welcome contributions to the Secure Web App project! If you're interested in helping improve this project, here's how you can contribute:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with clear, descriptive commit messages.
5. Push your changes to your fork on GitHub.
6. Submit a pull request to the main repository.

### Guidelines for contributing:

- Ensure your code adheres to the project's coding style and conventions.
- Write clear, concise commit messages.
- Include appropriate tests for your changes.
- Update documentation as necessary.
- Ensure your changes don't break existing functionality.

If you're unsure about anything, feel free to open an issue to discuss your ideas or ask questions.

We appreciate all contributions, whether they're bug reports, feature requests, or code contributions. Thank you for helping make Secure Web App better!

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). 

For more details, see the [LICENSE](LICENSE) file in the project repository or visit [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html).
