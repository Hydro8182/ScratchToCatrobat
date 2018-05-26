from scratchtocatrobat.scratch.scratch3 import visitBlockAlt, get_block, visitGeneric, testglobalmap
from scratchtocatrobat.scratch.scratch3 import Scratch3Block


def visitSubtract(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["-", operand1, operand2]

def visitGt(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return [">", operand1, operand2]

def visitJoin(block, blockmap):
    operand1 = visitOperand(block, "STRING1")
    operand2 = visitOperand(block, "STRING2")
    return ["concatenate:with:", operand1, operand2]

def visitLetter_of(block, blockmap):
    letter = visitOperand(block, "LETTER")
    string = visitOperand(block, "STRING")
    return ["letter:of:", letter, string]

def visitLt(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["<", operand1, operand2]

def visitNot(block, blockmap):
    operand1 = visitOperand(block, "OPERAND")
    return ["not", operand1]

def visitMod(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["%", operand1, operand2]

def visitAdd(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["+", operand1, operand2]

def visitEquals(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["=", operand1, operand2]

def visitMathop(block, blockmap):
    num1 = visitBlockAlt(get_block(block.inputs["NUM"][1][1]), blockmap)
    operation = block.fields["OPERATOR"][0]
    return ["computeFunction:of:", operation, num1]

def visitAnd(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["&", operand1, operand2]

def visitRound(block, blockmap):
    operand1 = visitOperand(block, "NUM")
    return ["rounded", operand1]

def visitMultiply(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["*", operand1, operand2]

def visitRandom(block, blockmap):
    from_param = visitOperand(block, "FROM")
    to_param = visitOperand(block, "TO")
    return ["randomFrom:to:", from_param, to_param]

def visitDivide(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["/", operand1, operand2]


def visitContains(block, blockmap):
    operand1 = visitOperand(block, "STRING1")
    operand2 = visitOperand(block, "STRING2")
    return ["contains:", operand1, operand2]
    #TODO: not in scratch2?


def visitOr(block, blockmap):
    operand1 = visitOperand(block, "OPERAND1")
    operand2 = visitOperand(block, "OPERAND2")
    return ["|", operand1, operand2]

def visitLength(block, blockmap):
    operand1 = visitOperand(block, "STRING")
    return ["stringLength:", operand1]

def visitOperand(block, operandname):
    if operandname in block.inputs:
        operandblock = get_block(block.inputs[operandname][1])
        if isinstance(operandblock, Scratch3Block):
            operand = visitBlockAlt(operandblock, testglobalmap)
            return operand[0]
        else:
            operand = block.inputs[operandname][1][1]
            return operand

    return []