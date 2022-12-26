from typing import Dict

from src.util.file_util import read_input_file


class Room:
    room_name: str
    sector_id: int
    checksum: str

    def __init__(self, line: str):
        self.checksum = line[-6:-1]
        self.sector_id = int(line[:-7].split("-")[-1])
        self.room_name = "-".join(line.split("-")[:-1])

    def is_real(self) -> bool:
        letters: Dict[str, int] = {}
        for num in range(ord("a"), ord("z") + 1):
            letter = chr(num)
            letters[letter] = self.room_name.count(letter)

        most_used = list(letters.values())
        most_used.sort(reverse=True)

        for i in range(5):
            letter = self.checksum[i]
            if letters[letter] != most_used[i]:
                return False

        return True

    def decrypt(self) -> str:
        decrypted = ""
        for letter in self.room_name:
            if letter == "-":
                decrypted += " "
            else:
                decrypted += chr((ord(letter) - ord("a") + self.sector_id) % 26 + ord("a"))
        return decrypted


def day_04_1() -> int:
    lines = read_input_file(4)
    rooms = list(map(Room, lines))
    return sum(map(lambda r: r.sector_id, filter(lambda r: r.is_real(), rooms)))


def day_04_2() -> int:
    lines = read_input_file(4)
    rooms = list(map(Room, lines))
    for room in rooms:
        decrypted = room.decrypt()
        if "north" in decrypted and "pole" in decrypted and "object" in decrypted:
            return room.sector_id
    raise ValueError("Couldn't find north pole objects")


if __name__ == "__main__":
    print(f"Sum sectors: {day_04_1()}")
    print(f"North pole objects: {day_04_2()}")
