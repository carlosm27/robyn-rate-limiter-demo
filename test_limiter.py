import requests
import time

def test_rate_limiter(url, rate_limit, time_window):
    """Tests a rate limiter with the given parameters."""

    start_time = time.time()
    allowed_requests = 0
    blocked_requests = 0

    while time.time() - start_time < time_window:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            allowed_requests += 1
        except requests.exceptions.RequestException as e:
            blocked_requests += 1
            print(f"Request blocked: {e}")

        time.sleep(time_window / rate_limit)  # Delay to respect the rate limit

    print(f"Allowed requests: {allowed_requests}")
    print(f"Blocked requests: {blocked_requests}")

# Example usage:
url = "http://localhost:8080/"  # Replace with the actual URL
rate_limit = 3  # Requests per second
time_window = 5  # Seconds

test_rate_limiter(url, rate_limit, time_window)
