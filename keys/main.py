majorkeydict = {

    'c': ("C", "D", "E", "F", "G", "A", "B"),
    'g': ("G", "A", "B", "C", "D", "E", "F#"),
    'd': ("D", "E", "F#", "G", "A", "B", "C#"),
    'a': ("A", "B", "C#", "D", "E", "F#", "G"),
    'e': ("E", "F#", "G#", "A", "B", "C#", "D#"),
    'b': ("B", "C#", "D#", "E", "F#", "G#", "A"),
    'gb': ("Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"),
    'db': ("Db", "Eb", "F", "Gb", "Ab", "B", "C"),
    'ab': ("Ab", "Bb", "C", "Db", "Eb", "F", "G"),
    'eb': ("Eb", "F", "G", "Ab", "Bb", "C", "D"),
    'bb': ("Bb", "C", "D", "Eb", "F", "G", "A"),
    'f': ("F", "G", "A", "Bb", "C", "D", "E",)

    }

root_note = str.lower(input("Enter the root note: "))

if root_note in majorkeydict:
    notes = majorkeydict[root_note]
    print(f"The notes in the key of {root_note} major are {notes}")



