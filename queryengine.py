import sqlite3 as sql
from sqlite3 import Error
import section_names

def give_sect_nums():
    global_var_lst = dir(section_names)
    module_section_list = []
    for item in global_var_lst:
        if item[0:6] == "MODULE":
            module_section_list.append(int(str(item[7]) + str(item[17])))
    return module_section_list

class Section:

    instances = {}

    def __init__(self, section_id, grades):
        self.section_id = section_id
        self.__class__.instances[self.section_id] = self
        self.grades = grades

    @property
    def section_id(self):
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        self._section_id = section_id

    @property
    def grades(self):
        return self._grades
    
    @grades.setter
    def grades(self, grades):
        self._grades = grades

class Module:

    instances = {}

    def __init__(self, module_id, all_sections):
        self.module_id = module_id
        self.sections = {}
        self.__class__.instances[self.module_id] = self
        for section in all_sections:
            if int(str(section)[0]) == module_id:
                self.sections[section] = all_sections[section]

    
    @property
    def mod_id(self):
        return self._module_id

    @mod_id.setter
    def mod_id(self, module_id):
        self._module_id = module_id

    @property
    def sections(self):
        return self._sections

    @sections.setter
    def setter(self, sections):
        self._sections = sections

# module1 = Module(1, Section.instances)

print(Section.instances)

  # def get_grades(self, grades):
    #     self.grades = grades

    # @classmethod
    # def create_section_ids(cls):
    #     '''Creates Section instance for every section_id'''
    #     section_lst = give_sect_nums()
    #     # print(section_lst)
    #     for section in section_lst:
    #         sections = Section(section_id = section)
            
    
# Section.create_section_ids()
# print(Section.instances)

   # @classmethod
    # def get_mod_ids(cls):
    #     '''Creates Module instances/Module_ids using Section_ids'''
    #     mod_nums = set(map(lambda section: int(str(section)[0]), Section.instances))
    #     for nums in mod_nums:
    #         module = Module(module_id = nums)

    # def get_sections(self):
    #     '''Returns dictionary of section_id:section object for a Module'''
    #     for key in Section.instances:
    #         if int(str(key)[0]) == self.module_id:
    #             print(self.module_id)