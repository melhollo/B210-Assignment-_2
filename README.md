sleep_stats
===========

Simple package providing mean, median, and mode functions for numeric sleep duration lists.

Usage
-----

from sleep_stats import mean, median, mode

sleep_hours = [7, 8, 6, 7.5]
print(mean(sleep_hours))
print(median(sleep_hours))
print(mode(sleep_hours))

Notes
-----
- `mode` returns a single value when there's one mode, or a sorted list when multiple values tie.
- All functions raise ValueError on empty input and TypeError if non-numeric items are passed.
