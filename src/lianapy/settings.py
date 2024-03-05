"""
Settings file adopting a paradigm based on pydantic_settings.
"""

from pathlib import Path

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict

# The prefix used to lookup environment variables.
ENV_PREFIX = "lianapy_"
# By default, pydantic_settings does not read from the parent directory. If we use subdirectories for scripts or notebooks, it is convenient to use the parent directory as a fallback.
ENV_FILES = ("settings.env", "../settings.env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=ENV_PREFIX, env_file=ENV_FILES)

    # Each of the following attribute will be looked up in the correspondingly named environment variable (uppercase).
    input_data: DirectoryPath = Path(".")
    install: DirectoryPath = Path(".")

    @property
    def output_path(self) -> Path:
        return self.install / "output"

    @property
    def test_output_path(self) -> Path:
        return self.output_path / "tests"
