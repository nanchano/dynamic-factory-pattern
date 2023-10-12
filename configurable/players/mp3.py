class MP3Player:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def play(self) -> None:
        print("Using api_key to authenticate")
        print("Playing MP3")
