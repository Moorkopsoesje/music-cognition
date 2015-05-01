# music-cognition
Repository of the experiment for the course Artificial and Natural Music Cognition.


Experiment where participants had to mimic rhythmic patterns with intervals adding up to 1 s. These patterns were made in Python, using the files __init__.py to create all possible intervals, intervals.py to create a selection of intervals per participant and using a combination of Matlab and Python created the MIDI files for each participant. The reactions were recorded and saved to MIDI files.

The timestamps of the sounds were read using Matlab. The intervals between timestamps are calculated using Python. We used Matlab to calculate averages, errors and entropy. The ternplot library in Matlab is used to map all the responses to a ternary plot. Here, we made a few adaptations in the library.


###Dependencies

* Python 2.7
* Matlab (2014a was used)
* [Midiutil](https://code.google.com/p/midiutil/) for Python
* [NumPy](http://numpy.org) for Python
* [MIDI](http://www.kenschutte.com/midi/) for Matlab
