from typing import Iterable, List, Union

Number = Union[int, float]


def _validate_data(data: Iterable[Number]) -> List[Number]:
    if data is None:
        raise ValueError("data must not be None")
    try:
        seq = list(data)
    except TypeError:
        raise TypeError("data must be an iterable of numbers")
    if not seq:
        raise ValueError("data must not be empty")
    for x in seq:
        if not isinstance(x, (int, float)):
            raise TypeError("all items in data must be int or float")
    return seq


def mean(data: Iterable[Number]) -> float:
    """Return the arithmetic mean of the data as a float."""
    seq = _validate_data(data)
    return sum(seq) / len(seq)


def median(data: Iterable[Number]) -> float:
    """Return the median. For even-length lists returns the average of the two center values."""
    seq = sorted(_validate_data(data))
    n = len(seq)
    mid = n // 2
    if n % 2 == 1:
        return float(seq[mid])
    return float((seq[mid - 1] + seq[mid]) / 2)


def mode(data: Iterable[Number]) -> Union[Number, List[Number]]:
    """Return the mode. If multiple values tie for highest frequency, returns a sorted list of modes.

    If there's a single mode, returns that number (int or float as present in input).
    """
    seq = _validate_data(data)
    freq = {}
    for x in seq:
        freq[x] = freq.get(x, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    if len(modes) == 1:
        return modes[0]
    return sorted(modes)
