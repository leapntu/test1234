#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Tue 05 Jul 2016 04:30:49 PM SGT
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui, microphone
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'test1234'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/leapadmin/Desktop/test1234/test1234.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(size=[1280, 720], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Introduction"
IntroductionClock = core.Clock()
introMessage = visual.TextStim(win=win, ori=0, name='introMessage',
    text="Welcome to the LEAP Lab!\nYou will have 5 test to measure your English Ablity.\nFor the test, it will take about 1 and half hour including the break time.\nThe break will be given during the each Test.\nIf you have any questions during the test, \nplease ask to the mannger in the break time or test intro time.\nThen, let's begin! Press the 'SPACEBAR'.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test1intro"
test1introClock = core.Clock()
test1Intro = visual.TextStim(win=win, ori=0, name='test1Intro',
    text="Test1\n\nIn this test, you will see 40 set of written pseudowords.\nThen you need to choose one word which seems more 'Wordlike'.\nWhen you think the Left word is more 'Word-like', then Press 'F'.\nWhen you think the Right word is more 'Word-like', then Press 'J'.\nIf you don't have confidnece about your choice, just believe your gut!\nIf you are ready, Press 'SPACEBAR'.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test1"
test1Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='default text',    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='default text',    font='Arial',
    pos=[0.3, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_16 = visual.TextStim(win=win, ori=0, name='text_16',
    text="Which word is more 'Word-like'?",    font='Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "break1"
break1Clock = core.Clock()
breakmes = visual.TextStim(win=win, ori=0, name='breakmes',
    text="Now, you can take a break as long as you need before continuing.\nPlease, press 'SPACEBAR' when you are ready to continue.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test2intro"
test2introClock = core.Clock()
test2IntroMsg = visual.TextStim(win=win, ori=0, name='test2IntroMsg',
    text="Test2\n\nIn this test, you will hear 40 set of spoken pseudowords.\nEach word will be given by Pressing 'SPACEBAR'.\nThen you need to choose one word which sounds more 'Word-like'.\nWhen you think the First word is more 'Word-like', then Press 'F'.\nWhen you think the Second word is more 'Word-like', then Press 'J'.\nIf you don't have confidnece about your choice, just believe your gut!\nIf you are ready, Press 'SPACEBAR' for listening the first word.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test2word1"
test2word1Clock = core.Clock()
nonwo1 = sound.Sound('A', secs=-1)
nonwo1.setVolume(1)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text="If you are ready to hear next word,\nPress 'SPACEBAR'.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test2word2"
test2word2Clock = core.Clock()
nonwo2 = sound.Sound('A', secs=-1)
nonwo2.setVolume(1)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text="Which word is more 'Word-like'?\nIf you think First one is more 'Word-like', Press 'F'.\nIf you think second one is more 'Word-like', Press 'J'.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "test2break"
test2breakClock = core.Clock()
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text="If you are ready to listen next word,\nPress 'SPACEBAR'!",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "break2"
break2Clock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text="Now, you can take a break as long as you need before continuing.\nPlease, press 'SPACEBAR' when you are ready to continue.\n",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test3intro"
test3introClock = core.Clock()
test3IntroMsg = visual.TextStim(win=win, ori=0, name='test3IntroMsg',
    text="Test3\n\nIn this test, you will hear 34 spoken words.\nThen you need to choose one written word which you heard before.\nIf you don't have confidnece about your choice, just believe your gut!\nIf you are ready, Press 'SPACEBAR' for listening the first word.\n",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test3"
test3Clock = core.Clock()
lrsoundfile = sound.Sound('A', secs=-1)
lrsoundfile.setVolume(1)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='default text',    font='Arial',
    pos=[-0.3, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='default text',    font='Arial',
    pos=[0.3, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='Which word is Correct by your listening?',    font='Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "break3"
break3Clock = core.Clock()
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text="Now, you can take a break as long as you need before continuing.\nPlease, press 'SPACEBAR' when you are ready to continue.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test4intro"
test4introClock = core.Clock()
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text="Test4\n\nIn this test, you will see 36 written words.\nThen you need to speak the word as clear as you can.\nIf you are ready, Press 'SPACEBAR'.\n",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "test4word"
test4wordClock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text="If you are ready to speak, Press 'SPACEBAR'.\nYou should speak the word in 3 seconds.",    font='Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "test4"
test4Clock = core.Clock()
text_15 = visual.TextStim(win=win, ori=0, name='text_15',
    text='Speak loud and clear please!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "endpage"
endpageClock = core.Clock()
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text="You have now come to the end of our first 4 experiment.\nNow, you will have final test.\nPlease wait for a while.\nPress, 'SPACEBAR' for tuning off the program.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Introduction"-------
t = 0
IntroductionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
IntroductionComponents = []
IntroductionComponents.append(introMessage)
IntroductionComponents.append(key_resp_2)
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Introduction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introMessage* updates
    if t >= 0.0 and introMessage.status == NOT_STARTED:
        # keep track of start time/frame for later
        introMessage.tStart = t  # underestimates by a little under one frame
        introMessage.frameNStart = frameN  # exact frame index
        introMessage.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "test1intro"-------
t = 0
test1introClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
test1introComponents = []
test1introComponents.append(test1Intro)
test1introComponents.append(key_resp_3)
for thisComponent in test1introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "test1intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = test1introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test1Intro* updates
    if t >= 0.0 and test1Intro.status == NOT_STARTED:
        # keep track of start time/frame for later
        test1Intro.tStart = t  # underestimates by a little under one frame
        test1Intro.frameNStart = frameN  # exact frame index
        test1Intro.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test1introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "test1intro"-------
for thisComponent in test1introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test1intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "test1"-------
    t = 0
    test1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text.setText(word1)
    text_2.setText(word2)
    key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_4.status = NOT_STARTED
    # keep track of which components have finished
    test1Components = []
    test1Components.append(text)
    test1Components.append(text_2)
    test1Components.append(key_resp_4)
    test1Components.append(text_16)
    for thisComponent in test1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = test1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t  # underestimates by a little under one frame
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
                # was this 'correct'?
                if (key_resp_4.keys == str(corrans)) or (key_resp_4.keys == corrans):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test1"-------
    for thisComponent in test1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
       key_resp_4.keys=None
       # was no response the correct answer?!
       if str(corrans).lower() == 'none': key_resp_4.corr = 1  # correct non-response
       else: key_resp_4.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    trials.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "test1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials'


#------Prepare to start Routine "break1"-------
t = 0
break1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
break1Components = []
break1Components.append(breakmes)
break1Components.append(key_resp_5)
for thisComponent in break1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "break1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = break1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *breakmes* updates
    if t >= 0.0 and breakmes.status == NOT_STARTED:
        # keep track of start time/frame for later
        breakmes.tStart = t  # underestimates by a little under one frame
        breakmes.frameNStart = frameN  # exact frame index
        breakmes.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "break1"-------
for thisComponent in break1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "break1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "test2intro"-------
t = 0
test2introClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
test2introComponents = []
test2introComponents.append(test2IntroMsg)
test2introComponents.append(key_resp_6)
for thisComponent in test2introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "test2intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = test2introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test2IntroMsg* updates
    if t >= 0.0 and test2IntroMsg.status == NOT_STARTED:
        # keep track of start time/frame for later
        test2IntroMsg.tStart = t  # underestimates by a little under one frame
        test2IntroMsg.frameNStart = frameN  # exact frame index
        test2IntroMsg.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test2introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "test2intro"-------
for thisComponent in test2introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test2intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "test2word1"-------
    t = 0
    test2word1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    nonwo1.setSound(nonword1, secs=-1)
    key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_7.status = NOT_STARTED
    # keep track of which components have finished
    test2word1Components = []
    test2word1Components.append(nonwo1)
    test2word1Components.append(key_resp_7)
    test2word1Components.append(text_3)
    for thisComponent in test2word1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test2word1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = test2word1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop nonwo1
        if t >= 0.0 and nonwo1.status == NOT_STARTED:
            # keep track of start time/frame for later
            nonwo1.tStart = t  # underestimates by a little under one frame
            nonwo1.frameNStart = frameN  # exact frame index
            nonwo1.play()  # start the sound (it finishes automatically)
        
        # *key_resp_7* updates
        if t >= 0.0 and key_resp_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_7.tStart = t  # underestimates by a little under one frame
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test2word1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test2word1"-------
    for thisComponent in test2word1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nonwo1.stop() #ensure sound has stopped at end of routine
    # the Routine "test2word1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "test2word2"-------
    t = 0
    test2word2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    nonwo2.setSound(nonword2, secs=-1)
    key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_8.status = NOT_STARTED
    # keep track of which components have finished
    test2word2Components = []
    test2word2Components.append(nonwo2)
    test2word2Components.append(key_resp_8)
    test2word2Components.append(text_4)
    for thisComponent in test2word2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test2word2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = test2word2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop nonwo2
        if t >= 0.0 and nonwo2.status == NOT_STARTED:
            # keep track of start time/frame for later
            nonwo2.tStart = t  # underestimates by a little under one frame
            nonwo2.frameNStart = frameN  # exact frame index
            nonwo2.play()  # start the sound (it finishes automatically)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t  # underestimates by a little under one frame
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                key_resp_8.rt = key_resp_8.clock.getTime()
                # was this 'correct'?
                if (key_resp_8.keys == str(corrans)) or (key_resp_8.keys == corrans):
                    key_resp_8.corr = 1
                else:
                    key_resp_8.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test2word2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test2word2"-------
    for thisComponent in test2word2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nonwo2.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
       key_resp_8.keys=None
       # was no response the correct answer?!
       if str(corrans).lower() == 'none': key_resp_8.corr = 1  # correct non-response
       else: key_resp_8.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_8.keys',key_resp_8.keys)
    trials_2.addData('key_resp_8.corr', key_resp_8.corr)
    if key_resp_8.keys != None:  # we had a response
        trials_2.addData('key_resp_8.rt', key_resp_8.rt)
    # the Routine "test2word2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "test2break"-------
    t = 0
    test2breakClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_16 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_16.status = NOT_STARTED
    # keep track of which components have finished
    test2breakComponents = []
    test2breakComponents.append(text_14)
    test2breakComponents.append(key_resp_16)
    for thisComponent in test2breakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test2break"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = test2breakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        
        # *key_resp_16* updates
        if t >= 0.0 and key_resp_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_16.tStart = t  # underestimates by a little under one frame
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_16.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test2breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test2break"-------
    for thisComponent in test2breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "test2break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_2'


#------Prepare to start Routine "break2"-------
t = 0
break2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_9.status = NOT_STARTED
# keep track of which components have finished
break2Components = []
break2Components.append(text_5)
break2Components.append(key_resp_9)
for thisComponent in break2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "break2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = break2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # underestimates by a little under one frame
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "break2"-------
for thisComponent in break2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "break2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "test3intro"-------
t = 0
test3introClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_10.status = NOT_STARTED
# keep track of which components have finished
test3introComponents = []
test3introComponents.append(test3IntroMsg)
test3introComponents.append(key_resp_10)
for thisComponent in test3introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "test3intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = test3introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test3IntroMsg* updates
    if t >= 0.0 and test3IntroMsg.status == NOT_STARTED:
        # keep track of start time/frame for later
        test3IntroMsg.tStart = t  # underestimates by a little under one frame
        test3IntroMsg.frameNStart = frameN  # exact frame index
        test3IntroMsg.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # underestimates by a little under one frame
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test3introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "test3intro"-------
for thisComponent in test3introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test3intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test3.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "test3"-------
    t = 0
    test3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    lrsoundfile.setSound(lrsound, secs=-1)
    text_6.setText(lrword1)
    text_7.setText(lrword2)
    key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_11.status = NOT_STARTED
    # keep track of which components have finished
    test3Components = []
    test3Components.append(lrsoundfile)
    test3Components.append(text_6)
    test3Components.append(text_7)
    test3Components.append(key_resp_11)
    test3Components.append(text_8)
    for thisComponent in test3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = test3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop lrsoundfile
        if t >= 0.0 and lrsoundfile.status == NOT_STARTED:
            # keep track of start time/frame for later
            lrsoundfile.tStart = t  # underestimates by a little under one frame
            lrsoundfile.frameNStart = frameN  # exact frame index
            lrsoundfile.play()  # start the sound (it finishes automatically)
        
        # *text_6* updates
        if t >= 0.5 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # *text_7* updates
        if t >= 0.5 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # underestimates by a little under one frame
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        
        # *key_resp_11* updates
        if t >= 0.0 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t  # underestimates by a little under one frame
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_11.keys = theseKeys[-1]  # just the last key pressed
                key_resp_11.rt = key_resp_11.clock.getTime()
                # was this 'correct'?
                if (key_resp_11.keys == str(corrans)) or (key_resp_11.keys == corrans):
                    key_resp_11.corr = 1
                else:
                    key_resp_11.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_8* updates
        if t >= 0.5 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test3"-------
    for thisComponent in test3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    lrsoundfile.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
       key_resp_11.keys=None
       # was no response the correct answer?!
       if str(corrans).lower() == 'none': key_resp_11.corr = 1  # correct non-response
       else: key_resp_11.corr = 0  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('key_resp_11.keys',key_resp_11.keys)
    trials_3.addData('key_resp_11.corr', key_resp_11.corr)
    if key_resp_11.keys != None:  # we had a response
        trials_3.addData('key_resp_11.rt', key_resp_11.rt)
    # the Routine "test3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_3'


#------Prepare to start Routine "break3"-------
t = 0
break3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_12.status = NOT_STARTED
# keep track of which components have finished
break3Components = []
break3Components.append(text_9)
break3Components.append(key_resp_12)
for thisComponent in break3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "break3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = break3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # underestimates by a little under one frame
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # underestimates by a little under one frame
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "break3"-------
for thisComponent in break3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "break3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "test4intro"-------
t = 0
test4introClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_13.status = NOT_STARTED
# keep track of which components have finished
test4introComponents = []
test4introComponents.append(text_10)
test4introComponents.append(key_resp_13)
for thisComponent in test4introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "test4intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = test4introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # underestimates by a little under one frame
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test4introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "test4intro"-------
for thisComponent in test4introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test4intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test4.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    #------Prepare to start Routine "test4word"-------
    t = 0
    test4wordClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text_11.setText(recword)
    key_resp_14 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_14.status = NOT_STARTED
    # keep track of which components have finished
    test4wordComponents = []
    test4wordComponents.append(text_11)
    test4wordComponents.append(text_12)
    test4wordComponents.append(key_resp_14)
    for thisComponent in test4wordComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test4word"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = test4wordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t  # underestimates by a little under one frame
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        
        # *key_resp_14* updates
        if t >= 0.0 and key_resp_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_14.tStart = t  # underestimates by a little under one frame
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_14.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test4wordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test4word"-------
    for thisComponent in test4wordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "test4word" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "test4"-------
    t = 0
    test4Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    mic_1 = microphone.AdvAudioCapture(name='mic_1', saveDir=wavDirName, stereo=False)
    # keep track of which components have finished
    test4Components = []
    test4Components.append(text_15)
    test4Components.append(mic_1)
    for thisComponent in test4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "test4"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t  # underestimates by a little under one frame
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        if text_15.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_15.setAutoDraw(False)
        
        # *mic_1* updates
        if t >= 0.0 and mic_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            mic_1.tStart = t  # underestimates by a little under one frame
            mic_1.frameNStart = frameN  # exact frame index
            mic_1.status = STARTED
            mic_1.record(sec=3, block=False)  # start the recording thread
        
        if mic_1.status == STARTED and not mic_1.recorder.running:
            mic_1.status = FINISHED
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "test4"-------
    for thisComponent in test4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # mic_1 stop & responses
    mic_1.stop()  # sometimes helpful
    if not mic_1.savedFile:
        mic_1.savedFile = None
    # store data for trials_4 (TrialHandler)
    trials_4.addData('mic_1.filename', mic_1.savedFile)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


#------Prepare to start Routine "endpage"-------
t = 0
endpageClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_15.status = NOT_STARTED
# keep track of which components have finished
endpageComponents = []
endpageComponents.append(text_13)
endpageComponents.append(key_resp_15)
for thisComponent in endpageComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "endpage"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endpageClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t  # underestimates by a little under one frame
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    
    # *key_resp_15* updates
    if t >= 0.0 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t  # underestimates by a little under one frame
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endpageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "endpage"-------
for thisComponent in endpageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "endpage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
