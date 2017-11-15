class Animal1(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!! " + ' ' + self.name +' '+ " is eating "+ food)
	def description(self):
		print(self.name + ' is '+(str(self.age)) +" years old and loves the color " +self.favorite_color)
	def make_sound(self):
		print(self.sound + self.sound + self.sound)

cat = Animal1("meow","kitty",4,"blue")
cat.eat ("fish")
cat.description()
cat.make_sound()

class person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self,fav_breakfast):
		print('Yammyyy! ' + ' ' +self.name+ ' '+ ' loves' +fav_breakfast) 
	def go(self,place):
		print(self.name + ' goes to ' + place )
vivi = person('vivi',15,'jaffa','female')
vivi.eat('pancakes')
vivi.go('meet hub')
