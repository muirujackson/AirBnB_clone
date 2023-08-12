#!/usr/bin/python3
"""Write a program called console.py that contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
        if arg == "BaseModel" or array[0] in BaseModel.__subclasses__():
            obj = eval(array[0])()
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
        elif array[0] != "BaseModel" or array[0] not in BaseModel.__subclasses__():
            print('** class doesnt exist **')
        elif len(array) < 2:
            print('** instance id missing **')
        else:
            allinstance = storage.all()
            k = "{}.{}".format(array[0], array[1])
            if k not in allinstance:
                print('** no instance found **')
            else:
                print(allinstance[k])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        
        array = arg.split()
        if not array:
            print('** class name missing **')
        elif array[0] != "BaseModel" or array[0] not in BaseModel.__subclasses__():
            print('** class doesnt exist **')
        elif len(array) < 2:
            print('** instance id missing **')
        else:
            allinstance = storage.all()
            k = "{}.{}".format(array[0], array[1])
            if k not in allinstance:
                print('** no instance found **')
            else:
                del allinstance[k]
        storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name."""



        array = arg.split()
        allinstance = storage.all()
        if not array:
            for v in allinstance.values():
                print(str(v))
        else:
            if array[0] != "BaseModel" or array[0] not in BaseModel.__subclasses__():
                print('** class doesnt exist **')
            else:
                for k, v in allinstance.items():
                    if k.startswith(array[0]+ "."):
                        print(str(v))
                    



    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""

        array = arg.split()
        if not array:
            print("** class name missing **")
            return
        if array[0] != "BaseModel" or array[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        if len(array) < 2:
            print("** instance id missing **")
            return
        allinstance = storage.all()
        key = "{}.{}".format(array[0], array[1])
        if key not in allinstance:
            print("** no instance found **")
            return
        if len(array) < 3:
            print("** attribute name missing **")
            return
        if len(array) < 4:
            print("** value missing **")
            return
        if len(array) >4:
            pass
        instance = allinstance[key]
        if (array[3] != "id" and array[3] != "created_at" and array[3] != "updated_at"):
            setattr(instance, array[2], array[3])
            instance.save()




            
if __name__ == '__main__':
    HBNBCommand().cmdloop()



