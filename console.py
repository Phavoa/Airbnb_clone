#!/usr/bin/env python3
"""
The main console for airbnb
"""
from models.base_model import BaseModel


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        The command to quit
        """
        return True

    def do_EOF(self, arg):
        """
        You've reached end of line
        """
        return True

    def do_create(self, arg):
        """
        Creates an instance of BaseModel
        """
        data = []
        data = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif "BaseModel" not in data or len(data) != 3:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            print("{}".format(my_model.id))

    def do_show(self, arg):
        """
        Prints the string form of an instance based on the class name and id
        """
        data = arg.split(" ")
        if len(data) == 0 or type(data[0]) != str:
            print("** class name missing **")
        elif data[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(data) == 1 or type(data[1]) != int:
            print("** instance id missing **")
        else:
            my_model = BaseModel()
            if my_model.id != data[1]:
                print("** no instance found **")
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
