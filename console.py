#!/usr/bin/python3
'''Entry point of the command interpreter '''
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json

dict_cls = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
            'Amenity': Amenity, 'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    '''Command processor '''
    prompt = '(hbnb) '
    
    def do_EOF(self, args):
        '''EOF command to exit the command interpreter '''
        print('')
        return True

    def do_quit(self, args):
        '''Quit command to exit the command interpreter '''
        return True

    def do_empty_line(self):
        '''do nothing when empty line '''
        pass

    def do_create(self, args):
        '''Creates an instance according to a given class '''
        if args is None or len(args) == 0:
            print('** class name missing **')
        else:
            if args in dict_cls:
                n = eval(str(args) + '()')
                n.save()
                print(n.id)
            else:
                print('** class doesn\'t exist **')

    def do_show(self, args):
        '''Shows string representation of an instance passed '''
        if args is None or len(args) == 0:
            print('** class name missing **')
        else:
            ln = args.split()
            if ln[0] in dict_cls:
                if len(ln) < 2:
                    print('''** instance id missing **''')
                else:
                    objs = models.storage.all()
                    key = str(ln[0]) + "." + str(ln[1])
                    if key in objs:
                        print(objs[key])
                    else:
                        print('** no instance found **')
            else:
                print('** class doesn\'t exist **')

    def do_destroy(self, args):
        '''Deletes an instance passed '''
        if args is None or len(args) == 0:
            print('** class name missing **')
        else:
            ln = args.split()
            if ln[0] in dict_cls:
                if len(ln) < 2:
                    print('''** instance id missing **''')
                else:
                    objs = models.storage.all()
                    key = str(ln[0]) + "." + str(ln[1])
                    if key in objs:
                        del(objs[key])
                        models.storage.save()
                    else:
                        print('** no instance found **')
            else:
                print('** class doesn\'t exist **')

    def do_all(self, args):
        '''Prints string represention of all instances of a given class '''
        objs = models.storage.all()
        obj_list = []
        if args == '':
            for key in objs:
                obj_list.append(str(objs[key]))
            print(obj_list)
        else:
            try:
                ln = args.split()
                eval(ln[0])
                for idx in objs:
                    ax = objs[idx].to_dict()
                    if ax['__class__'] == ln[0]:
                        obj_list.append(str(objs[idx]))
                print(obj_list)
            except Exception:
                print('** class doesn\'t exist **')

    def do_update(self, args):
        '''Updates an instance based on the class name and id '''
        ln = shlex.split(args)
        if len(ln) == 0:
            print('** class name missing **')
        else:
            try:
                eval(str(ln[0]))
            except Exception:
                print('** class doesn\'t exist **')
                return
            if len(ln) == 1:
                print('** instance id is missing **')
            else:
                objs = models.storage.all()
                key = str(ln[0]) + "." + str(lv[1])
                if key not in objs:
                    print('** no instance found **')
                else:
                    if len(ln) == 2:
                        print('** value missing **')
                    else:
                        setattr(objs[key], ln[2], ln[3])
                        models.storage.save()
    
    def do_count(self, args):
        '''counts number of instances of a class '''
        num = 0
        objs = models.storage.all()
        new = {}
        for idx in objs:
            new[idx] = objs[idx].to_dict()
        for idx in new:
            if (args == new[idx]['__class__']):
                num = num + 1
        print(num)

    def default(self, args):
        '''set default on instance based on class and id '''
        first = args.split('.')
        if len(first) > 1:
            cls_name = first[0]
            methods = first[1]
            first[1] = first[1].replace('(', '&(')
            second = first[1].split('&')
            cmmd = cls_name

            if methods == "all()":
                self.do_all(cmmd)
            elif methods == "count()":
                self.do_count(cmmd)
            else:
                methods = second[0]
                elems = second[1]
                elems = elems.replace('(', '')
                elems = elems.replace(')', '')
                elems = elems.replace('{', '"{')
                elems = elems.replace('}', '}"')
                third = shlex.split(elems)
                if not third:
                    id = ' '
                    third.append(id)
                else:
                    for idx in range(len(third)):
                        third[idx] = third[idx].replace(',', ' ')
                        third[idx] = third[idx].strip()
                    id = third[0]
                cmmd = cmmd + ' ' + id
                cmmd = cmmd.replace('\"', '')
                if methods == "show" and len(third) == 1:
                    self.do_show(cmmd)
                elif methods == "destroy" and len(third) == 1:
                    self.do_destroy(cmmd)
                elif methods == "update":
                    x = len(third)
                    if x > 1 and third[1][0] == '{' and third[1][-1] == '}':
                        third[1] = third[1].replace('{', '')
                        third[1] = third[1].replace('}', '')
                        third[1] = third[1].replace(': ', ':')
                        sub = shlex.split(third[1], ', ')
                        new = []
                        for ele in sub:
                            sub2 = ele.split(':')
                            if len(sub2) < 2:
                                sub2.append('')
                            new.append(tuple(sub2))
                        dicti = dict(new)
                        print(dicti)
                        for key in dicti:
                            new_cmd = cmmd + ' '
                            new_cmd += str(key)
                            new_cmd = new_cmd.replace('\"', '')
                            new_cmd = new_cmd.replace('\'', '')
                            new_cmd += ' \"' + str(dicti[key]) + '\"'
                            self.do_update(new_cmd)
                    else:
                        for idx in range(1, len(third)):
                            if idx == 1:
                                cmmd = cmmd + ' ' + third[idx]
                            if idx == 2:
                                cmmd = cmmd + ' '
                                cmmd += '\"' + third[idx] + '\"'
                        self.do_update(cmmd)
                else:
                    return cmd.Cmd.default(self, args)
        else:
            return cmd.Cmd.default(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
