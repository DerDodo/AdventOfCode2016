import hashlib

from run_util import RunTimer


def day_05_1(key: str, password_length: int) -> str:
    password = ""
    for i in range(1000000000):
        hash_id = hashlib.md5((key + str(i)).encode()).hexdigest()
        if hash_id[0:5] == "00000":
            password += hash_id[5]
            print(f"    Password: {password}", flush=True)
            if len(password) == password_length:
                return password
    raise ValueError(f"Couldn't find password for {key}")


def day_05_2(key: str, password_length: int) -> str:
    password = ["_" for _ in range(password_length)]
    num_found = 0
    for i in range(10000000000):
        hash_id = hashlib.md5((key + str(i)).encode()).hexdigest()
        if hash_id[0:5] == "00000":
            print(f"    Found hash {hash_id[0:7]}", flush=True)
            if hash_id[5].isdecimal() and int(hash_id[5]) < password_length and password[int(hash_id[5])] == "_":
                password[int(hash_id[5])] = hash_id[6]
                print(f"    Password: {''.join(password)}", flush=True)
                num_found += 1
                if num_found == password_length:
                    return "".join(password)
    raise ValueError(f"Couldn't find password for {key}")


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Password (1): {day_05_1('ugkcyxxp', 8)}")
    print(f"Password (2): {day_05_2('ugkcyxxp', 8)}")
    timer.print()


def test_day_05():
    assert day_05_1("abc", 3) == "18f"
    assert day_05_2("abc", 2) == "05"
