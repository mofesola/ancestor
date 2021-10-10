import os

class Common:

    def recording_duration():
        return os.getenv("RECORDING_DURATION", 15)
