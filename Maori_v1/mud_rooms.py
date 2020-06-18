#-----------------------------------------------------------------------------#

### IMPORTS ###


#-----------------------------------------------------------------------------#

### COMMAND CLASS ###

class Command():

	def __init__(self, command, action, *args, result=None, **kwargs):

		self.command = command
		self.action = action # i.e. text or move or ?multitext?
		self.result = result # i.e. text message sent to player or new Room()

	def process_command(self, mud, id, player, data):

		if self.action == 'text':
			mud.send_message(id, self.result)
		elif self.action == 'move':
			player.move_room(self.result) # exit direction, Room()
		elif self.action == 'text&move':
			mud.send_message(id, self.result[0])
			player.move_room(self.result[1])

#-----------------------------------------------------------------------------#

### ROOM CLASS ###

class Room():

	def __init__(self, x, y, *args, 
					title='Enter Title', 
					description='Enter Description',
					commands={},**kwargs):

		self.x = x
		self.y = y
		
		self.title = title
		self.description = description

		self.exits = {}

		self.commands = commands

		self.players = []

	def describe(self, player):

		line = '#' + '-'*77 + '#'
		title = self.title
		
		description = self.description
		# additional descriptions can be added if player has 'unlocked' them
		
		exits = list(self.exits.keys())
		# additional exits can be added if player has 'unlocked' them
		if exits == []:
			exits = 'There are no known exits'
		else:
			exits = (',').join(exits)

		return '%s\n\t%s\n\n%s\n\n%sExits: %s\n>>>' % (line, 
												title, description, line, exits)

	def check_command(self, player, message):

		pass

#-----------------------------------------------------------------------------#