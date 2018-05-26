from pprint import pprint

testglobalmap = dict()

def get_block(blockid):
    if blockid in testglobalmap.keys():
        return testglobalmap[blockid]
    return blockid

def visitBlockAlt(block, blockmap):
    if not isinstance(block, Scratch3Block):
        return block
    blocklist = []
    while block != None:
        blocklist.append(visitormap[block.opcode](block, blockmap))
        block = block.nextBlock
    pprint(blocklist)
    return blocklist

def visitGeneric(block, attributename):
    if attributename in block.inputs:
        substackstartblock = get_block(block.inputs[attributename][1])
        if isinstance(substackstartblock, Scratch3Block):
            blocklist = visitBlockAlt(substackstartblock, testglobalmap)
            return blocklist
    return []



class Scratch3Sprite(object):
    def __init__(self):
        self.isStage = False
        self.objName = "__UNSET__"
        self.variables = []
        self.lists = []
        self.scripts = []
        self.sounds = []
        self.costumes = []
        self.currentCostumeIndex = 0
        self.scratchX = 0
        self.scratchY = 0
        self.scale = 1
        self.direction = 90
        self.rotationStyle = "normal"
        self.isDraggable = False
        self.visible = False
        self.spriteInfo = []

class Scratch3Script(object):
    def __init__(self):
        self.isStage = False
    def getNextBlock(self, currentblock):
        return self.blocks[currentblock.next]

    def getNextBlockScratch2(self, currentblock):
        return currentblock.child

class Scratch3Costume(object):
    def __init__(self):
        self.assetId = "cd21514d0531fdffb22204e0ec5ed84a"
        self.name = "backdrop1"
        self.md5ext = "cd21514d0531fdffb22204e0ec5ed84a.svg"
        self.dataFormat = "svg"
        self.rotationCenterX = 0
        self.rotationCenterY = 0

    pass


class Scratch3Sound(object):
    def __init__(self):
        self.assetId = "83a9787d4cb6f3b7632b4ddfebf74367"
        self.name = "pop"
        self.dataFormat = "wav"
        self.format = ""
        self.rate = 48000
        self.sampleCount = 1123
        self.md5ext = "83a9787d4cb6f3b7632b4ddfebf74367.wav"
        pass







class Scratch3Block(object):

    def __init__(self, block, name):
        self.name = name
        self.opcode = block["opcode"]
        self.nextName = block["next"]
        self.parentName = block["parent"]
        self.nextBlock = None
        self.parentBlock = None
        self.inputs = block["inputs"]
        self.fields = block["fields"]
        self.topLevel = block["topLevel"]
        self.shadow = block["shadow"]
        self.x = 0
        self.y = 0
        if self.topLevel:
            self.x = block["x"]
            self.y = block["y"]

    # pass
    # class type (object):
    #     FORMULA = 1
    # def visitblock(self, block):
    #     scratch3_to_scratch2_map = {
    #         "event_broadcast" : ["whenIReceive", ("inputs", "BROADCAST_INPUT", 1, 2)] #"whenIReceive", "Trees"
    #     }
    #     if not "opcode" in scratch3_to_scratch2_map:
    #         return block
    #     keys = scratch3_to_scratch2_map["opcode"]
    #
    #     newname = keys[0]
    #
    #     for key in keys[1:]:
    #         if  key in block["inputs"]:
    #
    #             #blockvalue = block["inputs"][key]
    #             def search(json_pos, list):
    #                 if len(list) == 0:
    #                     return self.visitblock(json_pos)
    #
    #                 else:
    #                     return search(json_pos[list[0]], list[1:])
    #
    #             blockvalue = search(block, keys)





# "y%sx.1U$*5ORAHMlDK5D":{
#     "next":null,
#     "opcode":"event_broadcast",
#     "parent":"[bI:rFG}?Cfu7B`_=o5x",
#     "inputs":{
#         "BROADCAST_INPUT":[
#             1,
#             [
#                 11,
#                 "message1",
#                 "PtPY47g*YB=o?D!f@U_C"
#             ]
#         ]
#     },




class Scratch3Project(object):
    def __init__(self):
        self.targets = []
        self.meta = { "semver":"3.0.0",
                      "vm":"0.1.0-prerelease.1526320682",
                      "agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
        self.name = "Untitled"
        self.sprites = []
class Scratch3Parser(object):
    scratch2dict = {}

    def __init__(self, file_path):
        import json
        print file_path
        with open(file_path, "r") as file:
            self.raw_dict = json.load(file)

    def parse_sprites(self):
        sprites = self.raw_dict["targets"]
        project = Scratch3Project()

        for sprite in sprites:
            self.parse_sprite(project, sprite)
        return project

    def parse_sprite(self, project, sprite):
        #project.sprites.append(Scratch3Sprite(sprite))
        #pprint(sprite["blocks"])

        script_blocks = []
        temp_block_dict = {}
        for block in sprite["blocks"]:
            temp_block_dict[block] = Scratch3Block(sprite["blocks"][block], block)

        for blockId in temp_block_dict:
            self.build_block_structure(blockId, temp_block_dict)

        for blockId in temp_block_dict:
            if temp_block_dict[blockId].topLevel:
                script_blocks.append(temp_block_dict[blockId])

        #test
        global testglobalmap
        testglobalmap = temp_block_dict
        for block in script_blocks:
            print "------------"
            self.printLinkedBlockList(block, temp_block_dict)
            visitBlockAlt(block, temp_block_dict)



    def printLinkedBlockList(self, block, temp_block_dict):
        #TODO: unhardcode this
        # print(block.opcode)
        group = block.opcode.split('_')[0]
        blockcode = "_".join(block.opcode.split('_')[1:])
        blockcode = blockcode[0].upper() + blockcode[1:]
        # print( '"'+block.opcode+"\" : scratch3visitor." + group + ".visit" + blockcode + ",")
        # if "CONDITION" in block.inputs:
        #     print "--condition--"
        #     self.printLinkedBlockList(temp_block_dict[block.inputs["CONDITION"][1]], temp_block_dict)
        # if "SUBSTACK" in block.inputs:
        #     print "--substack--"
        #     self.printLinkedBlockList(temp_block_dict[block.inputs["SUBSTACK"][1]], temp_block_dict)
        # if "SUBSTACK2" in block.inputs:
        #     print "--substack2--"
        #     self.printLinkedBlockList(temp_block_dict[block.inputs["SUBSTACK2"][1]], temp_block_dict)
        if block.nextBlock is None:
            return
        self.printLinkedBlockList(block.nextBlock, temp_block_dict)

    def build_block_structure(self, blockId, temp_block_dict):
        block = temp_block_dict[blockId]
        if block.nextName is not None:
            block.nextBlock = temp_block_dict[block.nextName]
        if block.parentName is not None:
            block.parentBlock = temp_block_dict[block.parentName]

    def parse_scripts(self):
        pass
    def parse_script(self, script):
        pass

import scratch3visitor.event
import scratch3visitor.control
import scratch3visitor.looks
import scratch3visitor.sensing
import scratch3visitor.motion
import scratch3visitor.sound
import scratch3visitor.data
import scratch3visitor.operator


def notimplemented(x,y):
    print "block not implemented"
    assert False

visitormap = {
    "sensing_touchingobjectmenu" : scratch3visitor.sensing.visitTouchingObjectMenu,


    "event_whenflagclicked" : scratch3visitor.event.visitWhenflagclicked,
    "motion_movesteps" : scratch3visitor.motion.visitMovesteps,
    "motion_turnright" : scratch3visitor.motion.visitTurnright,
    "motion_turnleft" : scratch3visitor.motion.visitTurnleft,
    "motion_goto" : scratch3visitor.motion.visitGoto,
    "motion_gotoxy" : scratch3visitor.motion.visitGotoxy,
    "motion_glideto" : scratch3visitor.motion.visitGlideto,
    "motion_glidesecstoxy" : scratch3visitor.motion.visitGlidesecstoxy,
    "motion_pointindirection" : scratch3visitor.motion.visitPointindirection,
    "motion_pointtowards" : scratch3visitor.motion.visitPointtowards,
    "motion_changexby" : scratch3visitor.motion.visitChangexby,
    "motion_setx" : scratch3visitor.motion.visitSetx,
    "motion_changeyby" : scratch3visitor.motion.visitChangeyby,
    "motion_sety" : scratch3visitor.motion.visitSety,
    "motion_ifonedgebounce" : scratch3visitor.motion.visitIfonedgebounce,
    "motion_setrotationstyle" : scratch3visitor.motion.visitSetrotationstyle,
    "looks_sayforsecs" : scratch3visitor.looks.visitSayforsecs,
    "looks_say" : scratch3visitor.looks.visitSay,
    "looks_thinkforsecs" : scratch3visitor.looks.visitThinkforsecs,
    "looks_think" : scratch3visitor.looks.visitThink,
    "looks_switchcostumeto" : scratch3visitor.looks.visitSwitchcostumeto,
    "looks_nextcostume" : scratch3visitor.looks.visitNextcostume,
    "looks_switchbackdropto" : scratch3visitor.looks.visitSwitchbackdropto,
    "looks_nextbackdrop" : scratch3visitor.looks.visitNextbackdrop,
    "looks_changesizeby" : scratch3visitor.looks.visitChangesizeby,
    "looks_setsizeto" : scratch3visitor.looks.visitSetsizeto,
    "looks_changeeffectby" : scratch3visitor.looks.visitChangeeffectby,
    "looks_seteffectto" : scratch3visitor.looks.visitSeteffectto,
    "looks_cleargraphiceffects" : scratch3visitor.looks.visitCleargraphiceffects,
    "looks_show" : scratch3visitor.looks.visitShow,
    "looks_hide" : scratch3visitor.looks.visitHide,
    "looks_gotofrontback" : scratch3visitor.looks.visitGotofrontback,
    "looks_goforwardbackwardlayers" : scratch3visitor.looks.visitGoforwardbackwardlayers,

    "sound_play" : scratch3visitor.sound.visitPlay,
    "sound_playuntildone" : scratch3visitor.sound.visitPlayuntildone,
    "sound_stopallsounds" : scratch3visitor.sound.visitStopallsounds,
    "sound_changeeffectby" : scratch3visitor.sound.visitChangeeffectby,
    "sound_seteffectto" : scratch3visitor.sound.visitSeteffectto,
    "sound_cleareffects" : scratch3visitor.sound.visitCleareffects,
    "sound_changevolumeby" : scratch3visitor.sound.visitChangevolumeby,
    "sound_setvolumeto" : scratch3visitor.sound.visitSetvolumeto,
    "event_broadcast" : scratch3visitor.event.visitBroadcast,
    "event_broadcastandwait" : scratch3visitor.event.visitBroadcastandwait,
    "control_wait" : scratch3visitor.control.visitWait,
    "control_repeat" : scratch3visitor.control.visitRepeat,
    "control_if" : scratch3visitor.control.visitIf,
    "control_if_else" : scratch3visitor.control.visitIf_else,
    "control_wait_until" : scratch3visitor.control.visitWait_until,
    "control_repeat_until" : scratch3visitor.control.visitRepeat_until,
    "control_create_clone_of" : scratch3visitor.control.visitCreate_clone_of,
    "control_stop" : scratch3visitor.control.visitStop,

    "control_start_as_clone" : scratch3visitor.control.visitStart_as_clone,
    "control_forever" : scratch3visitor.control.visitForever,
    "control_delete_this_clone" : scratch3visitor.control.visitDelete_this_clone,

    "sensing_askandwait" : scratch3visitor.sensing.visitAskandwait,
    "sensing_setdragmode" : scratch3visitor.sensing.visitSetdragmode,
    "sensing_resettimer" : scratch3visitor.sensing.visitResettimer,
    "data_setvariableto" : scratch3visitor.data.visitSetvariableto,
    "data_changevariableby" : scratch3visitor.data.visitChangevariableby,
    "data_showvariable" : scratch3visitor.data.visitShowvariable,
    "data_hidevariable" : scratch3visitor.data.visitHidevariable,

    "sensing_distanceto" : scratch3visitor.sensing.visitDistanceto,
    "looks_costumenumbername" : scratch3visitor.looks.visitCostumenumbername,
    "sensing_loudness" : scratch3visitor.sensing.visitLoudness,
    "sensing_coloristouchingcolor" : scratch3visitor.sensing.visitColoristouchingcolor,
    "sensing_of" : scratch3visitor.sensing.visitOf,
    "sensing_current" : scratch3visitor.sensing.visitCurrent,
    "looks_size" : scratch3visitor.looks.visitSize,
    "motion_xposition" : scratch3visitor.motion.visitXposition,
    "sound_volume" : scratch3visitor.sound.visitVolume,
    "sensing_answer" : scratch3visitor.sensing.visitAnswer,
    "sensing_dayssince2000" : scratch3visitor.sensing.visitDayssince2000,
    "sensing_keypressed" : scratch3visitor.sensing.visitKeypressed,
    "sensing_keyoptions" : scratch3visitor.sensing.visitKey_options,
    "looks_backdropnumbername" : scratch3visitor.looks.visitBackdropnumbername,
    "sensing_mousex" : scratch3visitor.sensing.visitMousex,
    "sensing_mousedown" : scratch3visitor.sensing.visitMousedown,
    "sensing_mousey" : scratch3visitor.sensing.visitMousey,
    "motion_yposition" : scratch3visitor.motion.visitYposition,
    "sensing_timer" : scratch3visitor.sensing.visitTimer,
    "sensing_touchingcolor" : scratch3visitor.sensing.visitTouchingcolor,
    "motion_direction" : scratch3visitor.motion.visitDirection,
    "sensing_touchingobject" : scratch3visitor.sensing.visitTouchingObject,

    "event_whenbroadcastreceived" : scratch3visitor.event.visitWhenbroadcastreceived,
    "operator_subtract" : scratch3visitor.operator.visitSubtract,
    "operator_gt" : scratch3visitor.operator.visitGt,
    "operator_join" : scratch3visitor.operator.visitJoin,
    "operator_letter_of" : scratch3visitor.operator.visitLetter_of,
    "event_whenbackdropswitchesto" : scratch3visitor.event.visitWhenbackdropswitchesto,
    "operator_lt" : scratch3visitor.operator.visitLt,
    "operator_not" : scratch3visitor.operator.visitNot,
    "operator_mod" : scratch3visitor.operator.visitMod,
    "operator_add" : scratch3visitor.operator.visitAdd,
    "event_whengreaterthan" : scratch3visitor.event.visitWhengreaterthan,
    "operator_equals" : scratch3visitor.operator.visitEquals,
    "operator_mathop" : scratch3visitor.operator.visitMathop,
    "operator_and" : scratch3visitor.operator.visitAnd,
    "event_whenthisspriteclicked" : scratch3visitor.event.visitWhenthisspriteclicked,
    "operator_round" : scratch3visitor.operator.visitRound,
    "operator_multiply" : scratch3visitor.operator.visitMultiply,
    "operator_random" : scratch3visitor.operator.visitRandom,
    "operator_divide" : scratch3visitor.operator.visitDivide,
    "event_whenkeypressed" : scratch3visitor.event.visitWhenkeypressed,
    "operator_contains" : scratch3visitor.operator.visitContains,
    "operator_or" : scratch3visitor.operator.visitOr,
    "operator_length" : scratch3visitor.operator.visitLength,
    "sensing_username" : scratch3visitor.sensing.visitUsername,

    "sensing_of_object_menu" : scratch3visitor.sensing.visitOf_object_menu,


}
