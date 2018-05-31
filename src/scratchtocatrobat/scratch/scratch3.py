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
        subblock = visitormap[block.opcode](block, blockmap)
        blocklist.append(subblock)
        block = block.nextBlock
    if isinstance(blocklist[0], list) and len(blocklist) == 1:
        blocklist = blocklist[0]

    pprint(blocklist)
    return blocklist

def visitBlockList(block, blockmap):
    if not isinstance(block, Scratch3Block):
        return block
    blocklist = []
    while block != None:
        subblock = visitormap[block.opcode](block, blockmap)
        blocklist.append(subblock)
        block = block.nextBlock

    pprint(blocklist)
    return blocklist

def visitLiteral(literal):
    if literal[0] == 12:
        return ["readVariable", literal[1]]
    elif literal[0] == 5 or literal[0] == 6 or literal[0] == 7:
        if literal[1] == None:
            return 0
        return int(literal[1])
    elif literal[0] == 4 or literal[0] == 8:
        if literal[1] == '':
            return 0.0
        return float(literal[1])
    elif literal[0] == 9:
        return literal[1]
    else:
        return literal[1]


def visitGeneric(block, attributename):
    if attributename in block.inputs:
        substackstartblock = get_block(block.inputs[attributename][1])
        if isinstance(substackstartblock, Scratch3Block):
            blocklist = visitBlockAlt(substackstartblock, testglobalmap)
            if block.inputs[attributename][0] == 1:
                return blocklist[0]
            return blocklist
        return visitLiteral(block.inputs[attributename][1])
        # return get_block(block.inputs[attributename][1][1])
    return []


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

    def __init__(self, file_path, scratch_project_dir):
        import json
        print file_path
        with open(file_path, "r+") as file1:
            import glob
            import os
            from scratchtocatrobat.tools import common
            file_content = file1.read()
            for file in glob.glob(scratch_project_dir + "/*.*"):
                if not file.endswith(".json"):

                    file_hash = common.md5_hash(file)
                    newname = scratch_project_dir+"/"+ file_hash +"." +file.split(".")[-1]
                    os.rename(file, newname)
                    oldfile = "".join(file.split('/')[-1].split('.')[0:-1])
                    print oldfile
                    print file_hash
                    file_content = file_content.replace(oldfile ,file_hash)
            file1.flush()
            file1.write(file_content)
            self.raw_dict = json.loads(file_content)

    def parse_sprites(self):
        sprites = self.raw_dict["targets"]
        scratch2Data = {}
        scratch2Data['sprites'] = []
        stageSprite = {}

        for sprite in sprites:
            spriteContent = self.parse_sprite(sprite)
            if sprite["isStage"]:
                stageSprite = spriteContent
            else:
                scratch2Data['sprites'].append(spriteContent)

        stageSprite["children"] = []
        for sprite in scratch2Data['sprites']:
            stageSprite["children"].append(sprite)
        stageSprite["info"] = self.raw_dict["meta"]
        stageSprite["penLayerMD5"] = "Scratch3Doesn'tHaveThis"
        stageSprite["penLayerID"] = 0 #TODO: this doesn't exist in scratch3 what is this!?
        stageSprite["tempoBPM"] = 60
        stageSprite["videoAlpha"] = 0.5
        return stageSprite

    def parse_sprite(self, sprite):
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
        scratch2ProjectDict = {}
        #test
        global testglobalmap
        testglobalmap = temp_block_dict
        scratch2ProjectDict["scripts"] = []

        for block in script_blocks:
            print "------------"
            self.printLinkedBlockList(block, temp_block_dict)
            scratch2ProjectDict["scripts"] += [[1,1, visitBlockAlt(block, temp_block_dict)]]
        variables = []
        for var in sprite["variables"].values():
            curvar = {}
            curvar["name"] = var[0]
            curvar["value"] = var[1]
            curvar["isPersistent"] = var[2] if len(var) > 2 else False
            variables.append(curvar)
        scratch2ProjectDict["variables"] = variables
        scratch2ProjectDict["costumes"] = []
        for s3Costume in sprite["costumes"]:
            s2Costume = {}
            s2Costume["costumeName"] = s3Costume["name"]
            s2Costume["baseLayerID"] = s3Costume["assetId"]
            s2Costume["baseLayerMD5"] = s3Costume["md5ext"]
            s2Costume["rotationCenterX"]= s3Costume["rotationCenterX"]
            s2Costume["rotationCenterY"]= s3Costume["rotationCenterX"]
            if "bitmapResolution" in s3Costume:
                s2Costume["bitmapResolution"] = s3Costume["bitmapResolution"]
            else:
                s2Costume["bitmapResolution"] =  1
            scratch2ProjectDict["costumes"].append(s2Costume)

        scratch2ProjectDict["sounds"] = []
        i = 0
        for s3Sound in sprite["sounds"]:
            i += 1
            print s3Sound
            s2Sound = {}
            s2Sound["assetId"] =  s3Sound["assetId"]
            s2Sound["soundName"] =  s3Sound["name"]
            s2Sound["format"] =  s3Sound["format"]
            s2Sound["rate"] =  s3Sound["rate"]
            s2Sound["sampleCount"] =  s3Sound["sampleCount"]
            s2Sound["md5"] =  s3Sound["md5ext"]
            s2Sound["soundID"] = i #TODO this could be wrong
            scratch2ProjectDict["sounds"].append(s2Sound)


        scratch2ProjectDict["objName"] = sprite["name"]
        scratch2ProjectDict["currentCostumeIndex"] = sprite["currentCostume"]
        scratch2ProjectDict["isStage"] = sprite["isStage"]
        if not sprite['isStage']:
            scratch2ProjectDict["scratchX"] = sprite["x"]
            scratch2ProjectDict["scratchY"] = sprite["y"]
            scratch2ProjectDict["scale"] = sprite["size"] / 100.0
            scratch2ProjectDict["direction"] = sprite["direction"]
            scratch2ProjectDict["rotationStyle"] = sprite["rotationStyle"]
            scratch2ProjectDict["isDraggable"] = sprite["draggable"]
            # scratch2ProjectDict["indexInLibrary"] = sprite["indexInLibrary"]
            # scratch2ProjectDict["spriteInfo"] = sprite["spriteInfo"]
            scratch2ProjectDict["visible"] = sprite["visible"]

        return scratch2ProjectDict

    def printLinkedBlockList(self, block, temp_block_dict):
        #TODO: unhardcode this
        # print(block.opcode)
        group = block.opcode.split('_')[0]
        blockcode = "_".join(block.opcode.split('_')[1:])
        blockcode = blockcode[0].upper() + blockcode[1:]
        # print( '"'+block.opcode+"\" : scratch3visitor." + group + ".visit" + blockcode + ",")

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
    "control_create_clone_of_menu" : scratch3visitor.control.visitCreate_clone_of_menu,
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
    "sound_sounds_menu" : scratch3visitor.sound.visitSounds_menu,
    "motion_goto_menu" : scratch3visitor.motion.visitGoto_menu,
    "motion_glideto_menu" : scratch3visitor.motion.visitGlideto_menu,
    "motion_pointtowards_menu" : scratch3visitor.motion.visitPointtowards_menu,

    "data_addtolist" : scratch3visitor.data.visitAddtolist,
    "data_deleteoflist" : scratch3visitor.data.visitDeleteoflist,
    "data_insertatlist" : scratch3visitor.data.visitInsertatlist,
    "data_replaceitemoflist" : scratch3visitor.data.visitReplaceitemoflist,
    "data_itemoflist" : scratch3visitor.data.visitItemoflist,
    "data_itemnumoflist" : scratch3visitor.data.visitItemnumoflist,
    "data_lengthoflist" : scratch3visitor.data.visitLengthoflist,
    "data_listcontainsitem" : scratch3visitor.data.visitListcontainsitem,
    "data_showlist" : scratch3visitor.data.visitShowlist,
    "data_hidelist" : scratch3visitor.data.visitHidelist,

    "looks_costume" : scratch3visitor.looks.visitCostume,
    "looks_backdrops" : scratch3visitor.looks.visitBackdrops,
}
