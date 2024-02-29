# holbertonschool-AirBnB_clone

AirBnB Clone project: The goal of this project is to deploy a server with a simple copy of the AirBnB web app to demonstrate technical grasp of backend development.

The overall Project scope is:

Build a command line interpreter to manipulate data without a visual interface.
A front-end (user interface) and a back-end for the web app: static and dynamic
Data storage via a database or a file storage
An API that bridges the front-end and the data (retrieve, create, delete, update)
Objectives For The BaseModel Class: A Class that defines all common attributes/methods for other classes:
Public instance attributes:
id: string - assign with an uuid when an instance is created

created_at: The current datetime when an instance is created

updated_at: The current datetime when an instance is created, updated every time you change your object

str: should print: [] (<self.id>) <self.dict>

Public instance methods:
save(self): updates the public instance with the current datetime
to_dict(self): returns a dictionary containing all keys/values of dict of the instance. This method will be the first piece of the serialization/deserialization process to JSON format.
Objectives For The Command Line Interpreter:
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

Operating In Interactive Mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

Operating In Non-Interactive Mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

