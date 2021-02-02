from random import randint
custom = {
    "@": ["<:at:759418946570027028>"],
}
lookup = {
    "A": ["a", "regional_indicator_a"],
    "B": ["b", "regional_indicator_b"],
    "C": ["regional_indicator_c", "copyright", "call_me", "ocean", "star_and_crescent", "arrow_right_hook", "compression"],
    "D": ["regional_indicator_d", "leftwards_arrow_with_hook", "dizzy"],
    "E": ["email", "regional_indicator_e"],
    "F": ["regional_indicator_f", "flags"],
    "G": ["regional_indicator_g"],
    "H": ["regional_indicator_h", "pisces"],
    "I": ["lipstick", "spoon", "regional_indicator_i", "information_source", "gemini", "warning"],
    "J": ["regional_indicator_j", "arrow_heading_up", "field_hockey"],
    "K": ["regional_indicator_k"],
    "L": ["mechanical_arm",  "regional_indicator_l", "boot"],
    "M": ["m", "regional_indicator_m", "virgo", "scorpius", "part_alternation_mark"],
    "N": ["regional_indicator_n", "capricorn", ],
    "O": ["ring", "ok_hand", "yarn", "full_moon_with_face", "soccer", "basketball", "baseball", "volleyball", "cd", "o2", "o", "regional_indicator_o"],
    "P": ["parking", "regional_indicator_p"],
    "Q": ["regional_indicator_q"],
    "R": ["regional_indicator_r", "registered"],
    "S": ["regional_indicator_s", "heavy_dollar_sign", "zap", "moneybag"],
    "T": ["regional_indicator_t", "cross"],
    "U": ["regional_indicator_u", "metal", "ophiuchus"],
    "V": ["regional_indicator_v", "v", "aries"],
    "W": ["regional_indicator_w", "love_you_gesture", "wavy_dash"],
    "X": ["x", "regional_indicator_x", "twisted_rightwards_arrows", "scissors", "crossed_swords", "tools"],
    "Y": ["regional_indicator_y", "chart"],
    "Z": ["regional_indicator_z", "zzz"],
    '1': ["first_place", "one"],
    '2': ["second_place", "two"],
    '3': ["third_place", "tree"],
    '4': ["four"],
    '5': ["five"],
    '6': ["six"],
    '7': ["seven"],
    '8': ["eight", "eight_ball"],
    '9': ["nine"],
    '0': ["zero", "arrows_clockwise"],
    '!': ["exclamation", "grey_exclamation", "heart_exclamation"],
    '?': ["question", "grey_question"],
}


def emojify(text):
    newText = ""
    for i in text:
        if i == ' ':
            newText += "⠀"
            continue
        if i.upper() not in custom and i.upper() not in lookup:
            newText += i
            continue
        for key, val in custom.items():
            if i.upper() == key:
                randInt = randint(0, len(val) - 1)
                newText = newText + " " + val[randInt]
                continue
        for key, val in lookup.items():
            if i.upper() == key:
                randInt = randint(0, len(val) - 1)
                newText = newText + ":" + val[randInt] + ":"
    return newText


def emoji(arg):
    response = emojify(arg)
    r = []
    i = 0
    while len(response) >= 2000:
        s = response.rfind('⠀', 0, 2000)
        res = response[:s]
        print('res', len(res))
        response = response[s+1:]
        print('response', len(response))
        r.append(res)
    r.append(response)
    for res in r:
        # print(res)
        print(len(res))


emoji("hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world hello world ")
