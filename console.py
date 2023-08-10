#!/usr/bin/python3
"""Write a program called console.py that contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Your command interpreter should implement"""

    prompt = '(hbnb) '
    def do_EOF(self, line):
        """to exit the program"""

        return True

    def do_quit(self, line):
        """Quit command to exit the program  
        
        """

        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""

        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if arg == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
        elif arg == "":
            print('** class name missing **')
        else:
            print('** class doesnt exist **')

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        
        array = arg.split()
        if not array:
            print('** class name missing **')
        elif array[0] != "BaseModel":
            print('** class doesnt exist **')
        elif array[1] == "":
            print('** instance id missing **')
        else:
            allinstance = storage.all()
            k = "{}.{}".format(array[0], array[1])
            if k not in allinstance:
                print('** instance id missing **')
            else:
                print(allinstance[k])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""


            

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()


