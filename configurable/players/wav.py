class WAVPlayer:
    def __init__(self, user: str, pwd: str) -> None:
        self.user = user
        self.pwd = pwd

    def play(self) -> None:
        print("Using user and pwd to authenticate")
        print("Playing WAV")
