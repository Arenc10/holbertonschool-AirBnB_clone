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
import re


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

    def default(self, args):
        if re.search(r'^\w+\.{1,1}\w+\({1,1}\)$', args):
            arr = args.split(".")
            s = arr[1] + " " + arr[0]
            s1 = s.replace("(", "").replace(")", "")
            arr1 = s1.split(" ")
            if arr1[0] == "count":
                count = 0
                all_objects = storage.all()
                for key in all_objects:
                    tokens = key.split(".")
                    if arr1[1] == tokens[0]:
                        count = count + 1
                print(count)
            else:
                self.onecmd(s1)
        elif re.search(r'^\w+\.{1,1}\w+\({1,1}[a-zA-Z0-9-]+\)$', args):
            s = args.replace("(", ".").replace(")", "")
            s1 = s.split(".")
            s2 = s1[1] + " " + s1[0] + " " + s1[2]
            self.onecmd(s2)
        elif re.search((r'^\w+\.{1,1}\w+'
                        r'\({1,1}[a-zA-Z0-9-_]+'
                        r',{1,1}\s?[a-zA-Z0-9-_]+\)$'), args):
            s = args.replace("(", ".").replace(")", "")\
                .replace(",", ".").replace(" ", "")
            s1 = s.split(".")
            s2 = s1[1] + " " + s1[0] + " " + s1[2] + " " + s1[3]
            self.onecmd(s2)
        elif re.search((r'^\w+\.{1,1}\w+\({1,1}'
                        r'[a-zA-Z0-9-_]+,{1,1}\s?[a-zA-Z0-9-_]+'
                        r',{1,1}\s?[a-zA-Z0-9-_]+\)$'), args):
            s = args.replace("(", ".").replace(")", "")\
                .replace(",", ".").replace(" ", "")
            s1 = s.split(".")
            s2 = s1[1] + " " + s1[0] + " " + s1[2] + " " + s1[3] + " " + s1[4]
            self.onecmd(s2)

        return False

    def do_quit(self, arg):
        """Quit command to exit the program

        """

        return True

    def do_EOF(self, arg):
        """Quit command to exit the program

        """

        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Create instance of a class

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
        """Shows a string representation of an instance based on class name

        """
        arr = args.split()
        if len(arr) == 0:
            print("** class name missing **")
        elif arr[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            temp_key = arr[0] + "." + arr[1]
            temp_obj = storage.all()
            if temp_key not in temp_obj:
                print("** no instance found **")
            else:
                print(temp_obj[temp_key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id

        """
        arr = args.split()
        if len(arr) == 0:
            print("** class name missing **")
        elif arr[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            temp_key = arr[0] + "." + arr[1]
            temp_obj = storage.all()
            if temp_key not in temp_obj:
                print("** no instance found **")
            else:
                del temp_obj[temp_key]
                storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances

        """
        all_objects = storage.all()

        if len(args) == 0:
            object_list = [str(value) for value in all_objects.values()]
        elif args in HBNBCommand.cmd_classes:
            object_list = [str(value) for key, value in all_objects.items()
                           if args in key]
        else:
            print("** class doesn't exist **")
            return False

        print(object_list)

    def do_update(self, args):
        """Updated an instance based on the class name and id

        """
        tokens = args.split()
        if len(tokens) < 1:
            print("** class name missing **")
        elif tokens[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        elif len(tokens) < 3:
            print("** attribute name missing **")
        elif len(tokens) < 4:
            print("** value missing **")
        else:
            temp_key = tokens[0] + "." + tokens[1]
            temp_obj = storage.all()
            if temp_key not in temp_obj:
                print("** no instance found **")
            else:
                setattr(temp_obj[temp_key], tokens[2], tokens[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
