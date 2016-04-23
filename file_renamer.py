#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'nabeel'


import os # os is a library that gives us the ability to make OS changes

def file_renamer(list_of_files, new_file_name_list):
    for file_name in list_of_files:
        for (new_filename, barcode_infile) in new_file_name_list:
            # as per the mentioned filename pattern -> xxxx.1.xxxx.[barcode]
            barcode_current = file_name[12:19] # extracting the barcode from current filename
            # print 'barcode_current - ', barcode_current
            # print 'barcode_infile - ', barcode_infile
            # print 'new filename  - ', new_filename
            if barcode_current == barcode_infile:
                os.rename(file_name, new_filename)  # renaming step
                print 'Successfully renamed %s to %s ' % (file_name, new_filename)


if __name__ == "__main__":
    path = os.getcwd()  # preassuming that you'll be executing the script while in the files directory
    file_dir = os.path.abspath(path)

    # path_newname_file = raw_input('enter path to the txt file with new names')

    newname_file = raw_input('enter file with new names: ')
    path_newname_file = os.path.join(file_dir, newname_file)
    new_file_name_list = []
    # print path
    # print file_dir
    # print path_newname_file
    with open(path_newname_file) as file:
        for line in file:
            x = line.strip().split(',')
            new_file_name_list.append(x)
    # print new_file_name_list

    list_of_files = os.listdir(file_dir)
    print 'The list of files - ', list_of_files

    file_renamer(list_of_files, new_file_name_list)

