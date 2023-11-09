from fastapi import FastAPI, HTTPException, Request
from modules import database_manager, ips
import os
import asyncio

app = FastAPI()

@app.get("/refreships")
async def test():
  try:
    await database_manager.download_database()
  except Exception as e:
    raise HTTPException(status_code=500, detail={"successful": False, "error": str(e)})

  return {"successful": True}

@app.get("/ip")
async def ip(request: Request):
  # Get the client's IP address from the request object
  client_ip = request.client.host

  # If your FastAPI application is behind a proxy server,
  # you can get the proxy's IP address from the headers
  proxy_ip = request.headers.get("X-Forwarded-For")

  ip = proxy_ip if proxy_ip else client_ip
  ip_data = await ips.get_ip_info(ip)
  
  if ip_data is None:
    raise HTTPException(status_code=404, detail={"successful": False, "error": "Didn't find ip data."})
  
  return {"successful": True, "ip_data": ip_data}

@app.get("/ip/{ip}")
async def ip(ip: str):
  ip_data = await ips.get_ip_info(ip)
  
  if ip_data is None:
    raise HTTPException(status_code=404, detail={"successful": False, "error": "Didn't find ip data."})
  
  return {"successful": True, "ip_data": ip_data}
