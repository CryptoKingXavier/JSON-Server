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
    git clone https://github.com/CryptoKingXavier/JSON-Server.git
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

1. Start the Bash Script:

    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

2. The server will be running at `http://127.0.0.1:8080`.

### Endpoints

- **GET /data**: Retrieve all JSON data.
- **GET /data/{id}**: Retrieve JSON data by ID.
- **POST /data**: Add new JSON data.
- **PUT /data/{id}**: Update existing JSON data.
- **DELETE /data/{id}**: Delete JSON data by ID.
