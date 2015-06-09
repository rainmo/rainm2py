#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animals():
	pass

class Mammals(Animals):
	def left_Foot_Forward(self):
		print ('left foot forward')

	def left_Foot_Back(self):
		print ('left foot back')

	def Right_Foot_Forward(self):
		print ('left foot forward')

	def Right_Foot_Back(self):
		print ('left foot back')

class Giraffes(Mammals):
	def dance(self):
		self.left_Foot_Forward()
		self.left_Foot_Back()
		self.Right_Foot_Forward()
		self.Right_Foot_Back()
		self.left_Foot_Back()
		self.Right_Foot_Back()
		self.Right_Foot_Forward()
		self.left_Foot_Forward()

	

reginald = Giraffes()
reginald.dance()



		
