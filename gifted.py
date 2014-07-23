from moviepy import editor
from gifted import commandline, scripts
from docopt import docopt

class Gif_Create:
	def __init__(self, arguments):
		self.video_name = arguments['<video_name>']
		self.gif_name = arguments['<gif_name>']
		self.start_time = arguments['<start_time>']
		self.end_time = arguments['<end_time>']
		self.resize_factor = float(arguments['--resize'])
		self.directory = arguments['--directory']

		if self.start_time.count(':') > 2 or self.end_time.count(':') > 2:
			print("Please enter the times in the correct time format.")
			raise SystemExit

		self.start_time = self.start_time.split(':')
		self.end_time = self.end_time.split(':')

	def main(self):
		scripts.gif_convert(self.video_name, \
							self.gif_name, \
							self.resize_factor, \
							self.start_time, \
							self.end_time, \
							self.directory)

if __name__ == '__main__':
    arguments = docopt(commandline.usage)
    print arguments
    new_gif = Gif_Create(arguments)
    new_gif.main()