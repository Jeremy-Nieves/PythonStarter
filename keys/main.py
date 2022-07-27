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

majorkey = str.lower(input("Enter the root note: "))

if majorkey == "c":
    print("The notes played in C Major are: ")
    print(majorkeydict["c"])
elif majorkey == "g":
    print("The notes played in G Major are:")
    print(majorkeydict["g"])
elif majorkey == "d":
    print("The notes played in D Major are:")
    print(majorkeydict["d"])
elif majorkey == "a":
    print("The notes played in A Major are:")
    print(majorkeydict["a"])
elif majorkey == "e":
    print("The notes played in E Major are:")
    print(majorkeydict["e"])
elif majorkey == "b":
    print("The notes played in E Major are:")
    print(majorkeydict["b"])
elif majorkey == "gb":
    print("The notes played in E Major are:")
    print(majorkeydict["gb"])
elif majorkey == "db":
    print("The notes played in E Major are:")
    print(majorkeydict["db"])
elif majorkey == "ab":
    print("The notes played in E Major are:")
    print(majorkeydict["ab"])
elif majorkey == "eb":
    print("The notes played in E Major are:")
    print(majorkeydict["eb"])
elif majorkey == "bb":
    print("The notes played in E Major are:")
    print(majorkeydict["bb"])
elif majorkey == "f":
    print("The notes played in E Major are:")
    print(majorkeydict["f"])
else:
    print("Not a key!")