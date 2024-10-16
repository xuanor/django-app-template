# Shipper Comparator (Work in Progress)

**Shipper Comparator** is a web application designed to compare shipping rates and services across various companies. The current status of the project is incomplete, and several key features still need development.

## Project Status

- **Core functionality**: Basic structure and setup are done.
- **Pending features**:
  - API integration for shipping providers.
  - Price and delivery time comparison logic.
  - UI/UX design improvements.
- **Testing**: No tests implemented yet.
  
### Next Steps
1. **API Integration**: Integrate the APIs from selected shipping companies (see `api_providers.txt` for details).
2. **Comparison Algorithm**: Develop the logic for comparing rates and delivery times (started in `views.py`).
3. **UI Improvements**: Current UI is a placeholder; design and implement final frontend components in `frontend/` folder.
4. **Testing**: Write unit tests for comparison and integration logic (focus on `test_views.py`).


## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   We recommend using a Python virtual environment.
   > **Note:** This has been tested against Django 3.10 (and may not work or be "optimal" for other versions).
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.

## Docker Setup
To use Docker for running the project:

1. Ensure Docker is installed and running on your system.

2. Build the Docker image:
```
docker build -t shipper-comparator .

```

3. Run the Docker container:
```
docker run -p 8000:8000 --env-file .env shipper-comparator

```
This will expose the application at http://localhost:8000.

4. (Optional) Use Docker Compose for easier management. If docker-compose.yml is set up, just run:
```
docker-compose up

```
This will start the app with all services (e.g., database) running in containers.


## License
Licensed under CC0-1.0.