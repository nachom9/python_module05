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
        for number in data:
            if self.validate(number):
                number_count += 1
                sum += number
        
        avg = sum / number_count
        result = f"Processed {number_count} numeric values, sum={sum}, avg={avg}"
        return(result)
        

    def validate(self, data: Any) -> bool:

        try:
            int(data)
            return True
        except ValueError as e:
            return False


class TextProcessor(DataProcessor):
    
    def process(self, data: Any) -> str:

        print("Initializing Text Processor...")
        word_count = 0
        letter_count = 0
        
        print(f"Processing data: {data}")
        for character in data:
            if self.validate(number):
                number_count += 1
                sum += number
        
        avg = sum / number_count
        result = f"Processed {number_count} numeric values, sum={sum}, avg={avg}"
        return(result)

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False



class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    numeric_data = [1, 2, 'e', 4, 5]
    text_data = "Hello Nexus World!"
    numeric_result = numeric.process(numeric_data)
    text_result = text.process(text_data)
    print(numeric.format_output(numeric_result), '\n')




if __name__ == "__main__":
    main()