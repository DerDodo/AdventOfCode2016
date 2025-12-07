import hashlib

from run_util import RunTimer


def calc_hash(text: str, hash_stretches: int) -> str:
    for _ in range(hash_stretches):
        text = hashlib.md5(text.encode()).hexdigest()
    return text


def get_key_triple(h: str) -> str | None:
    for i in range(len(h) - 2):
        if h[i] == h[i + 1] == h[i + 2]:
            return h[i]
    return None


def get_quintuples(h: str) -> set[str]:
    quintuples = set()
    for i in range(len(h) - 4):
        if h[i] == h[i + 1] == h[i + 2] == h[i + 3] == h[i + 4]:
            quintuples.add(h[i])
    return quintuples


def day_14(salt: str, hash_stretches: int) -> int:
    key_targets = []
    relevant_keys_start = 0
    keys = set()
    end = 100000
    i = 0
    while i < end:
        key_candidate = salt + str(i)
        hash_value = calc_hash(key_candidate, hash_stretches)
        quintuples = get_quintuples(hash_value)

        for key_i in range(relevant_keys_start, len(key_targets)):
            if key_targets[key_i][0] < i - 1000:
                relevant_keys_start += 1
            elif i - key_targets[key_i][2] < 1000 and key_targets[key_i][2] not in keys and key_targets[key_i][1] in quintuples:
                keys.add(key_targets[key_i][2])
                if len(keys) == 64:
                    end = i + 1000

        hash_triple = get_key_triple(hash_value)
        if hash_triple is not None:
            key_targets.append((i + 1000, hash_triple, i))

        i += 1
    if len(keys) < 64:
        raise RuntimeError("Couldn't find enough keys")

    key_list = list(keys)
    key_list.sort()
    return key_list[63]


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Index: {day_14('ngcjuoqr', 1)}, {day_14('ngcjuoqr', 2017)}")
    timer.print()


def test_day_14():
    assert (day_14("abc", 1), day_14("abc", 2017)) == (22728, 22551)
