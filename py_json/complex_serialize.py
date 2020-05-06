import  json

class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

    def encodeJSON(elf):
        dict = {
            "level":elf.level,
            "ability_scores":elf.ability_scores,
            "hp": elf.hp
        }
        return  dict

class ElfEncoder(json.JSONEncoder):
    def encodeJSON(elf):
        dict = {
            "level":elf.level,
            "ability_scores":elf.ability_scores,
            "hp": elf.hp
        }
        return  dict
    def default(self, elf):
        if isinstance(elf, Elf):
            return self.encodeJSON(elf)
        else:
            super().default(self,elf)

elf = Elf(level=4)
print(elf.encodeJSON())
print(json.dumps(elf.encodeJSON(), indent=4))

with open("elf.json", "w") as read_file:
    json.dump(elf, read_file, indent=4, default=Elf.encodeJSON)

# elfEncoder = ElfEncoder()
# with open("elf_class.json", "w") as write_file:
#     json.dump(elfEncoder.encode(elf), write_file, indent=4)

z = 3 + 8j
print(type(z))


print(z.real)
print(z.imag)

print(complex(3,8) == z)

def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

encode = encode_complex(complex(3,8))
print(type(encode))

encode_json = json.dumps(9+5j, default=encode_complex)
print(type(encode_json))