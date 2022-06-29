#!/usr/bin/python3
"""Console program
"""
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the interpreter
    """
    prompt = '(hbnb) '
    cmd_classes = {
            "BaseModel": BaseModel,
            "City": City,
            "State": State,
            "User": User,
            "Review": Review,
            "Amenity": Amenity,
            "Place": Place
            }

    def do_quit(self, arg):
        'Quit command to exit the program'

        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'

        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """create instance of BaseModel

        """
        if args is None or args == "":
            print("** class name missing **")
        elif args not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        else:
            new_object = HBNBCommand.cmd_classes[args]()
            new_object.save()
            print(new_object.id)
            storage.save()

    def do_show(self, args):
        arr = args.split()
        if len(arr) == 0:
            print("** class name missing **")
        elif arr[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        elif HBNBCommand.cmd_classes[arr[0]].id != arr[1]:
            print("** no instance found **")
        else:
            show_obj = HBNBCommand.cmd_classes[arr[0]]()
            print(show_obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
