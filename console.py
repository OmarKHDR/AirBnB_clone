#!/usr/bin/env python3
import cmd
""" cmd.Cmd object which give the cmd properties 
    HBNBCommand will be our interface while developing the BnB clone proj"""


class HBNBCommand(cmd.Cmd):
    """ ######### cmd prompet #########"""

    def emptyline(self) -> bool:
        """ when entering empty line """
        return 

    def do_quit(self, arg):
        """ this command can quit that country"""
        raise SystemExit

    def do_EOF(self, arg):
        """ documented quit signal"""
        print()
        raise SystemExit

if __name__ == '__main__':
    myCmd = HBNBCommand()
    myCmd.prompt =  "(hbnb) "
    myCmd.cmdloop('')
