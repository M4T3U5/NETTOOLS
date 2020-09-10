def IntegerToBinary(val):
    string = "{0:b}".format(val)
    return string

def IntegerToHex(val):
    return hex(val)

def BinaryToInteger(val):
    return int(str(val), 2)

def BinaryToHex(val):
    return hex(BinaryToInteger(val))

def HextoInteger(val):
    return int(val, 16)

def HextoBinary(val):
    return IntegerToBinary(HextoInteger(val))


