# GitHub Gists API Service

This is a simple HTTP API built with Python and Flask that retrieves public gists for a given GitHub user. 
The service runs on port `8080` and is containerized using Docker.

---

## 📦 Requirements

- Docker (for containerized usage)
- OR Python 3.8+ (for running locally)
- `pip` (for dependency installation if running locally)

---

## 🚀 Quick Start
Run Locally with Python

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py


# Run Tests
pip install pytest
pytest test_app.py

Visit: http://localhost:8080/octocat

### Run with Docker (Recommended)

```bash
# Build the Docker image
docker build -t github-gists-api .

# Run the container on port 8080
docker run -p 8080:8080 github-gists-api
