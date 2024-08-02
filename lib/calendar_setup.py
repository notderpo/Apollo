from dotenv import load_dotenv
load_dotenv()

import os
from nylas import Client
from flask import Flask, request, redirect, url_for, session, jsonify
from flask_session.__init__ import Session

from nylas.models.auth import URLForAuthenticationConfig
from nylas.models.auth import CodeExchangeRequest
from datetime import datetime, timedelta

# Create the app
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Initialize Nylas client
nylas = Client(
    api_key = "<NYLAS_API_KEY>",
    api_uri = "<NYLAS_API_URI>",
)

@app.route("/nylas/auth", methods=["GET"])
def login():
  if session.get("grant_id") is None:
    config = URLForAuthenticationConfig({
      "client_id": "<NYLAS_CLIENT_ID>",
      "redirect_uri" : "http://localhost:5000/oauth/exchange"
    })

    url = nylas.auth.url_for_oauth2(config)

    return redirect(url)
  else:
      return f'{session["grant_id"]}'  