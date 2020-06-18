#-----------------------------------------------------------------------------#

### MUD IMPORTS ###

from mud_rooms import Room, Command

#-----------------------------------------------------------------------------#

###

class MudWorld():

	def __init__(self, *args, **kwargs):

		self.commands = [] # i.e. Korero, Panui
		self.starting_room = self.build_starting_room()
	
	### BUILD ###

	def build_starting_room(self):

		note = 'Na te Kore, te Po,\nKi te Whai-Ao,\nKi te Ao-Mārama,\nTihei mauri-ora!'
		
		d =  '\n' * 2
		d += '\nKo tenei te Kore, te Po. Te po nui, te po roa, te po tangotango.'
		d += '\nKaore te marama, kaore nga atua, kaore te ao.'
		d += '\nEngari... hei aha tera? He huanui, he karanga, he tangi pea?'
		d += '\n' * 5

		commands = {'whakarongo':Command('whakarongo', 'text',
									result='\n\n"Ko wai koe?"\n\n'),
					'ko':Command('ko', 'process',
									result={}),
					}



		room = Room(None, None, 
				title='Na te Kore, te Po.',
				description=d,
				commands=commands)


		return room




#-----------------------------------------------------------------------------#