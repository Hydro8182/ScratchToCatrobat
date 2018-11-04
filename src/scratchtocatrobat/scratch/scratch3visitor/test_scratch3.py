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


    def test_visitWait(self):
        context = create_block_context("control_wait")
        testblock = context.block
        addInputOfType(testblock, "DURATION", TYPE_INT)
        addInputOfType(testblock, "SUBSTACK", TYPE_BLOCK)
        converted_block = visitBlock(context)
        assert converted_block[0] == "wait:elapsed:from:"
        assert converted_block[1] == 1234

    def test_visitRepat(self):
        context = create_block_context("control_repeat")
        testblock = context.block
        addInputOfType(testblock, "TIMES", TYPE_INT)
        testblock.fields["NUMBER_NAME"] = ["name"]
        converted_block = visitBlock(context)
        assert converted_block[0] == "doRepeat"
        assert converted_block[1] == 1234
        assert converted_block[1][0][0] == "say:"


    def test_visitIf(self):
        context = create_block_context("control_if")
        testblock = context.block
        addInputOfType(testblock, "CONDITION", TYPE_BLOCK)
        addInputOfType(testblock, "SUBSTACK", TYPE_BLOCK)
        converted_block = visitBlock(context)
        assert converted_block[0] == "doIf"
        assert converted_block[1][0][0] == "say:"


    def test_visitIfelse(self):
        context = create_block_context("control_if_else")
        testblock = context.block
        addInputOfType(testblock, "CONDITION", TYPE_BLOCK)
        addInputOfType(testblock, "SUBSTACK1", TYPE_BLOCK)
        addInputOfType(testblock, "SUBSTACK2", TYPE_BLOCK)
        converted_block = visitBlock(context)
        assert converted_block[0] == "doIfElse"
        assert converted_block[1][0][0] == "say:"

        # assert converted_block[1] == 1234

    def test_visitWait_until(self):
        context = create_block_context("control_wait_until")
        testblock = context.block
        addInputOfType(testblock, "CONDITION", TYPE_BLOCK)
        converted_block = visitBlock(context)
        assert converted_block[0] == "doWaitUntil"
        assert converted_block[1][0][0] == "say:"

        # assert converted_block[1] == 1234

    def test_visitRepeat_until(self):
        context = create_block_context("control_repeat_until")
        testblock = context.block
        addInputOfType(testblock, "CONDITION", TYPE_BLOCK)
        addInputOfType(testblock, "SUBSTACK", TYPE_BLOCK)
        converted_block = visitBlock(context)
        assert converted_block[0] == "doUntil"
        assert converted_block[1][0][0] == "say:"

        # assert converted_block[1] == 1234

    def test_visitCreate_clone_of(self):
        context = create_block_context("control_create_clone_of")
        testblock = context.block
        menu_block = add_new_block_to_context(context, "control_create_clone_of_menu")
        menu_block.fields["CLONE_OPTION"] = ["_myself_"]

        testblock.inputs["CLONE_OPTION"] = [1, menu_block.name]

        # addInputOfType(testblock, "CLONE_OPTION", TYPE_BLOCK)
        # addInputToBlock(testblock, "CLONE_OPTION", [1,])

        converted_block = visitBlock(context)
        assert converted_block[0] == "createCloneOf"
        assert converted_block[1] == "_myself_"

    def test_visitStop(self):
        context = create_block_context("control_stop")
        testblock = context.block
        testblock.fields["STOP_OPTION"] = ["stopthisscript"]
        converted_block = visitBlock(context)
        assert converted_block[0] == "stopScripts"
        assert converted_block[1][0][0] == "say:"


    def test_visitStart_as_clone(self):
        context = create_block_context("control_start_as_clone")
        testblock = context.block
        converted_block = visitBlock(context)
        assert converted_block[0] == "whenCloned"
        assert converted_block[1][0][0] == "say:"


    def test_visitDelete_this_clone(self):
        context = create_block_context("control_delete_this_clone")
        testblock = context.block
        converted_block = visitBlock(context)
        assert converted_block[0] == "deleteClone"
        assert converted_block[1][0][0] == "say:"


    def test_visitForever(self):
        context = create_block_context("control_forever")
        testblock = context.block
        sayblock = createScratch3Block(context, "looks_say")
        context.spriteblocks[sayblock.name] = sayblock
        testblock.inputs["SUBSTACK"] = [1, sayblock.name]
        addInputOfType(sayblock, "MESSAGE", TYPE_STRING)
        converted_block = visitBlock(context)
        assert converted_block[0] == "doForever"
        assert converted_block[1][0][0] == "say:"

if __name__ == "__main__":
    unittest.main()
