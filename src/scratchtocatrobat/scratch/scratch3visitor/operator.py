from scratchtocatrobat.scratch.scratch3 import visitBlockAlt, get_block, visitGeneric, visitLiteral, testglobalmap


def visitSubtract(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "NUM1")
    operand2 = visitGeneric(blockcontext, "NUM2")
    return ["-", operand1, operand2]

def visitGt(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "OPERAND1")
    operand2 = visitGeneric(blockcontext, "OPERAND2")
    return [">", operand1, operand2]

def visitJoin(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "STRING1")
    operand2 = visitGeneric(blockcontext, "STRING2")
    return ["concatenate:with:", operand1, operand2]

def visitLetter_of(blockcontext):
    block = blockcontext.block
    letter = visitGeneric(blockcontext, "LETTER")
    string = visitGeneric(blockcontext, "STRING")
    return ["letter:of:", letter, string]

def visitLt(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "OPERAND1")
    operand2 = visitGeneric(blockcontext, "OPERAND2")
    return ["<", operand1, operand2]

def visitNot(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "OPERAND")
    return ["not", operand1]

def visitMod(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "NUM1")
    operand2 = visitGeneric(blockcontext, "NUM2")
    return ["%", operand1, operand2]

def visitAdd(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "NUM1")
    operand2 = visitGeneric(blockcontext, "NUM2")
    return ["+", operand1, operand2]

def visitEquals(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "OPERAND1")
    operand2 = visitGeneric(blockcontext, "OPERAND2")
    return ["=", operand1, operand2]

def visitMathop(blockcontext):
    block = blockcontext.block
    #num1 = visitBlockAlt(get_block(block.inputs["NUM"][1][1]), blockmap)
    num1 = visitGeneric(blockcontext, "NUM")
    operation = block.fields["OPERATOR"][0]
    return ["computeFunction:of:", operation, num1]

def visitAnd(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "OPERAND1")
    operand2 = visitGeneric(blockcontext, "OPERAND2")
    return ["&", operand1, operand2]

def visitRound(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "NUM")
    return ["rounded", operand1]

def visitMultiply(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "NUM1")
    operand2 = visitGeneric(blockcontext, "NUM2")
    return ["*", operand1, operand2]

def visitRandom(blockcontext):
    block = blockcontext.block
    from_param = visitGeneric(blockcontext, "FROM")
    to_param = visitGeneric(blockcontext, "TO")
    return ["randomFrom:to:", from_param, to_param]

def visitDivide(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "NUM1")
    operand2 = visitGeneric(blockcontext, "NUM2")
    return ["/", operand1, operand2]


def visitContains(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "STRING1")
    operand2 = visitGeneric(blockcontext, "STRING2")
    return ["contains:", operand1, operand2]
    #TODO: not in scratch2?


def visitOr(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "OPERAND1")
    operand2 = visitGeneric(blockcontext, "OPERAND2")
    return ["|", operand1, operand2]

def visitLength(blockcontext):
    block = blockcontext.block
    operand1 = visitGeneric(blockcontext, "STRING")
    return ["stringLength:", operand1]
