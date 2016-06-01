# Pairmaker

## Intro

Generates pairs for pair programming, that are guaranteed to not
repeat.

## Algorithm

Uses *round-robin tournament algorithm* as described at
<https://en.wikipedia.org/wiki/Round-robin_tournament>.

## Usage

    ./pairmaker.py [OPTIONS]

## Examples

    ./pairmaker.py 0426          Pairs for 04/26
    ./pairmaker.py today         Pairs for today
    ./pairmaker.py help          Usage message

## Notes

- Looks for `students.txt` in directory where script running from
- File `students.txt` must contain student names one per line

