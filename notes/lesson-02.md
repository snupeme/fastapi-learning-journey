# Lesson 02 — Routing and HTTP Fundamentals

## What I learned

- What a URL is
- What a route is
- What an endpoint is
- What an HTTP method is
- How the GET method works
- How to connect a route to a Python function
- How FastAPI returns JSON responses
- What 200 OK and 404 Not Found mean

## New endpoints

- `GET /`
- `GET /health`
- `GET /about`
- `GET /contact`

## Important code

```python
@app.get("/about")
def read_about():
    return {"project": "FastAPI Learning Journey"}