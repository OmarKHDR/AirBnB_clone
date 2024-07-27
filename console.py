#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    #================

    def emptyline(self) -> bool:
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
