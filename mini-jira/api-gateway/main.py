# mini-jira/api-gateway/main.py

from fastapi import FastAPI, Request
import httpx

app = FastAPI()

# Konfigurasi endpoint service
SERVICE_URLS = {
    "user": "http://user-service:8001",
    "task": "http://task-service:8002",
    "payment": "http://payment-service:8003",
    "notification": "http://notification-service:8004",
    "report": "http://report-service:8005",
    "audit": "http://audit-service:8006",
    "inventory": "http://inventory-service:8007"
}


@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):
    if service not in SERVICE_URLS:
        return {"error": f"Service '{service}' tidak ditemukan"}

    target_url = f"{SERVICE_URLS[service]}/{path}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=request.headers.raw,
                content=await request.body()
            )
            return response.json()
        except httpx.RequestError as e:
            return {"error": f"Gagal menghubungi service {service}: {str(e)}"}
