#Import the library

from midiutil.MidiFile import MIDIFile
from boto.dynamodb.condition import NULL

def makemidi(intervals, filename='test.midi'):
    # Create the MIDIFile Object with 1 track
    MyMIDI = MIDIFile(1)
    
    # Tracks are numbered from zero. Times are measured in beats. 
    track = 0   # testphase (0), trainphase (1)
    time = 0
    
    # Number of repetitions and notes in interval
    rep = 3
    note = 0
    
    # Add track name and tempo.
    track = 0  
    MyMIDI.addTrackName(track,time,"Music Cognition Experiment")
    MyMIDI.addTempo(track,time,60)
    
    # Add a note. addNote expects the following information:
    channel = 0
    pitch = 60
    duration = 0.5
    volume = 100
    counter = 0
    
    for int in intervals:                       # Nr of intervals
        for j in range(0,rep):                  # Nr of repetitions
            for k in range(0,len(int)+1):       # Nr of notes in interval
                # Add the note.
                if k == 0:
                    time = note + counter
                    MyMIDI.addNote(track,channel,pitch,time,duration,volume)
                else:
                    time = note + int[k-1] + counter
                    MyMIDI.addNote(track,channel,pitch,time,duration,volume)
                    note = note + int[k-1]
                #print time
            counter = counter + 5
            
            #MyMIDI.addNote(track,channel,pitch,counter,15,0)
            
    binfile = NULL
    # Write it to disk.
    binfile = open(filename+".mid", 'wb')
    
    if binfile != NULL:
        MyMIDI.writeFile(binfile)
        binfile.close() 