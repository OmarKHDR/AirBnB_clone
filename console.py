#!/usr/bin/env python3
""" maybe here """
""" cmd.Cmd object which give the cmd properties
    HBNBCommand will be our interface while developing the BnB clone proj"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ ######### cmd prompet #########"""
    @staticmethod
    def find_subclasses(Base, arr):
        arr.append(Base.__name__)
        sub = Base.__subclasses__()
        if sub == []:
            return
        else:
            for c in sub:
                HBNBCommand.find_subclasses(c,arr)

    @staticmethod
    def ClassExist(cls):
        arr = []
        HBNBCommand.find_subclasses(BaseModel, arr)
        if cls not in arr:
            raise NameError
    

    def emptyline(self) -> bool:
        """ when entering empty line nothing will happen """
        return

    def do_quit(self, arg):
        """ can quit the script: $quit"""
        raise SystemExit

    def do_EOF(self, arg):
        """ quit when sending quit signal: $ctrl + d == quit"""
        print()
        raise SystemExit

    def do_create(self, arg):
        """creating a new object that's based on BaseModel class : $create ClassName"""
        
        if arg == '':
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except:
            print("** class doesn't exist **")
        return


    def do_show(self, arg1):
        """show a saved instance: $show ClassName ID"""
        arg = arg1.split(" ")
        try:
            HBNBCommand.ClassExist(arg[0])
            if arg[0] == '':
                print("** class name missing **")
                return
            elif arg[1] == '':
                print("** instance id missing **")
                return

            storage.reload()
            dic = storage.all()
            obj_dict = dic[arg[0]+'.'+arg[1]]
            obj = eval(arg[0])(**obj_dict)
            print(obj)
        except (KeyError, IOError):
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
        return

    def do_destroy(self, args):
        """delete an object: $destroy ClassName ID"""
        arg = args.split(" ")
        
        try:
            HBNBCommand.ClassExist(arg[0])
            if arg[0] == '':
                print("** class name missing **")
                return
            if arg[1] == '':
                print("** instance id missing **")
                return

            storage.reload()
            dic = storage.all()
            del dic[arg[0] + '.' + arg[1]]
            storage.save()
        except (KeyError, IOError):
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
        return
    
    def do_all(self, args):
        """ print all objects: $all ClassName or $all"""
        try:
            if args != '':
                HBNBCommand.ClassExist(args)
            storage.reload()
            dic = storage.all().copy()
            for key, val in dic.items():
                if args in key :
                    print(BaseModel(**val))
        except:
            print(" ** class doesn't exist **")

    def do_update(self,args):
        """adding attr to existing object: $update ClassName ID attr_name 'attr value'"""
        arg = args.split(" ")
        match len(arg):
            case 0:
                print("** class name missing **")
            case 1:
                print("** instance id missing **")
            case 2:
                print("** attribute name missing **")
            case 3:
                print("** value missing **")
            case 4:
                try:
                    HBNBCommand.ClassExist(arg[0])
                    storage.reload()
                    dic = storage.all()
                    obj = dic[arg[0]+'.'+arg[1]]
                    obj[arg[2]] = arg[3]
                    storage.save()
                except NameError:
                    print("** class doesn't exist **")
                except KeyError:
                    print("** no instance found **")

if __name__ == '__main__':
    myCmd = HBNBCommand()
    myCmd.prompt = "(hbnb) "
    myCmd.cmdloop('use help or ? for commands\n========================================')
    