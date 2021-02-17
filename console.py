#!/usr/bin/python3
""" importing """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
from models import storage
import json
import shlex

"""
AirBnB Clone
"""


class HBNBCommand(cmd.Cmd):
    """ command interpreter """

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'City': City, 'Place': Place, 'Review': Review,
               'State': State, 'User': User}
    check = ["BaseModel", "Amenity", "City", "Place", "Review",
             "State", "User"]
    prompt = '(hbnb)'

    def emptyline(self):
        """ do nothing """
        pass

    def do_quit(self, line):
        """ quiting by texting quit """
        print("")
        return True

    def do_EOF(self, line):
        """ quiting by textin EOF """
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id """
        if line == "":
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            line = eval(line)()
            line.save()
            print(line.id)

    def do_show(self, line):
        """ Prints the string representation of an
        instance based on the class name and id"""
        str_split = shlex.split(line)
        name = "file.json"
        check = 0
        if len(str_split) == 0:
            print("** class name missing **")
        elif str_split[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(str_split) == 1:
            print("** instance id missing **")
        else:
            data = storage.all()
            key = str_split[0] + "." + str_split[1]
            if key not in data.keys():
                print("** no instance found **")
            else:
                print(data[key])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        str_split = shlex.split(line)
        name = "file.json"
        check = 0
        if len(str_split) == 0:
            print("** class name missing **")
        elif str_split[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(str_split) == 1:
            print("** instance id missing **")
        else:
            data = storage.all()
            key = str_split[0] + "." + str_split[1]
            if key not in data.keys():
                print("** no instance found **")
            else:
                del data[key]
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of all
        instances based or not on the class name. """
        n = line.split()
        obj_list = []
        if len(n) == 0:
            for value in storage.all().values():
                obj_list.append(value.__str__())
            print(obj_list)
        elif n[0] not in self.check:
                print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if n[0] in key:
                    obj_list.append(storage.all()[key].__str__())
            print(obj_list)

    def do_update(self, line):
        n = line.split()
        if len(n) == 0:
            print("** class name missing **")
        elif n[0] not in self.check:
            print("** class doesn't exist **")
        elif len(n) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = ("{}.{}".format(n[0], n[1]))
            if key not in obj:
                print("** no instance found **")
            elif len(n) == 2:
                print("** attribute name missing **")
            elif len(n) == 3:
                print("** value missing **")
            else:
                setattr(obj[key], n[2], n[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
