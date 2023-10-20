#!/usr/bin/env python3
"""
The main console for airbnb
"""
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
import json
import re

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]

    def parseline(self, line):
        """
        Edits the command
        """
        if "." in line:
            name, command = line.split(".")
            com, arg = command.split("(")
            arg = re.findall("[^)]", arg)
            arg = "".join(arg)
            update_arg = "".join(arg)
            arg = re.findall('[^"]', arg)
            arg = "".join(arg)
            if com == "update":
                if "{" in arg:
                    class_id, new_dict = update_arg.split(", {")
                    new_dict = "{" + new_dict
                    class_id = re.findall('[^"]', class_id)
                    class_id = "".join(class_id)
                    line = com + " " + name + " " + class_id + " " + new_dict
                else:
                    class_id, new_attr, value = arg.split(",")
                    line = com + " " + name + " " + class_id + new_attr + value
            else:
                line = com + " " + name + " " + arg
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def do_quit(self, arg):
        """
        The command to quit
        """
        return True

    def emptyline(self):
        pass

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
        elif arg not in self.class_list:
            print("** class doesn't exist **")
        elif arg == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print("{}".format(my_model.id))
        elif arg == "User":
            my_model = User()
            my_model.save()
            print("{}".format(my_model.id))
        elif arg == "Place":
            my_model = Place()
            my_model.save()
            print("{}".format(my_model.id))
        elif arg == "City":
            my_model = City()
            my_model.save()
            print("{}".format(my_model.id))
        elif arg == "Amenity":
            my_model = Amenity()
            my_model.save()
            print("{}".format(my_model.id))
        elif arg == "State":
            my_model = State()
            my_model.save()
            print("{}".format(my_model.id))
        elif arg == "Review":
            my_model = Review()
            my_model.save()
            print("{}".format(my_model.id))

    def do_show(self, arg):
        """
        Prints the string form of an instance based on the class name and id
        """
        data = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif data[0] not in self.class_list:
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
        if arg != "" and data[0] not in self.class_list:
            print("** class doesn't exist **")
        elif data[0] != "":
            new_list = []
            obj_dict = storage.all()
            for key in obj_dict.keys():
                new_dict = obj_dict[key].to_dict()
                if data[0] == new_dict["__class__"]:
                    new_list.append(str(obj_dict[key]))
            print(new_list)
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
            if len(data) < 3:
                print("** attribute name missing **")
            elif len(data) < 4:
                print("** value missing **")
            elif len(data) > 4 and data[2].startswith("{"):
                print(data[2])
                new_dict = ""
                for i in range(2, len(data)):
                    new_dict += data[i]
                new_dict = re.sub("'", '"', new_dict)
                new_dict = "".join(new_dict)
                new_dict = json.loads(new_dict)
                dict_id = data[0] + "." + data[1]
                kwargs = storage.all()[dict_id]
                for key, value in new_dict.items():
                    setattr(kwargs, key, value)
                storage.save()
            else:
                dict_id = data[0] + "." + data[1]
                kwargs = storage.all()[dict_id]
                data[3] = re.findall('[^"]', data[3])
                data[3] = "".join(data[3])
                setattr(kwargs, data[2], data[3])
                storage.save()

    def do_count(self, arg):
        """
        Retrieves the number of instances a class has
        """
        data = arg.split(" ")
        obj_dict = storage.all()
        count = 0
        for key in obj_dict.keys():
            new_dict = obj_dict[key].to_dict()
            if data[0] == new_dict["__class__"]:
                count += 1
        print("{}".format(count))

    def test_arg(self, arg):
        """
         Test update method
        """
        data = arg.split(" ")
        if arg == "":
            print("** class name missing **")
        elif data[0] not in self.class_list:
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
