#!/usr/bin/python3
"""Importing the necessary classes and modules"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class that creates the console module"""
    
    instances = {}
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handling End Of file
        """
        return True

    def do_quit(self, line):
        """Handling Quit command
        """
        return True

    def emptyline(self):
        """Handling empty lines
        """
        pass

    def do_create(self, line):
        """Handling the create command
        """
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        try:
            model_class = globals()[class_name]
            print(model_class)
            new_instance = model_class()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Handling the show command
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()

            class_name = args[0] if len(args) >= 1 else None
            instance_id = args[1] if len(args) > 1 else None

            try:
                model_ = globals()[class_name]
            except KeyError:
                print("** class doesn't exist **")
            else:
                if instance_id is None:
                    print("** instance id missing **")
                    return

                dic = storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in dic:
                    print(dic[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Handling the destroy command
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()

            class_name = args[0] if len(args) >= 1 else None
            instance_id = args[1] if len(args) > 1 else None

            try:
                model_ = globals()[class_name]
            except KeyError:
                print("** class doesn't exist **")
            else:
                if instance_id is None:
                    print("** instance id missing **")
                    return

                dic = storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in dic:
                    del dic[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Handling the all command
        """
        class_name = arg.split()[0] if arg else None
        if class_name and class_name not in storage.all_classes():
            print("** class doesn't exist **")
            return

        all_instances = storage.all()
        if class_name:
            instances = [str(instance) for instance in all_instances.values()
                         if
                         instance.__class__.__name__ == class_name]
        else:
            instances = [str(instance) for instance in all_instances.values()]

        print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
