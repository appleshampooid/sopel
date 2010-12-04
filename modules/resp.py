#!/usr/bin/env python
"""
resp.py - Jenney Response Module
Author: Michael S. Yanovich, http://opensource.osu.edu/
About: http://inamidst.com/phenny/

This module tries to make jenney appear more "affection."
"""

import random, time
greeting = ['Hi', 'Hey', 'Hello', 'Hallo', 'Welcome']
# By increasing the variable 'limit' you are also increasing how annoying jenney will be.
limit = 0.05

def f_whoa(jenney, input):
	randnum = random.random()
	if 0 < randnum < limit:
		respond = ['what?', 'huh?', 'please explain...', 'I\'m confused.']
		randtime = random.uniform(10,45)
		time.sleep(randtime)
		jenney.say(random.choice(respond))
#f_whoa.rule = '(whoa.*)$'
#f_whoa.priority = 'high'

def f_lol(jenney, input):
	randnum = random.random()
	if 0 < randnum < limit:
		respond = ['haha', 'lol', 'rofl']
		randtime = random.uniform(0,9)
		time.sleep(randtime)
		jenney.say(random.choice(respond))
f_lol.rule = '(haha!?|lol!?)$'
f_lol.priority = 'high'

def f_bye(jenney, input):
	respond = ['bye!', 'bye', 'see ya', 'see ya!']
	jenney.say(random.choice(respond))
f_bye.rule = '(g2g!?|bye!?)$'
f_bye.priority = 'high'

def f_argh(jenney, input):
	randnum = random.random()
	if 0 < randnum < limit:
		respond = ['I feel your frustration.', 'I\'m sorry.']
		randtime = random.uniform(10,45)
		time.sleep(randtime)
		jenney.say(random.choice(respond))
#f_argh.rule = '(argh.*)$'
#f_argh.priority = 'high'

def f_heh(jenney, input):
	randnum = random.random()
	if 0 < randnum < limit:
		respond = ['hm']
		randtime = random.uniform(0,7)
		time.sleep(randtime)
		jenney.say(random.choice(respond))
f_heh.rule = '(heh!?)$'
f_heh.priority = 'high'

def f_awesomeness(jenney, input):
	randnum = random.random()
	if 0 < randnum < limit:
		respond = ['cool', 'awesome', 'sweet', 'neat']
		randtime = random.uniform(0,9)
		time.sleep(randtime)
		jenney.say(random.choice(respond))
#f_awesomeness.rule = '(cool!?|awesome!?|sweet!?)$'
#f_awesomeness.priority = 'high'

def f_confusion(jenney, input):
	randnum = random.random()
	if 0 < randnum < limit:
		respond = ['I don\'t get it either.', 'I don\'t get it.', 'Could you elaborate?']
		randtime = random.uniform(10,45)
		time.sleep(randtime)
		jenney.say(random.choice(respond))
#f_confusion.rule = '(huh.*)$'
#f_confusion.priority = 'high'

def f_really(jenney, input):
	randtime = random.uniform(10,45)
	time.sleep(randtime)
	jenney.say(str(input.nick) + ": " + "Yes, really.")
f_really.rule = r'(?i)$nickname\:\s+(really!?)'
f_really.priority = 'high'

def wb(jenney, input):
	jenney.reply("Thank you!")
wb.rule = '(wb).*(jenney|jenney_osu)$'

def bru (jenney, input):
    #if input.sender != "osu_osc":
    #    return
    text = input.group()
    words = { "color" : "colour", "favor" : "favour", "behavior" : "behaviour", "flavor" : "flavour", "favorite" : "favourite", "honor" : "honour", "neighbor" : "neighbour", "rumor" : "rumour", "labor" : "labour"}
    reply = ""
    for k in words:
        if k in text:
            reply += (words[k] + "! ")
    jenney.reply(reply)

#bru.rule = '.*(color|favor|behavior|flavor|honor|labor|rumor|neighbor|favorite).*'

if __name__ == '__main__': 
	print __doc__.strip()
