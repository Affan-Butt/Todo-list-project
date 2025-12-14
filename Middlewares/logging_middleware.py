# Middlewares/logging_middleware.py
from fastapi import Request
import time


async def logging_middleware(request: Request, call_next):
    start_time = time.time()

    method = request.method
    path = request.url.path

    print(f"[REQUEST] {method} {path}")

    response = await call_next(request)

    duration = time.time() - start_time
    status_code = response.status_code

    print(f"[RESPONSE] {method} {path} -> {status_code} in {duration:.4f}s")

    response.headers["X-Process-Time"] = f"{duration:.4f}s"
    return response
