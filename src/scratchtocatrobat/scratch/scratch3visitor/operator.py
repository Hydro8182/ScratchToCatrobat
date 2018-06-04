from scratchtocatrobat.scratch.scratch3 import visitBlockAlt, get_block, visitGeneric, visitLiteral, testglobalmap


def visitSubtract(block):
    operand1 = visitGeneric(block, "NUM1")
    operand2 = visitGeneric(block, "NUM2")
    return ["-", operand1, operand2]

def visitGt(block):
    operand1 = visitGeneric(block, "OPERAND1")
    operand2 = visitGeneric(block, "OPERAND2")
    return [">", operand1, operand2]

def visitJoin(block):
    operand1 = visitGeneric(block, "STRING1")
    operand2 = visitGeneric(block, "STRING2")
    return ["concatenate:with:", operand1, operand2]

def visitLetter_of(block):
    letter = visitGeneric(block, "LETTER")
    string = visitGeneric(block, "STRING")
    return ["letter:of:", letter, string]

def visitLt(block):
    operand1 = visitGeneric(block, "OPERAND1")
    operand2 = visitGeneric(block, "OPERAND2")
    return ["<", operand1, operand2]

def visitNot(block):
    operand1 = visitGeneric(block, "OPERAND")
    return ["not", operand1]

def visitMod(block):
    operand1 = visitGeneric(block, "NUM1")
    operand2 = visitGeneric(block, "NUM2")
    return ["%", operand1, operand2]

def visitAdd(block):
    operand1 = visitGeneric(block, "NUM1")
    operand2 = visitGeneric(block, "NUM2")
    return ["+", operand1, operand2]

def visitEquals(block):
    operand1 = visitGeneric(block, "OPERAND1")
    operand2 = visitGeneric(block, "OPERAND2")
    return ["=", operand1, operand2]

def visitMathop(block):
    #num1 = visitBlockAlt(get_block(block.inputs["NUM"][1][1]), blockmap)
    num1 = visitGeneric(block, "NUM")
    operation = block.fields["OPERATOR"][0]
    return ["computeFunction:of:", operation, num1]

def visitAnd(block):
    operand1 = visitGeneric(block, "OPERAND1")
    operand2 = visitGeneric(block, "OPERAND2")
    return ["&", operand1, operand2]

def visitRound(block):
    operand1 = visitGeneric(block, "NUM")
    return ["rounded", operand1]

def visitMultiply(block):
    operand1 = visitGeneric(block, "NUM1")
    operand2 = visitGeneric(block, "NUM2")
    return ["*", operand1, operand2]

def visitRandom(block):
    from_param = visitGeneric(block, "FROM")
    to_param = visitGeneric(block, "TO")
    return ["randomFrom:to:", from_param, to_param]

def visitDivide(block):
    operand1 = visitGeneric(block, "NUM1")
    operand2 = visitGeneric(block, "NUM2")
    return ["/", operand1, operand2]


def visitContains(block):
    operand1 = visitGeneric(block, "STRING1")
    operand2 = visitGeneric(block, "STRING2")
    return ["contains:", operand1, operand2]
    #TODO: not in scratch2?


def visitOr(block):
    operand1 = visitGeneric(block, "OPERAND1")
    operand2 = visitGeneric(block, "OPERAND2")
    return ["|", operand1, operand2]

def visitLength(block):
    operand1 = visitGeneric(block, "STRING")
    return ["stringLength:", operand1]
