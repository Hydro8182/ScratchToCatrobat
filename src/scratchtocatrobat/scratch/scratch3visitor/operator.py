from scratchtocatrobat.scratch.scratch3 import visitBlockAlt, get_block
from scratchtocatrobat.scratch.scratch3 import Scratch3Block
def visitSubtract(block, blockmap):
    pass

def visitGt(block, blockmap):
    pass

def visitJoin(block, blockmap):
    pass

def visitLetter_of(block, blockmap):
    pass

def visitLt(block, blockmap):
    pass

def visitNot(block, blockmap):
    pass

def visitMod(block, blockmap):
    pass

def visitAdd(block, blockmap):
    block1 = get_block(block.inputs["NUM1"][1], blockmap)
    block2 = get_block(block.inputs["NUM2"][1], blockmap)

    if isinstance(block1, Scratch3Block):
        num1 = visitBlockAlt(block1, blockmap)
    else:
        num1 = block1[1]

    if isinstance(block2, Scratch3Block):
        num2 = visitBlockAlt(block2, blockmap)
    else:
        num2 = block2[1]

    return ["add", num1, num2]

def visitEquals(block, blockmap):
    pass

def visitMathop(block, blockmap):
    num1 = visitBlockAlt(get_block(block.inputs["NUM"][1][1],blockmap), blockmap)
    operation = block.fields["OPERATOR"][0]
    return ["mathop", operation, num1]

def visitAnd(block, blockmap):
    pass

def visitRound(block, blockmap):
    pass

def visitMultiply(block, blockmap):
    pass

def visitRandom(block, blockmap):
    pass

def visitDivide(block, blockmap):
    pass


def visitContains(block, blockmap):
    pass

def visitOr(block, blockmap):
    pass

def visitLength(block, blockmap):
    pass

