#-----------------------------------------------------------------------------#

### PYTHON IMPORTS ###

import time

#-----------------------------------------------------------------------------#

### MUD IMPORTS ###

from mud_server import MudServer

from mud_world import MudWorld
from mud_players import Player

#-----------------------------------------------------------------------------#

### ENGINE CLASS ###

class MudEngine():

	mud = MudServer()

	def __init__(self, *args, **kwargs):

		self.world = MudWorld()
		self.players = {} # id:Player()

		self.run()

	## BUILD ##



	## RUN ##

	def run(self, *args, **kwargs):

		while True:

			# pause for 1/5 second on each loop and 
			# call to update() to get new information
			time.sleep(0.2)
			self.mud.update()

			# check newly connected players
			for id in self.mud.get_new_players():

				# creates a Player() object, assigns it to the id
				# and puts the player in the starting Room()
				player = Player(id=id, room=self.world.starting_room)
				self.players[id] = player
				# sends a message to player describing that room
				self.mud.send_message(id, player.room.describe(player=player))

			# check disconnected players (this could be expanded for linkdead)
			for id in self.mud.get_disconnected_players():

				if id not in self.players:
					continue

				for pid, player in self.players.items():
					self.mud.send_message(pid, 'Kei te haere atu a %s' % self.players[id].name)

				del(self.players[id])

			#
			for id, data in self.mud.get_commands():

				self.process_data(id, data)

	### PROCESS ###

	def process_data(self, id, data):

		# 
		player = self.players[id]
		room = self.player.room
		command = data.split()[0].lower()

		# test 'room' commands i.e.
		if command in room.commands:

			room.commands[command].process_command(self, id, player, data)

		elif command in room.exits:

			pass

		elif command == 'haere':

			pass # same as above

		elif command in self.world.commands:

			pass

		# test 'general' commands i.e. panui, korero


	def runextra(self):

	    # go through any new commands sent from players
	    for id, command, params in mud.get_commands():

	        # if for any reason the player isn't in the player map, skip them and
	        # move on to the next one
	        if id not in players:
	            continue

	        # if the player hasn't given their name yet, use this first command as
	        # their name and move them to the starting room.
	        if players[id]["name"] is None:

	            players[id]["name"] = command
	            players[id]["room"] = "Tavern"

	            # go through all the players in the game
	            for pid, pl in players.items():
	                # send each player a message to tell them about the new player
	                mud.send_message(pid, "{} entered the game".format(
	                                                        players[id]["name"]))

	            # send the new player a welcome message
	            mud.send_message(id, "Welcome to the game, {}. ".format(
	                                                           players[id]["name"])
	                             + "Type 'help' for a list of commands. Have fun!")

	            # send the new player the description of their current room
	            mud.send_message(id, rooms[players[id]["room"]]["description"])

	        # each of the possible commands is handled below. Try adding new
	        # commands to the game!

	        # 'help' command
	        elif command == "help":

	            # send the player back the list of possible commands
	            mud.send_message(id, "Commands:")
	            mud.send_message(id, "  say <message>  - Says something out loud, "
	                                 + "e.g. 'say Hello'")
	            mud.send_message(id, "  look           - Examines the "
	                                 + "surroundings, e.g. 'look'")
	            mud.send_message(id, "  go <exit>      - Moves through the exit "
	                                 + "specified, e.g. 'go outside'")

	        # 'say' command
	        elif command == "say":

	            # go through every player in the game
	            for pid, pl in players.items():
	                # if they're in the same room as the player
	                if players[pid]["room"] == players[id]["room"]:
	                    # send them a message telling them what the player said
	                    mud.send_message(pid, "{} says: {}".format(
	                                                players[id]["name"], params))

	        # 'look' command
	        elif command == "look":

	            # store the player's current room
	            rm = rooms[players[id]["room"]]

	            # send the player back the description of their current room
	            mud.send_message(id, rm["description"])

	            playershere = []
	            # go through every player in the game
	            for pid, pl in players.items():
	                # if they're in the same room as the player
	                if players[pid]["room"] == players[id]["room"]:
	                    # ... and they have a name to be shown
	                    if players[pid]["name"] is not None:
	                        # add their name to the list
	                        playershere.append(players[pid]["name"])

	            # send player a message containing the list of players in the room
	            mud.send_message(id, "Players here: {}".format(
	                                                    ", ".join(playershere)))

	            # send player a message containing the list of exits from this room
	            mud.send_message(id, "Exits are: {}".format(
	                                                    ", ".join(rm["exits"])))

	        # 'go' command
	        elif command == "go":

	            # store the exit name
	            ex = params.lower()

	            # store the player's current room
	            rm = rooms[players[id]["room"]]

	            # if the specified exit is found in the room's exits list
	            if ex in rm["exits"]:

	                # go through all the players in the game
	                for pid, pl in players.items():
	                    # if player is in the same room and isn't the player
	                    # sending the command
	                    if players[pid]["room"] == players[id]["room"] \
	                            and pid != id:
	                        # send them a message telling them that the player
	                        # left the room
	                        mud.send_message(pid, "{} left via exit '{}'".format(
	                                                      players[id]["name"], ex))

	                # update the player's current room to the one the exit leads to
	                players[id]["room"] = rm["exits"][ex]
	                rm = rooms[players[id]["room"]]

	                # go through all the players in the game
	                for pid, pl in players.items():
	                    # if player is in the same (new) room and isn't the player
	                    # sending the command
	                    if players[pid]["room"] == players[id]["room"] \
	                            and pid != id:
	                        # send them a message telling them that the player
	                        # entered the room
	                        mud.send_message(pid,
	                                         "{} arrived via exit '{}'".format(
	                                                      players[id]["name"], ex))

	                # send the player a message telling them where they are now
	                mud.send_message(id, "You arrive at '{}'".format(
	                                                          players[id]["room"]))

	            # the specified exit wasn't found in the current room
	            else:
	                # send back an 'unknown exit' message
	                mud.send_message(id, "Unknown exit '{}'".format(ex))

	        # some other, unrecognised command
	        else:
	            # send back an 'unknown command' message
	            mud.send_message(id, "Unknown command '{}'".format(command))

#-----------------------------------------------------------------------------#

### ENGINE ###

if __name__ == '__main__':

	MudEngine()

#-----------------------------------------------------------------------------#