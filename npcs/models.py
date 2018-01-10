# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class TrackedModel(models.Model):
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Item(models.Model):
    ITEM_TYPE_CHOICES = (
        ('npc', 'NPC'),
        ('level', 'Level'),
        ('aspect', 'Aspect'),
        ('skill', 'Skill'),
        ('approach', 'Approach'),
        ('stunt', 'Stunt'),
    )
    type = models.CharField(max_length=15)

class NPC(TrackedModel): 
    item = models.OneToOneField(Item)
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.npc_name


class Level(TrackedModel): 
    LEVEL_CHOICES = (
    	('filler1', 'Filler - Average (+1)'),
    	('filler2', 'Filler - Fair (+2)'),
    	('filler3', 'Filler - Good (+3)'),
    	('hitter', 'Hitter'),
    	('threat', 'Threat'),
    	('boss', 'Boss'),
    	('vlm', 'Very Large Monster')
    )
    item = models.OneToOneField(Item)
    name = models.CharField(max_length=50)

class Aspect(TrackedModel): 
    ASPECT_TYPE_CHOICES = (
    	('HC', 'High Concept'),
    	('TR', 'Trouble'),
    	('OT', 'Other')
    )
    item = models.OneToOneField(Item)
    text = models.CharField(max_length=75)
    type = models.CharField(max_length=2, choices=ASPECT_TYPE_CHOICES)
    description = models.CharField(max_length=250)

    def __str__(self):
    	return self.aspect_text

class Skill(TrackedModel):
    SKILL_TYPE_CHOICES = (
        ('skill', 'Skill'),
        ('approach', 'Approach'),
    )
    item = models.OneToOneField(Item)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15, choices=SKILL_TYPE_CHOICES)

    def __str__(self):
    	return self.skill_name

class Stunt(TrackedModel):
    item = models.OneToOneField(Item)
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=500)

    def __str__(self):
    	return self.stunt_name

