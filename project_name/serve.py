#!/usr/bin/env python3
"""
Sample Flask app
"""
# Permissions scope names
import functools
import os
import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Response
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from common import auth


PERM_READ = "read"
PERM_WRITE = "write"
PERM_ADMIN = "Reports"

app = FastAPI()

origins = [
    "http://localhost:8111",
    "http://localhost:7008/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

requires_auth_read = functools.partial(auth._requires_auth, permission=PERM_READ)
requires_auth_write = functools.partial(auth._requires_auth, permission=PERM_WRITE)
requires_auth_admin = functools.partial(auth._requires_auth, permission=PERM_ADMIN)



# Route definitions

@app.get("/insecure")
def insecure(): # pragma: no cover
    return "Insecure route."

@app.get("/secure")
@requires_auth_read
def secure(request: Request): # pragma: no cover
    """Test for a secure route"""
    return "Secure route."

