#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    
    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):


class TextProcessor(DataProcessor):


class LogProcessor(DataProcessor):