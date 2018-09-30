import unittest
from  scratchtocatrobat.scratch.scratch3visitor.looks import *
from scratchtocatrobat.scratch.scratch3 import Scratch3Block
from scratchtocatrobat.scratch.scratch3visitor.visitorUtil import BlockContext, visitBlock
INPUTTYPE_LITERAL = 1
INPUTTYPE_BLOCK_NO_SHADOW = 2
INPUTTYPE_BLOCK = 3

TYPE_INT = 1
TYPE_STRING = 2
TYPE_BLOCK = 3
TYPE_VARIABLE = 4


def addInputToBlock(block, key, value, type=2, datatype=4):

    if type == INPUTTYPE_LITERAL:
        block.inputs[key] = [type, [datatype, value]]
    elif type == INPUTTYPE_BLOCK_NO_SHADOW:
        block.inputs[key] = [type, value]
    else:
        block.inputs[key] = [type, value, [2, "shadow_value"]]


def addInputOfType(block, key, type):

    if type == TYPE_INT:
        value = [1, [4, 1234]]
    elif type == TYPE_STRING:
        value = [1, [10, "teststring"]]
    else:
        return

    block.inputs[key] = value


def create_block_context(opcode):
    context = BlockContext(None, {})
    block = createScratch3Block(context, opcode)
    context.block = block
    context.spriteblocks[block.name] = block
    return context

def createScratch3Block(context, opcode):
    name = opcode + "_" + str(len(context.spriteblocks))
    block = {}
    block['name'] = name

    block['opcode'] = opcode
    block['inputs'] = {}
    block['fields'] = {}
    block["parent"] = None
    block["next"] = None
    block = Scratch3Block(block, name)

    return block

def add_new_block_to_context(context, opcode):
    block = createScratch3Block(context, opcode)
    context.spriteblocks[block.name] = block
    return block

def create_dummy_formula_block(context):
    operator = createScratch3Block(context, "operator_add")
    addInputOfType(operator, "NUM1", TYPE_INT)
    addInputOfType(operator, "NUM2", TYPE_INT)
    context.spriteblocks[operator.name] = operator
    return [INPUTTYPE_BLOCK_NO_SHADOW, operator.name]


def createDummyProject():

    pass

def createDummySprite():
    pass


class TestScratch3Blocks(unittest.TestCase):
    def setUp(self):
        pass

### Look block testcases ###################
    def test_showSpriteBlock(self):
        context = create_block_context("show")
        testblock = context.block
        addInputToBlock(testblock,"myval", 1)
        converted_block = visitBlock(context)

        assert converted_block

    def test_visitGoforwardbackwardlayers(self):
        context = create_block_context("looks_goforwardbackwardlayers")
        testblock = context.block
        testblock.fields["FORWARD_BACKWARD"] = ["forward"]
        addInputOfType(testblock, "NUM", TYPE_INT)
        converted_block = visitBlock(context)
        assert converted_block[0] == "goBackByLayers:"

    def test_visitGoforwardbackwardlayers_formula(self):
        context = create_block_context("looks_goforwardbackwardlayers")
        testblock = context.block
        testblock.fields["FORWARD_BACKWARD"] = ["forward"]
        formula = create_dummy_formula_block(context)
        testblock.inputs["NUM"] = formula
        converted_block = visitBlock(context)
        assert converted_block[0] == "goBackByLayers:"
        assert len(converted_block[1]) == 3
        assert converted_block[1][0] == "+"

    def test_visitSayforsecs(self):
        context = create_block_context("looks_sayforsecs")
        testblock = context.block
        addInputOfType(testblock, "SECS", TYPE_INT)
        addInputOfType(testblock, "MESSAGE", TYPE_STRING)

        converted_block = visitBlock(context)
        assert converted_block[0] == "say:duration:elapsed:from:"
        assert converted_block[1] == "teststring"
        assert converted_block[2] == 1234.0


    def test_visitSay(self):
        context = create_block_context("looks_say")
        testblock = context.block
        addInputOfType(testblock, "MESSAGE", TYPE_STRING)

        converted_block = visitBlock(context)
        assert converted_block[0] == "say:"
        assert converted_block[1] == "teststring"

    def test_visitThinkforsecs(self):
        context = create_block_context("looks_thinkforsecs")
        testblock = context.block
        addInputOfType(testblock, "MESSAGE", TYPE_STRING)
        addInputOfType(testblock, "SECS", TYPE_INT)

        converted_block = visitBlock(context)
        assert converted_block[0] == "think:duration:elapsed:from:"
        assert converted_block[1] == "teststring"
        assert converted_block[2] == 1234.0

    def test_visitThink(self):
        context = create_block_context("looks_think")
        testblock = context.block
        addInputOfType(testblock, "MESSAGE", TYPE_STRING)

        converted_block = visitBlock(context)
        assert converted_block[0] == "think:"
        assert converted_block[1] == "teststring"

    def test_visitSwitchCostumeTo(self):
        context = create_block_context("looks_switchcostumeto")
        testblock = context.block
        addInputOfType(testblock, "COSTUME", TYPE_STRING)

        block2 = add_new_block_to_context(context, "looks_costume")
        block2.fields["COSTUME"] = ["test_costume"]
        testblock.inputs["COSTUME"] = [1, block2.name]
        converted_block = visitBlock(context)
        assert converted_block[0] == "lookLike:"
        assert converted_block[1] == "test_costume"

    def test_visitNextCostume(self):
        context = create_block_context("looks_nextcostume")
        converted_block = visitBlock(context)
        assert converted_block[0] == "nextCostume"

    def test_visitSwitchBackdropTo(self):
        context = create_block_context("looks_switchbackdropto")
        testblock = context.block
        addInputOfType(testblock, "BACKDROP", TYPE_STRING)

        block2 = add_new_block_to_context(context, "looks_backdrops")
        block2.fields["BACKDROP"] = ["test_costume"]
        addInputToBlock(testblock, "BACKDROP", block2.name, INPUTTYPE_BLOCK_NO_SHADOW)
        testblock.inputs["BACKDROP"] = [1, block2.name]

        converted_block = visitBlock(context)
        assert converted_block[0] == "startScene"
        assert converted_block[1] == "test_costume"

    def test_visitChangesizeby(self):
        context = create_block_context("looks_changesizeby")
        testblock = context.block
        addInputOfType(testblock, "CHANGE", TYPE_INT)

        converted_block = visitBlock(context)
        assert converted_block[0] == "changeSizeBy:"
        assert converted_block[1] == 1234.0

    def test_visitSetsizeto(self):
        context = create_block_context("looks_setsizeto")
        testblock = context.block
        addInputOfType(testblock, "SIZE", TYPE_INT)

        converted_block = visitBlock(context)
        assert converted_block[0] == "setSizeTo:"
        assert converted_block[1] == 1234.0

    def test_visitChangeeffectby(self):
        context = create_block_context("looks_changeeffectby")
        testblock = context.block
        addInputOfType(testblock, "CHANGE", TYPE_INT)
        testblock.fields["EFFECT"] = ["testeffect"]
        converted_block = visitBlock(context)
        assert converted_block[0] == "changeGraphicEffect:by:"
        assert converted_block[1] == "testeffect"
        assert converted_block[2] == 1234.0

    def test_visitSeteffectto(self):
        context = create_block_context("looks_seteffectto")
        testblock = context.block
        addInputOfType(testblock, "VALUE", TYPE_INT)
        testblock.fields["EFFECT"] = ["testeffect"]
        converted_block = visitBlock(context)
        assert converted_block[0] == "setGraphicEffect:to:"
        assert converted_block[1] == "testeffect"
        assert converted_block[2] == 1234.0

    def test_visitCleargraphiceffects(self):
        context = create_block_context("looks_cleargraphiceffects")
        converted_block = visitBlock(context)
        assert converted_block[0] == "filterReset"

    def test_visitShow(self):
        context = create_block_context("looks_show")
        converted_block = visitBlock(context)
        assert converted_block[0] == "show"
    def test_visitHide(self):
        context = create_block_context("looks_hide")
        converted_block = visitBlock(context)
        assert converted_block[0] == "hide"

    def test_visitGotofrontback(self):
        context = create_block_context("looks_gotofrontback")
        converted_block = visitBlock(context)
        assert converted_block[0] == "comeToFront"

    # def test_visitCostumenumbername(self):
    #     context = create_block_context("looks_costumenumbername")
    #     testblock = context.block
    #     addInputOfType(testblock, "CHANGE", TYPE_INT)
    #     testblock.fields["NUMBER_NAME"] = ["name"]
    #     testblock.fields["EFFECT"] = ["testeffect"]
    #     converted_block = visitBlock(context)
    #     assert converted_block[0] == "costumeName"
    #
    #     testblock.fields["NUMBER_NAME"] = ["number"]
    #     converted_block = visitBlock(context)
    #     assert converted_block[0] == "costumeIndex"

    def test_visitSize(self):
        context = create_block_context("looks_size")
        converted_block = visitBlock(context)
        assert converted_block[0] == "scale"


    def test_visitMovesteps(self):
        context = create_block_context("motion_movesteps")
        testblock = context.block
        addInputOfType(testblock, "STEPS", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "forward:"
        assert converted_block[1] == 1234

    def test_visitTurnright(self):
        context = create_block_context("motion_turnright")
        testblock = context.block
        addInputOfType(testblock, "DEGREES", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "turnRight:"
        assert converted_block[1] == 1234

    def test_visitTurnleft(self):
        context = create_block_context("motion_turnleft")
        testblock = context.block
        addInputOfType(testblock, "DEGREES", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "turnLeft:"
        assert converted_block[1] == 1234

    def test_visitGotoxy(self):
        context = create_block_context("motion_gotoxy")
        testblock = context.block
        addInputOfType(testblock, "X", TYPE_INT)
        addInputOfType(testblock, "Y", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "gotoX:y:"
        assert converted_block[1] == 1234
        assert converted_block[2] == 1234

    def test_visitGoto(self):
        context = create_block_context("motion_goto")
        testblock = context.block
        addInputOfType(testblock, "TO", TYPE_STRING)
        converted_block = visitBlock(context)

        assert converted_block[0] == "gotoSpriteOrMouse:"
        assert converted_block[1] == "teststring"

    def test_visitGlideto(self):
        context = create_block_context("motion_glideto")
        testblock = context.block
        addInputOfType(testblock, "SECS", TYPE_INT)
        addInputOfType(testblock, "TO", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "glideTo:"
        assert converted_block[1] == 1234

    def test_visitGlidesecstoxy(self):
        context = create_block_context("motion_glidesecstoxy")
        testblock = context.block
        addInputOfType(testblock, "SECS", TYPE_INT)
        addInputOfType(testblock, "X", TYPE_INT)
        addInputOfType(testblock, "Y", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "glideSecs:toX:y:elapsed:from:"
        assert converted_block[1] == 1234
        assert converted_block[2] == 1234
        assert converted_block[3] == 1234

    def test_visitPointindirection(self):
        context = create_block_context("motion_pointindirection")
        testblock = context.block
        addInputOfType(testblock, "DIRECTION", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "heading:"
        assert converted_block[1] == 1234

    def test_visitPointtowards(self):
        context = create_block_context("motion_pointtowards")
        testblock = context.block
        addInputOfType(testblock, "TOWARDS", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "pointTowards:"
        assert converted_block[1] == 1234

    def test_visitChangexby(self):
        context = create_block_context("motion_changexby")
        testblock = context.block
        addInputOfType(testblock, "DX", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "changeXposBy:"
        assert converted_block[1] == 1234

    def test_visitChangeyby(self):
        context = create_block_context("motion_changeyby")
        testblock = context.block
        addInputOfType(testblock, "DY", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "changeYposBy:"
        assert converted_block[1] == 1234

    def test_visitSetx(self):
        context = create_block_context("motion_setx")
        testblock = context.block
        addInputOfType(testblock, "X", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "xpos:"
        assert converted_block[1] == 1234

    def test_visitSety(self):
        context = create_block_context("motion_sety")
        testblock = context.block
        addInputOfType(testblock, "Y", TYPE_INT)
        converted_block = visitBlock(context)

        assert converted_block[0] == "ypos:"
        assert converted_block[1] == 1234

    def test_visitIfonedgebounce(self):
        context = create_block_context("motion_ifonedgebounce")
        testblock = context.block
        converted_block = visitBlock(context)

        assert converted_block[0] == "bounceOffEdge"

    def test_visitSetrotationstyle(self):
        context = create_block_context("motion_setrotationstyle")
        testblock = context.block
        testblock.fields["STYLE"] = ["teststyle"]

        converted_block = visitBlock(context)

        assert converted_block[0] == "setRotationStyle"
        assert converted_block[1] == "teststyle"

    def test_visitDirection(self):
        context = create_block_context("motion_direction")
        testblock = context.block

        converted_block = visitBlock(context)

        assert converted_block[0] == "heading"

    def test_visitXposition(self):
        context = create_block_context("motion_xposition")
        testblock = context.block

        converted_block = visitBlock(context)

        assert converted_block[0] == "xpos"

    def test_visitYposition(self):
        context = create_block_context("motion_yposition")
        testblock = context.block

        converted_block = visitBlock(context)

        assert converted_block[0] == "ypos"

if __name__ == "__main__":
    unittest.main()
