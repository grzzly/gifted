from moviepy import editor
from gifted import commandline, scripts
from docopt import docopt
import re

class Gif_Create:
	def __init__(self, arguments):
		self.video_name = arguments['<video_name>']
		self.gif_name = arguments['<gif_name>']
		self.start_time = arguments['<start_time>']
		self.end_time = arguments['<end_time>']
		self.resize_factor = float(arguments['--resize'])
		self.directory = arguments['--directory']
		self.crop_x1 = arguments['<left>']
		self.crop_x2 = arguments['<right>']
		self.crop_y1 = arguments['<top>']
		self.crop_y2 = arguments['<bottom>']
		self.new = arguments['new']
		self.crop = arguments['crop']
		
		self.check_input()

	def check_input(self):
		if self.check_time(self.start_time) and self.check_time(self.end_time):
			self.start_time = self.start_time.split(':')
			self.end_time = self.end_time.split(':')
		else:
			print ("Please check your time input.")	
			raise SystemExit

		if self.crop and ((self.crop_x2 and self.crop_y2) != 0):
			if not(self.check_crop()):
				print ("Please check the coordinate input")
				raise SystemExit

	def check_crop(self):
		def check_axis(first, second):
			if int(second) != 0:
				return (int(first) < int(second))
			else: 
				return True

		correct_y = check_axis(self.crop_y1, self.crop_y2)
		correct_x = check_axis(self.crop_x1, self.crop_x2)
		
		if correct_x and correct_y:
			correct_coordinates = True
			return correct_coordinates

	def check_time(self, time):
		correct_time = re.match(r'\d\d:\d\d:\d\d', time)
		return correct_time

	def new_default(self):
		scripts.gif_convert(self.video_name, \
							self.gif_name, \
							self.resize_factor, \
							self.start_time, \
							self.end_time, \
							self.directory)

	def new_crop(self):
		scripts.gif_crop(self.video_name, \
							self.gif_name, \
							self.resize_factor, \
							self.start_time, \
							self.end_time, \
							self.directory, \
							self.crop_x1, \
							self.crop_x2, \
							self.crop_y1, \
							self.crop_y2)

	def main(self):
		if self.new and not(self.crop):
			self.new_default()
		elif self.new and self.crop:
			self.new_crop()

if __name__ == '__main__':
    arguments = docopt(commandline.usage)
    new_gif = Gif_Create(arguments)
    new_gif.main()