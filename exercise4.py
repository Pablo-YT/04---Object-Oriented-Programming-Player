#Create a class called Player.
#Every player should have three attributes: gold_coins, health_points, and lives.
#lives should start at 5.
#gold_coins should start at 0.
#health_points should start at 10.
#Define an __str__() instance method.
#Your class should have an instance method called level_up that increases lives by one.
#Your class should have an instance method called collect_treasure that increases gold_coins by one. 
#If gold_coins is a multiple of ten (eg, 10, 20, 30, and so on) then the collect_treasure method should run the level_up method.
#Your class should have an instance method called do_battle that accepts one damage argument and subtracts it from the player's health_points. 
#If health_points falls below one, subtract one from lives and reset health_points to ten. If you have run out of lives, this method should run another method called restart (see below).
#The restart instance method should set all attributes back to their starting values (5, 0, and 10).



class Player:
	"""docstring for Player"""
	def __init__(self, name, health_points = 10, lives = 5, gold_coins = 0):
		self.name = name
		self.health_points = health_points
		self.lives = lives
		self.gold_coins = gold_coins



	def __str__(self):
		return "{} has {} health points, {} lives and {} gold coins remaining.".format(self.name, self.health_points, self.lives, self.gold_coins)



	
		
	def level_up(self):
		if self.gold_coins % 10 == 0:
			self.lives += 1
			print("You just leveled up. You now have {} lives.".format(self.lives))




		
	def collect_treasure(self):
		for i in range(1,11):
			#self.level_up()
			self.gold_coins += 1
			print("You have collected treasure :). You now have {} gold coin(s).".format(self.gold_coins))


	
		
	def do_battle(self):
		self.health_points -= 1
		print("You have are now FIGHTING FOR YOUR LIFE!!! and trip on a rock :(.\nYou lost health! Your health points are now at: {}".format(self.health_points))


	def health_restart(self):
		if self.health_points < 1:
			self.lives -= 1
			self.health_points = 10
			print("You have run out of health :-[. You now have {} lives. Your health points have been reset to {}".format(self.lives, self.health_points))
		
		if self.lives < 1:
			self.restart()
			print("Game Over! You have NO MORE LIVES! But you have been granted another chance!!! DON'T LOSE THIS TIME MWAH WAA HAA.\nHealth points: {} \nLives: {} \nGold Coins: {}".format(self.health_points, self.lives, self.gold_coins))



	def restart(self):
		self.lives = 5
		self.health_points = 10
		self.gold_coins = 0




Player1 = Player("Josh")
print(Player1)

Player1.collect_treasure()
Player1.level_up()
Player1.do_battle()
Player1.health_restart()