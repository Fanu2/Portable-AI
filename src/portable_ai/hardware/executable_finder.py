import shutil


class ExecutableFinder:
    """
    Finds executables available on the host system.
    """

    def find(self, executable: str) -> str | None:
        return shutil.which(executable)
