#!/usr/bin/python3
"""Importing the necessary classes and modules"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    instances = {}
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
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
