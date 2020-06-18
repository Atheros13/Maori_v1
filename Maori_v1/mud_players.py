#-----------------------------------------------------------------------------#

### IMPORTS ###


#-----------------------------------------------------------------------------#

### BASIC NEW PLAYER CLASS ###

class Player():

	def __init__(self, *args, id=None, room=None, **kwargs):

		self.id = id
		self.room = room

		self.name = None

		self.equipment = [] # what they are wearing/using/wielding
		self.inventory = [] # what they have i.e. in a backpack

	def move_room(self, mud, exit_text, new_room):

		self.room.players.remove(self)
		mud.send_message(self.id, exit_text)
		self.room = new_room
		mud.send_message(self.id, self.room.describe())

		

#-----------------------------------------------------------------------------#