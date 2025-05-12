def number_in_english(number: int):
    data = {
        '': '',
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninty',
    }
    if number in data:
        return data[number]
    elif number < 100:
        number = (number // 10 * 10, number % 10)
        return data[number[0]] + ' ' + data[number[1]]
    else:
        number = (number // 100, number % 100 if number % 100 in data else number % 100 // 10 * 10, number % 10 if number % 100 not in data else '')
        return data[number[0]] + ' hundred and ' + data[number[1]] + ' ' + data[number[2]]
