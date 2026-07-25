# Page Pulse - Digital Heroes Task

A production-grade URL auditing service built with FastAPI.

## Features

- URL Validation
- Website Audit
- HTML Title Extraction
- HTTP Status Detection
- Response Time Measurement
- Content Length Detection
- Timeout Handling
- Structured Error Responses
- In-Memory TTL Cache
- Rate Limiting
- Concurrency Limiting

## Tech Stack

- Python 3
- FastAPI
- httpx
- BeautifulSoup4
- SlowAPI
- cachetools
- Uvicorn

## Installation

```bash
git clone https://github.com/minchugm/page-pulse-digital-heroes.git

cd page-pulse-digital-heroes

pip install -r requirements.txt
```

Run

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

## API

### POST /audit

Request

```json
{
    "url":"https://example.com"
}
```

Example Response

```json
{
    "url":"https://example.com",
    "status":"success",
    "message":"Audit completed successfully",
    "title":"Example Domain",
    "status_code":200,
    "response_time_ms":120.5,
    "content_length":1256
}
```

## Project Structure

```
page-pulse-digital-heroes
│
├── app
├── tests
├── requirements.txt
├── README.md
└── .env.example
```

## Future Improvements

- Persistent caching (Redis)
- Authentication
- Docker support
- Prometheus metrics
- Distributed rate limiting