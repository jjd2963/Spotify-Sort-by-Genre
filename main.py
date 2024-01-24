from flask import Flask, redirect, request, session, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Spotify API credentials
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

# Spotify API endpoints
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1/me'

# Scopes define the permissions your app needs
SPOTIFY_SCOPES = 'user-read-private user-read-email playlist-read-private playlist-modify-public playlist-modify-private'

@app.route('/')
def index():
    # Redirect to Spotify authorization page
    return redirect(f"{SPOTIFY_AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SPOTIFY_SCOPES}")

@app.route('/callback')
def callback():
    # Handle callback from Spotify and retrieve code
    auth_code = request.args.get('code')

    # Exchange authorization code for access token
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    response = requests.post(SPOTIFY_TOKEN_URL, data=data)
    access_token = response.json().get('access_token')

    # Store the access token in the session or database (as appropriate for your app)
    session['access_token'] = access_token

    # Example: Get user's profile information
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(f"{SPOTIFY_API_BASE_URL}/me", headers=headers)
    user_data = user_response.json()


    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=True)
