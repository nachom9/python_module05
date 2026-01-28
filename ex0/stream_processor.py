#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return ("Output: " + result)


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        number_count = 0
        sum = 0

        print(f"Processing data: {data}")

        if not self.validate(data):
            return
        for number in data:
            number_count += 1
            sum += number

        avg = sum / number_count
        result = (f"Processed {number_count} numeric values, sum={sum},"
                  f"avg={avg}")
        return (result)

    def validate(self, data: Any) -> bool:

        try:
            for number in data:
                int(number)
            print("Validation: Numeric data verified")
            return True
        except ValueError:
            print(f"Invalid numeric data: '{number}' is not a number")
            return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print("Initializing Text Processor...")
        word_count = 0
        ch_count = 0

        print(f"Processing data: {data}")

        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")
            print("Validation: Text data verified")
        except ValueError as e:
            print(f"Error {e}")
            return
        for char in data:
            if char != ' ' and not data[ch_count - 1].isascii():
                word_count += 1
            ch_count += 1

        result = f"Processed text: {ch_count} characters, {word_count} words"
        return (result)

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print("Initializing Log Processor...")
        result = ''
        found = False

        print(f"Processing data: {data}")
        try:
            if not self.validate(data):
                raise Exception("Invalid log data")
            print("Validation: Log entry verified")
        except Exception as e:
            print(f"Error: {e}")
            return

        if "ERROR" in data or "Error" in data:
            result = "[ALERT] ERROR level detected"

        for ch in data:
            if ch == ':':
                found = True
            if found:
                result += ch
        return (result)

    def validate(self, data: Any) -> bool:

        for ch in data:
            if ch == ':':
                return True
        return False


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    numeric_result = numeric.process(numeric_data)
    if numeric_result:
        print(numeric.format_output(numeric_result))
    print()

    text_result = text.process(text_data)
    if text_result:
        print(text.format_output(text_result))
    print()

    log_result = log.process(log_data)
    if log_result:
        print(log.format_output(log_result))


if __name__ == "__main__":
    main()
