class FLACPlayer:
    def __init__(self, api_key: str, secret_key: str) -> None:
        self.api_key = api_key
        self.secret_key = secret_key

    def play(self) -> None:
        print("Using api_key and secret_key to authenticate")
        print("Playing FLAC")
