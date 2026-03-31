from __future__ import annotations

import pandas as pd


class Stats:
    """Small descriptive-statistics helper for pandas data."""

    def __init__(self, data, columns=None) -> None:
        if isinstance(data, pd.Series):
            data = data.to_frame()
        self.data = pd.DataFrame(data).copy()
        if columns is not None:
            self.data = self.data.loc[:, list(columns)]

    @property
    def numeric_columns(self) -> list[str]:
        return self.data.select_dtypes(include="number").columns.tolist()

    def mean(self) -> pd.Series:
        return self.data[self.numeric_columns].mean()

    def median(self) -> pd.Series:
        return self.data[self.numeric_columns].median()

    def mode(self) -> pd.Series:
        modes = self.data.mode(dropna=True)
        return modes.iloc[0] if not modes.empty else pd.Series(dtype="object")

    def standard_deviation(self) -> pd.Series:
        return self.data[self.numeric_columns].std()

    def missing_values(self) -> pd.Series:
        return self.data.isna().sum()

    def duplicate_rows(self) -> int:
        return int(self.data.duplicated().sum())

    def correlation(self, target: str | None = None):
        corr = self.data[self.numeric_columns].corr()
        return corr if target is None else corr[target].sort_values(ascending=False)

    def summary(self) -> dict:
        return {
            "rows": int(self.data.shape[0]),
            "columns": int(self.data.shape[1]),
            "numeric_columns": self.numeric_columns,
            "missing_values": self.missing_values().to_dict(),
            "duplicate_rows": self.duplicate_rows(),
        }
