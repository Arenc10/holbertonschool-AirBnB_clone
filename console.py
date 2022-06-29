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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
