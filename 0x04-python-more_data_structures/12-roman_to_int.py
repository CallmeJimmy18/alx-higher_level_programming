#!/usr/bin/python3
def subt(list_num):
    sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            sub += n

    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}

    rom_list = list(rom_n.keys())
    last_rom = 0
    list_num = []
    num = 0

    for r in roman_string:
        for i in rom_list:
            if i == r:
                if rom_n.get(r) <= last_rom:
                    num += subt(list_num)
                    list_num = [rom_n.get(r)]
                else:
                    list_num.append(rom_n)
                last_rom = rom_n.get(r)

    num += subt(list_num)
    return num
