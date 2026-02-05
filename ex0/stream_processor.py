#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Optional


class DataProcessor(ABC):
    """Abstract base class defining the interface for data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a string result or None."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate the input data, return True if valid."""
        pass

    def format_output(self, result: str) -> str:
        """Format the processed result for display."""
        return ("Output: " + result)


class NumericProcessor(DataProcessor):
    """Processes numeric data: sums and averages numbers."""

    def __init__(self) -> None:
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        """Process numeric data to calculate sum and average."""
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
        """Ensure all items in data are numeric."""
        try:
            for number in data:
                int(number)
            print("Validation: Numeric data verified")
            return True
        except ValueError:
            print(f"Invalid numeric data: '{number}' is not a number")
            return False


class TextProcessor(DataProcessor):
    """Processes text data: counts words and characters."""

    def __init__(self) -> None:
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        """Process text to count characters and words."""
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
            if word_count == 0 and char != ' ':
                word_count += 1
            elif char != ' ' and not data[ch_count - 1] != ' ':
                word_count += 1
            ch_count += 1

        result = f"Processed text: {ch_count} characters, {word_count} words"
        return (result)

    def validate(self, data: Any) -> bool:
        """Check if data is a string."""
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """Processes log data: detects errors and extracts log messages."""

    def __init__(self) -> None:
        print("Initializing Log Processor...")

    def process(self, data: Any) -> Optional[str]:
        """Process log entries to detect errors and capture message
        after colon."""
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
        """Check if the log entry contains a colon character."""
        for ch in data:
            if ch == ':':
                return True
        return False


def polymorphic_demo(processors: List[tuple[DataProcessor, Any]]) -> None:
    """Demonstrate polymorphic processing for multiple data processors."""
    i = 1
    for processor, data in processors:
        result = processor.process(data)
        if result:
            print(f"Result {i}: {result}\n")
        i += 1


def main() -> None:
    """Main function to run the data processors and polymorphic demo."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    numeric = NumericProcessor()
    numeric_result = numeric.process(numeric_data)
    if numeric_result:
        print(numeric.format_output(numeric_result))
    print()

    text = TextProcessor()
    text_result = text.process(text_data)
    if text_result:
        print(text.format_output(text_result))
    print()

    log = LogProcessor()
    log_result = log.process(log_data)
    if log_result:
        print(log.format_output(log_result))

    print("\n=== Polymorphic Processing Demo ===\n")

    processors = [(numeric, numeric_data), (text, text_data), (log, log_data)]
    polymorphic_demo(processors)

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
