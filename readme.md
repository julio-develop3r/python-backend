# FastAPI Backend Deployment on Render

This project demonstrates how to create a backend using FastAPI and deploy it for free on Render.

## Features

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.

- Render Deployment: Deploying the FastAPI application on Render for free.

- Automatic Deployment: The backend is updated automatically when pushing changes to the repository.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

        git clone https://github.com/yourusername/yourproject.git
        cd yourproject


2. Create and activate a virtual environment:

        python -m venv venv
        source venv/bin/activate  # On macOS/Linux
        venv\Scripts\activate  # On Windows


3. Install dependencies:

        pip install -r requirements.txt


4. Run the FastAPI server:

        uvicorn main:app --reload


5. Open the API documentation in your browser:

    - Swagger UI: http://127.0.0.1:8000/docs

    - Redoc: http://127.0.0.1:8000/redoc

## Deployment on Render

To deploy the FastAPI application on Render:

1. Push your project to a Git repository (GitHub, GitLab, or Bitbucket).

2. Create a new Web Service on Render.

3. Select your repository and set up the following configuration:

    - Runtime: Python

    - Build Command: ```pip install -r requirements.txt```

    - Start Command: ```uvicorn main:app --host 0.0.0.0 --port 10000```

4. Deploy and get your public URL.

## Technologies Used

- FastAPI for backend development.

- Uvicorn as an ASGI server.

- Render for cloud deployment.

- Git for version control.

## License

This project is open-source and available under the MIT License.