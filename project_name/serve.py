#!/usr/bin/env python3
"""
Sample Flask app
"""
# Permissions scope names
import functools
import os

from common import auth
from flask import Flask, request
from flask_cors import CORS

PERM_READ = "read"
PERM_WRITE = "write"
PERM_ADMIN = "reports"

def error_func(code=401, **args): # pragma: no cover
    if isinstance(code, int):
        return "Auth Error", code
    return "Auth Error", 500



requires_auth_read = functools.partial(auth._requires_auth, permission=PERM_READ, error_func=error_func)
requires_auth_write = functools.partial(auth._requires_auth, permission=PERM_WRITE, error_func=error_func)
requires_auth_admin = functools.partial(auth._requires_auth, permission=PERM_ADMIN, error_func=error_func)

app = Flask(__name__)
CORS(app)


# Route definitions

@app.route("/insecure")
def insecure():
    return "Insecure route.", 200

@app.route("/secure")
@requires_auth_read
def secure():
    return "Secure route.", 200


if __name__ == "__main__": # Run the Flask server in development mode
    app.debug = True
    app.config["ENV"] = "development"
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7000)))
