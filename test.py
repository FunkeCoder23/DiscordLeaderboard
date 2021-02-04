from re import findall


def getIdFromAt(arg, args=None):
    reg = '[0-9]*'
    id = findall(reg, arg)[3]
    good = id.isnumeric()
    return (id, good)


# , "THIS IS A SHITPASTA TEST")
(id, good) = getIdFromAt("<@!310479313814159364>", "test")
print(good)
print(id)
