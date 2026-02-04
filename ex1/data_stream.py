#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for all types of data streams."""

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a string result."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data batch based on type criteria (string, number, int)."""

        if criteria == 'string':
            return ([x for x in data_batch if isinstance(x, str)])

        if criteria == 'number':
            return ([x for x in data_batch if isinstance(x, (int, float))])

        if criteria == 'int':
            return ([x for x in data_batch if isinstance(x, int)])

        else:
            return (data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return statistics about the stream (to be implemented by
        subclasses)."""
        pass


class SensorStream(DataStream):
    """Processes environmental sensor data: temperature, humidity,
    pressure."""

    def __init__(self, stream_id: str) -> None:
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Analyze a sensor batch and calculate average temperature."""
        if ft_len(data_batch) != 3:
            return ("Error: need temperature, humidity and pressure for"
                    " processing.")
        print(f"Processing sensor batch: [temp:{data_batch[0]},"
              f" humidity:{data_batch[1]}, pressure:{data_batch[2]}]")
        try:
            self.filter_data(data_batch)
        except ValueError as e:
            return (f"Error: {e}")
        count = 0
        avg_temp = data_batch[0]
        for _ in data_batch:
            count += 1
        return (f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg_temp}")

    def filter_data(self, data_batch: List[Any]) -> None:
        """Validate that all sensor data are positive numbers."""
        for operation in data_batch:
            if not isinstance(operation, (int, float)):
                raise ValueError('Invalid data, please enter only numbers')
            elif operation < 0:
                raise ValueError("Units can't be negative")


class TransactionStream(DataStream):
    """Processes financial transaction streams."""

    def __init__(self, stream_id: str) -> None:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of transactions and compute net flow."""
        data_batch = self.filter_data(data_batch)
        process_print = "Processing transaction batch:"
        first = '['
        len = 0
        for _ in data_batch:
            len += 1
        for operation in data_batch:
            if operation > 0:
                process_print += f"{first}buy:{operation}"
            else:
                process_print += f"{first}sell:{operation}"
            first = ''
            len -= 1
            if len != 0:
                process_print += ', '
            else:
                process_print += ']'
        print(process_print)

        op_count = 0
        net_flow = 0
        for operation in data_batch:
            op_count += 1
            net_flow += operation

        if net_flow >= 0:
            return (f"Transaction analysis: {op_count} operations, "
                    f"net flow: +{net_flow} units")
        else:
            return (f"Transaction analysis: {op_count} operations, "
                    f"net flow: {net_flow} units")

    def filter_data(self, data_batch: List[Any]) -> List[int]:
        """Filter valid transactions: integers between -10000 and 10000,
        excluding 0."""
        return ([x for x in data_batch if isinstance(x, int) and x != 0
                and x > -10000 and x < 10000])


class EventStream(DataStream):
    """Processes event logs, counting events and errors."""

    def __init__(self, stream_id: str) -> None:
        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Analyze event batch, count total events and errors."""
        data_batch = self.filter_data(data_batch, 'string')
        print(f"Processing event batch: {data_batch}")
        event_count = 0
        error_count = 0
        for event in data_batch:
            event_count += 1
            if event == "error":
                error_count += 1

        if event_count == 0 or event_count > 1:
            event_count = str(event_count)
            event_count += ' events'
        else:
            event_count = str(event_count)
            event_count += ' event'
        if error_count == 0 or error_count > 1:
            error_count = str(error_count)
            error_count += ' errors'
        else:
            error_count = str(error_count)
            error_count += ' error'

        return (f"Event analysis: {event_count}, {error_count} detected")


class StreamProcessor:
    """Provides a unified polymorphic interface to process mixed stream
    types."""

    @staticmethod
    def polymorphic_process(data: Dict[str, List[Any]],
                            streams: List[Any]) -> None:
        """Process multiple streams and report filtered and processed
        results."""
        print("Processing mixed stream types through unified interface...")
        stream_types = ["Sensor", "Transaction", "Event"]
        operation_types = ["readings", "operations", "events"]
        i = 0
        event_filtered = 0
        transasction_filtered = 0

        print("\nBatch 1 Results:")
        for stm in streams:
            operation_count = 0
            if stream_types[i] == "Event":
                len = ft_len(data[stream_types[i]])
                data[stream_types[i]] = stm.filter_data(data[stream_types[i]],
                                                        "string")
                filtered_len = ft_len(data[stream_types[i]])
                event_filtered += len - filtered_len
            elif stream_types[i] == "Transaction":
                len = ft_len(data[stream_types[i]])
                data[stream_types[i]] = stm.filter_data(data[stream_types[i]])
                filtered_len = ft_len(data[stream_types[i]])
                transasction_filtered += len - filtered_len
            for _ in data[stream_types[i]]:
                operation_count += 1
            print(f"- {stream_types[i]} data: {operation_count} "
                  f"{operation_types[i]} processed")
            i += 1

        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results {transasction_filtered} transactions, "
              f"{event_filtered} events")
        print("\nAll streams processed successfully."
              "Nexus throughput optimal.")


def ft_len(it: Any) -> int:
    """Custom function to count items in an iterable."""
    i = 0
    for _ in it:
        i += 1
    return (i)


def main() -> None:
    """Main function to run polymorphic stream processing demo."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    data = {"Sensor": [22.5, 65, 1013], "Transaction":
            [100, -150, 75, 4, 35, '2', 'e', 143540, -2000, 't', -20, 2],
            "Event":
            ['login', 'error', 'logout']}

    sensor = SensorStream("SENSOR_001")
    sensor_result = sensor.process_batch(data["Sensor"])
    print(sensor_result)
    print()

    transaction = TransactionStream("TRANS_001")
    transaction_result = transaction.process_batch(data["Transaction"])
    print(transaction_result)
    print()

    event = EventStream("EVENT_001")
    event_result = event.process_batch(data["Event"])
    print(event_result)
    print()

    print("=== Polymorphic Stream Processing ===")
    streams = [sensor, transaction, event]
    StreamProcessor.polymorphic_process(data, streams)


if __name__ == "__main__":
    main()
