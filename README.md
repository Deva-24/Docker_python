# QR Code Generator with Docker

This project is a Python application that generates a QR code PNG file linking to a specific URL (your GitHub homepage) using Docker. The QR code can be scanned with a mobile device to open the URL directly in a browser.

## Requirements

- Docker installed on your machine
- Basic knowledge of Docker and Python

## Project Setup

### 1. Clone the Repository

If you haven’t already, clone the repository to your local machine:

```bash
git clone https://github.com/Deva-24/qr_code_docker.git
cd qr_code_docker
```

### 2. File Overview

This project contains the following files:

- **`generate_qr.py`**: The Python script that generates the QR code.
- **`Dockerfile`**: Defines the Docker image and environment.
- **`requirements.txt`**: Lists the Python dependencies needed for the project.

### 3. Steps to Run the Project with Docker

#### 1. Build the Docker Image

To build the Docker image for the project, use the following command:

```bash
docker build -t qr-code-generator .
```

This will create a Docker image named `qr-code-generator` from the `Dockerfile` in the current directory.

#### 2. Run the Docker Container

Run the container to generate the QR code:

```bash
docker run --name qr_code_container qr-code-generator
```

The Python script inside the container will generate a QR code PNG file containing the URL (your GitHub homepage) and save it as `github_qr.png` inside the container.

#### 3. Retrieve the Generated QR Code File

To get the generated `github_qr.png` file from the container, run the following command:

```bash
docker cp qr_code_container:/app/github_qr.png .
```

This will copy the generated QR code image from the container to your current directory.

#### 4. Clean Up

Once you have the QR code file, you can remove the running container:

```bash
docker rm qr_code_container
```

### 4. Viewing the QR Code

Now that you have the `github_qr.png` file, you can:

- Open it using any image viewer.
- Scan the QR code with your phone’s camera to access the URL.

### 5. Docker Commands Summary

Here are the important Docker commands used in this project:

- **Build the Docker image**:
  ```bash
  docker build -t qr-code-generator .
  ```

- **Run the container**:
  ```bash
  docker run --name qr_code_container qr-code-generator
  ```

- **Copy the QR code file from the container to your local machine**:
  ```bash
  docker cp qr_code_container:/app/github_qr.png .
  ```

- **Remove the container after use**:
  ```bash
  docker rm qr_code_container
  ```

## Additional Information

- The QR code generated in this project links to your GitHub homepage. If you'd like to change the URL, modify the `url` variable in the `generate_qr.py` file.
- This project demonstrates how to use Docker with a simple Python script to generate an image file, showcasing Docker's power in containerizing applications.

## License

This project is licensed under the MIT License.

```

This README file provides a clear and structured guide on how to set up, run, and retrieve the generated QR code image from the Dockerized Python application.