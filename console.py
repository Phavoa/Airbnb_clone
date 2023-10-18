#!/usr/bin/env python3
"""
The main console for airbnb
"""
from models import storage
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
        if arg == "":
            print("** class name missing **")
        elif "BaseModel" not in arg:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print("{}".format(my_model.id))

    def do_show(self, arg):
        """
        Prints the string form of an instance based on the class name and id
        """
        data = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif data[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(data) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                ins_id = all_objs[obj_id]
                ins_id = ins_id.to_dict()
                if ins_id["id"] == data[1]:
                    print(all_objs[obj_id])
                    return 0
            print("** no instance found **")

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id/
         (save the change into the JSON file).
        """
        if self.test_arg(arg) == 0:
            data = arg.split(" ")
            dict_id = data[0] + "." + data[1]
            del storage.all()[dict_id]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not\
         on the class name
        """
        data = arg.split(" ")
        if arg != "" and data[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_list = []
            obj_dict = storage.all()
            for key in obj_dict.keys():
                new_dict = str(obj_dict[key])
                new_list.append(new_dict)
            print(new_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or\
         updating attribute (save the change into the JSON file).
        """
        if self.test_arg(arg) == 0:
            data = arg.split(" ")
            array = arg.split(" ")
            if len(array) < 3:
                print("** attribute name missing **")
            elif len(array) < 4:
                print("** value missing **")
            else:
                dict_id = data[0] + "." + data[1]
                kwargs = storage.all()[dict_id]
                print(type(kwargs))
                setattr(kwargs, data[2], data[3])
                storage.save()


    def emptyline(self):
        pass

    def test_arg(self, arg):
        """
         Test update method
        """
        data = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif data[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(data) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                ins_id = all_objs[obj_id]
                ins_id = ins_id.to_dict()
                if ins_id["id"] == data[1]:
                    return 0
            print("** no instance found **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
