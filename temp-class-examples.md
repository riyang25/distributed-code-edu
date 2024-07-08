# Bad
```py
first_names = ["Brian", "Donald", "Ada"]
last_names =  ["Kernighan", "Knuth", "Lovelace"]
ages = [82, 86, 209]
professions = ["Computer Scientist", "Computer Scientist", "Mathematician"]

# To obtain all information for Mr. Kernighan, we can do the following:
brian_first_name = first_names[0]
brian_last_name = last_names[0]
brian_age = ages[0]
brian_profession = professions[0]
```
# Better
```py
class Person:
	def __init__(self, first_name, last_name, age, profession):
		self.full_name = first_name + " " + last_name
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.profession = profession

# To create a new Person.
new_person = Person("Donald", "Knuth", 86, "Computer Scientist")

# To use the Person.
new_person.full_name # This has a value "Donald Knuth".
new_person.age # This has a value 86.

# As you can see, this is much easier to use than a bunch of lists.
```
# Method
```py
class Person:
...

	def say_hello(self, current_year):
		print("Hello, my name is " + self.full_name + ". I am a " + self.profession + " and I was born in the year " + str(current_year - self.age) + ".")

# Now to create a Person.
new_person = Person("Ada", "Lovelace", 209, "Mathematician")

new_person.sey_hello(2024)
# The line above calls the function we defined in the class Person. We give it the argument 2024 which is assigned to the parameter current_year.
# Output: "Hello, my name is Ada Lovelace. I am a Mathematician and I was born in the year 1815."
```
