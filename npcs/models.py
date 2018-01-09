# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class NPC(models.Model): #######################################################
	name = models.CharField(max_length=75)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.npc_name

class NPC_vote(models.Model):
	npc = models.ForeignKey(NPC)

class Level(models.Model): #####################################################
	LEVEL_CHOICES = (
		('filler1', 'Filler - Average (+1)'),
		('filler2', 'Filler - Fair (+2)'),
		('filler3', 'Filler - Good (+3)'),
		('hitter', 'Hitter'),
		('threat', 'Threat'),
		('boss', 'Boss'),
		('vlm', 'Very Large Monster')
	)
	name = models.CharField(max_length=50)

class Level_vote(models.Model):
	level = models.ForeignKey(Level)

class Aspect(models.Model): ####################################################
	ASPECT_TYPE_CHOICES = (
		('HC', 'High Concept'),
		('TR', 'Trouble'),
		('OT', 'Other')
	)
	text = models.CharField(max_length=75)
	type = models.CharField(max_length=2, choices=ASPECT_TYPE_CHOICES)
        description = models.CharField(max_length=250)

	def __str__(self):
		return self.aspect_text

class Aspect_vote(models.Model):
	aspect = models.ForeignKey(Aspect)

class Skill(model.Models): #####################################################
	SKILL_TYPE_CHOICES = (
		('skill', 'Skill'),
		('approach', 'Approach'),
		('custom', 'Custom')
	)
	name = CharField(max_length=50)
	type = models.CharField(max_length=10, choices=SKILL_TYPE_CHOICES)

class Skill_vote(models.Model):
	skill = models.ForeignKey(Skill)

class Stunt(model.Models): #####################################################
	name = models.CharField(max_length=75)
	description = models.CharField(max_length=500)

	def __str__(self):
		return self.stunt_name

class Stunt_vote(models.Model):
	stunt = models.ForeignKey(Stunt)
