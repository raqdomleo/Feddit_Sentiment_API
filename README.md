
# Allianz Technical Challenge - Sentiment Analysis Microservice

This project is a technical challenge for Allianz Services. The goal is to build a microservice that consumes the Feddit API (a fake Reddit-like API), performs sentiment analysis on comments using TextBlob, and exposes an API to query the processed data.

---

## Project Structure

```
├── app/                # FastAPI application
│   ├── main.py        # API endpoints
│   ├── models.py      # Data models
│   ├── services.py    # Sentiment analysis logic
│   └── config.py      # Configuration settings
│
├── tests/              # Unit tests
│
├── Dockerfile          # Docker configuration for the microservice
├── docker-compose.yml  # Docker configuration to run Feddit API
├── requirements.txt    # Python dependencies
├── .github/workflows/  # CI/CD with GitHub Actions
├── README.md           # Project documentation
└── .env.example        # Environment variables example
```

---

## How to Run Locally

1. Clone this repository.

2. Install Docker and Docker Compose.

3. Start the Feddit API locally:
```bash
docker compose -f docker-compose.yml up -d
```

4. Run the FastAPI microservice:
```bash
docker build -t sentiment-service .
docker run -d -p 8000:8000 --env-file .env sentiment-service
```

5. Access the API:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

---

## API Features

- List comments with sentiment analysis.
- Filter comments by date range.
- Sort comments by sentiment polarity.
- Get average sentiment for a given subfeddit.

---

## Environment Variables

Copy `.env.example` to `.env` and configure:

```
API_URL=http://feddit:8080
LIMIT=100
SKIP=0
```

---

## Run Tests

```bash
pytest tests/
```

---

## CI/CD with GitHub Actions

This project uses GitHub Actions to:
- Run tests on every push.
- Lint the code with flake8.
- Check Docker build.

---

## Feddit API Reference

The Feddit API documentation is available at:
- http://0.0.0.0:8080/docs
- http://0.0.0.0:8080/redoc

---

## Sentiment Analysis

The sentiment polarity is computed using TextBlob:

| Polarity Value        | Interpretation        |
|----------------------|-----------------------|
| -1 to -0.1           | Negative              |
| -0.1 to 0.1          | Neutral               |
| 0.1 to 1             | Positive              |

---

## Requirements

- Python 3.10
- Docker & Docker Compose
- FastAPI
- TextBlob
- PostgreSQL (Feddit internal)
