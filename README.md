# Spotify Sort by Genre

## Overview

This Python program utilizes the Spotify Web API and Spotipy library to import the "Liked Songs" playlist from a user's Spotify account. It aims to extract song details and sort them by genres.

Please note that this README is a placeholder and the program is currently incomplete. The genre extraction logic has not been fully implemented due to challenges in finding an accurate database for the genre of each song.

## Requirements

- Python 3.x
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jjd2963/Spotify-Sort-by-Genre.git
   ```

2. Install the required dependencies:

   ```bash
   pip install spotipy
   ```

3. Set up your Spotify Developer credentials:

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new application to obtain your Client ID and Client Secret.
   - Set the Redirect URI to match your application's callback URI.

4. Update the credentials in the script:

   Open `sorter.py` and replace the following placeholders:

   ```python
   CLIENT_ID = 'your_client_id'
   CLIENT_SECRET = 'your_client_secret'
   REDIRECT_URI = 'your_redirect_uri'
   ```

## Usage

Run the program:

```bash
python sorter.py
```

The program will authenticate with Spotify, retrieve the user's "Liked Songs" playlist, and attempt to extract and sort songs by genres. However, the genre extraction logic is incomplete.

## Known Issues

The genre extraction logic is incomplete due to challenges in finding an accurate database for the genre of each song.

## Contributing

Feel free to contribute to the project by implementing the missing genre extraction logic or addressing any known issues. Pull requests are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
