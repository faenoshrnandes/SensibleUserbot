import os

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    
    # Ensure TEMP_DOWNLOAD_DIRECTORY has a fallback value
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "/tmp")  # Default to '/tmp' if not set
    
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    
    # Ensure TEMP_DOWNLOAD_DIRECTORY is set with a fallback value
    if TEMP_DOWNLOAD_DIRECTORY:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY, exist_ok=True)  # Make sure the directory exists
        # Save the auth token to a file
        with open(os.path.join(TEMP_DOWNLOAD_DIRECTORY, "auth_token.txt"), "w") as t_file:
            t_file.write(AUTH_TOKEN_DATA)
    else:
        raise ValueError("TEMP_DOWNLOAD_DIRECTORY is not set.")
    
    # Private group ID validation
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError("Invalid Private Group ID. Make sure your ID starts with -100 and is only numbers.")

class Development(Var):
    LOGGER = True
    # Here for later purposes
