Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "alice"
>>> if (name == "alice")
SyntaxError: invalid syntax
>>> if (name == "alice"):
	print("hi alice")
	print("hi, alice")

	
hi alice
hi, alice

>>> name = "zain"
>>> if (name =="zain"):
	print ("hello zain")

	
hello zain
>>> zoo_animals = ["zebra","rhino","giraffe","owl","lion","monkey"]
>>> for animal in zoo_animals:
	print(animals)

	
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print(animals)
NameError: name 'animals' is not defined
>>> vegetables = ["carrot","peas","lettuce","tomato"]
>>> for vegetable in vegetables:
	print("I love " + vegetable)

	
I love carrot
I love peas
I love lettuce
I love tomato
>>> 
