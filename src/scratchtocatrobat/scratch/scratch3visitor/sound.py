from scratchtocatrobat.scratch.scratch3 import visitGeneric

def visitPlay(blockcontext):
    block = blockcontext.block
    sound = visitGeneric(blockcontext, 'SOUND_MENU')
    return ['playSound:', sound[0]]

def visitPlayuntildone(blockcontext):
    block = blockcontext.block
    sound = visitGeneric(blockcontext, 'SOUND_MENU')
    return ['playSoundAndWait', sound[0]]

def visitStopallsounds(blockcontext):
    block = blockcontext.block
    return ["stopAllSounds"]

def visitChangeeffectby(blockcontext):
    block = blockcontext.block
    pass #TODO: doesnt exist in scratch2/catroid

def visitSeteffectto(blockcontext):
    block = blockcontext.block
    pass #TODO: doesnt exist in scratch2/catroid

def visitCleareffects(blockcontext):
    block = blockcontext.block
    return ["clearSoundEffects"] #TODO: not in scratch2

def visitChangevolumeby(blockcontext):
    block = blockcontext.block
    volume = visitGeneric(blockcontext, "VOLUME")
    if volume == []:
        volume = block.inputs['VOLUME'][1][1]
    return ["changeVolumeBy:", volume]

def visitSetvolumeto(blockcontext):
    block = blockcontext.block
    volume = visitGeneric(blockcontext, "VOLUME")
    if volume == []:
        volume = block.inputs['VOLUME'][1][1]
    return ["setVolumeTo:", volume]

def visitVolume(blockcontext):
    block = blockcontext.block
    return ["volume"]


def visitSounds_menu(blockcontext):
    block = blockcontext.block
    return block.fields["SOUND_MENU"][0]
