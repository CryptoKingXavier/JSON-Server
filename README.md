# JSON Server with Python Flask

This project implements a simple JSON Server using Python Flask. It serves as a RESTful API for handling JSON data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.x recommended)
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_project
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. The server will be running at `http://localhost:5000`.

### Endpoints

- **GET /data**: Retrieve all JSON data.
- **GET /data/{id}**: Retrieve JSON data by ID.
- **POST /data**: Add new JSON data.
- **PUT /data/{id}**: Update existing JSON data.
- **DELETE /data/{id}**: Delete JSON data by ID.
