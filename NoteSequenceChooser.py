 
#!/bin/env python3

import time
import asyncio

'''
    todo: improve choosed notes
    maybe soundPatch properties should affect the notes like "bass" in patch name or category names
'''
class NoteSequenceChooser:
    def __init__(self, midiOutWrapper, soundPatch):
        self.midiOutWrapper = midiOutWrapper
        self.soundPatch = soundPatch
        self.finishedAllSequences = False

    async def sendSequences(self):
        seqs = [
            {
                "notes": [60,64,68],
                "duration": 1.5
            },
            {
                "notes": [45],
                "duration": 1
            }
        ]
        for sequence in seqs:
            for note in sequence["notes"]:
                self.midiOutWrapper.note_on(note)
            time.sleep(sequence["duration"])
            for note in sequence["notes"]:
                self.midiOutWrapper.note_off(note)
            self.midiOutWrapper.send_all_sound_off()
            #time.sleep(0.5)

        self.finishedAllSequences = True

        #return 1
            