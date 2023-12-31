from robyn import Robyn, Request
from robyn_rate_limits import InMemoryStore
from robyn_rate_limits import RateLimiter

app = Robyn(__file__)
limiter = RateLimiter(store=InMemoryStore, calls_limit=3, limit_ttl=100)

@app.before_request()
def middleware(request: Request):
    return limiter.handle_request(app, request)


@app.get("/")
def h():
    return "Hello, World!"

app.start(port=8080)