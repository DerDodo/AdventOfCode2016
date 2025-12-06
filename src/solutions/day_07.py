from file_util import read_input_file
from run_util import RunTimer


def read_input() -> list[str]:
    return read_input_file(7)


def is_abba(text: str) -> bool:
    return text[0] == text[3] and text[1] == text[2] and text[0] != text[1]


def is_aba(text: str) -> bool:
    return text[0] == text[2] and text[0] != text[1]


def supports_tls(ip_address: str) -> bool:
    in_brackets = 0
    had_correct_abba = False
    for i in range(len(ip_address) - 3):
        if ip_address[i] == "[":
            in_brackets += 1
        elif ip_address[i] == "]":
            in_brackets -= 1
        if is_abba(ip_address[i:i+4]):
            if in_brackets > 0:
                return False
            had_correct_abba = True
    return had_correct_abba


def supports_ssl(ip_address: str) -> bool:
    in_brackets = 0
    abas = set()
    inverted_babs = set()
    for i in range(len(ip_address) - 2):
        if ip_address[i] == "[":
            in_brackets += 1
        elif ip_address[i] == "]":
            in_brackets -= 1
        if is_aba(ip_address[i:i+4]):
            if in_brackets > 0:
                inverted_babs.add(f"{ip_address[i+1]}{ip_address[i]}{ip_address[i+1]}")
            else:
                abas.add(ip_address[i:i+3])
    return len(abas.intersection(inverted_babs)) > 0


def day_07() -> tuple[int, int]:
    ip_addresses = read_input()
    num_support_tls = sum([1 if supports_tls(ip_address) else 0 for ip_address in ip_addresses])
    num_support_ssl = sum([1 if supports_ssl(ip_address) else 0 for ip_address in ip_addresses])
    return num_support_tls, num_support_ssl


if __name__ == "__main__":
    timer = RunTimer()
    print(f"Num ips: {day_07()}")
    timer.print()


def test_day_07():
    assert day_07() == (3, 3)
