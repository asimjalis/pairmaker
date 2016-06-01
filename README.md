# Pairmaker

## Intro

Generates pairs for pair programming, that are guaranteed to not
repeat.

## How To Install And Use

Make a local copy.

    git clone https://github.com/asimjalis/pairmaker
    cd pairmaker

Edit the `students.txt` file and put one student name per line. Here
are some example students.

    Alexander
    Ben
    Cassandra
    Dana

For today's pairs run:

    ./pairmaker.py today
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


