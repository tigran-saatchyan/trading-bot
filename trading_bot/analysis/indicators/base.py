from abc import ABC, abstractmethod
from typing import Union

import pandas as pd
import structlog

logger = structlog.get_logger()


class Indicator(ABC):
    """
    Abstract base class for all technical indicators.
    """

    def compute(self, df: pd.DataFrame) -> Union[pd.Series, pd.DataFrame]:
        """
        Public method: validate input, log start/end, call implementation.
        """
        logger.info("Start computing", indicator=self.__class__.__name__)
        self._validate(df)
        result = self._compute(df)
        logger.info("Finished computing", indicator=self.__class__.__name__)
        return result

    def _validate(self, df: pd.DataFrame) -> None:
        """
        Ensure DataFrame has required columns and DatetimeIndex.
        """
        required = {"open", "high", "low", "close", "volume"}
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError("DataFrame index must be DatetimeIndex")
        if not required.issubset(df.columns):
            missing = required - set(df.columns)
            raise ValueError(f"Missing required columns: {missing}")

    @abstractmethod
    def _compute(self, df: pd.DataFrame) -> Union[pd.Series, pd.DataFrame]:
        """
        Core implementation; returns Series or DataFrame.
        """
        ...
