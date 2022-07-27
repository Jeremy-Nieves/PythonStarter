import enum

class Scales(enum.Enum):
    c = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    g = ["G", "A", "B", "C", "D", "E", "F#"]
    d = ["D", "E", "F#", "G", "A", "B", "C#"]
    a = ["A", "B", "C#", "D", "E", "F#", "G"]

def get_musical_scale(scale):
    match scale:
        case Scales.c.name:
            return Scales.c.value
        case Scales.g.name:
            return Scales.g.value
        case Scales.d.name:
            return Scales.d.value
        case Scales.a.name:
            return Scales.a.value

print(get_musical_scale('a'))
