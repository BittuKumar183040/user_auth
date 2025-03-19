# Auth Service

This is an authentication service built using **FastAPI**.

## Features

- User authentication and authorization
- Token-based authentication (JWT)
- Secure password hashing
- RESTful API endpoints

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

	```bash
	git clone https://github.com/your-repo/auth-service.git
	cd auth-service
	```

2. Create a virtual environment and activate it:

	```bash
	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
	```

3. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

## Running the Application

1. Start the development server:

	```bash
	fastapi dev main.py
	```

2. Open your browser and navigate to:

	```
	http://127.0.0.1:8000
	```

## API Documentation

FastAPI provides interactive API documentation:

- docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

```
auth-service/
│
├── app/
│   ├── main.py          # Entry point of the application
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   ├── schemas/         # Pydantic models
│   └── utils/           # Utility functions
│
├── tests/               # Unit and integration tests
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.