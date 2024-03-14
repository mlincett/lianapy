from collections import defaultdict
import pandas as pd


class SummaryTable:
    """A summary class for tabular data of arbitrary length. This class wraps around a (default)dict to store, one row at a time, one value per column. Provides a method to output a dataframe."""

    def __init__(self):
        self.summary = defaultdict(list)

    def record(self, key: str, value) -> None:
        """Record a key-value pair."""
        self.summary[key].append(value)

    def to_pandas(self) -> pd.DataFrame:
        return pd.DataFrame(self.summary)
