""" This module determines what files and folders will be displayed.
"""

import os, configparser

config = configparser.ConfigParser()
config.read('playerConfig')

parent_directory = config['Directories']['Base directory']


def get_dir(current_working_directory, selected_directory=None):
    # Given the working directory and an optional selected directory, return the child and subchild directories.
    subdirs = os.listdir(current_working_directory)
    if selected_directory == None:
        selected_directory = subdirs[0]
    try:
        selected_subdirs = os.listdir(current_working_directory + '\\' + selected_directory)
    except NotADirectoryError:
        selected_subdirs = []
    return subdirs, selected_directory, selected_subdirs


def dirchange(current_working_directory, dircounter, directorylist, action=''):
    # Change directory based on an action. Maintains a directory list for going up/down levels.
    global parent_directory
    if action == 'downlevel':
        try:
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            directorylist.append(selected_directory)
            current_working_directory = parent_directory + '\\' + '\\'.join(directorylist)
            selected_directory = get_dir(current_working_directory)[1]
            dircounter = 0
            return current_working_directory, selected_directory, directorylist, dircounter
        except NotADirectoryError:
            print('That is not a directory!')
            del (directorylist[-1])
            current_working_directory = parent_directory + '\\' + '\\'.join(directorylist)
            selected_directory = get_dir(current_working_directory)[1]
            dircounter = 0
            return current_working_directory, selected_directory, directorylist, dircounter
    if action == 'uplevel':
        try:
            del(directorylist[-1])
            current_working_directory = parent_directory + '\\' + '\\'.join(directorylist)
            selected_directory = get_dir(current_working_directory)[1]
            dircounter = 0
            return current_working_directory, selected_directory, directorylist, dircounter
        except IndexError:
            print(current_working_directory)
            print('You are at the root music directory!')
            selected_directory = get_dir(current_working_directory)[1]
            return current_working_directory, selected_directory, directorylist, dircounter
    if action == 'nextdir':
        try:
            dircounter += 1
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory, directorylist, dircounter
        except IndexError:
            dircounter = 0
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory, directorylist, dircounter
    if action == 'prevdir':
        try:
            dircounter -= 1
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory, directorylist, dircounter
        except IndexError:
            dircounter = -1
            selected_directory = get_dir(current_working_directory)[0][dircounter]
            return current_working_directory, selected_directory, directorylist, dircounter
    if action == '':
        selected_directory = get_dir(current_working_directory)[0][dircounter]
        return current_working_directory, selected_directory, directorylist, dircounter


def file_update(current_working_directory, dircount, directorylist, action = ''):
    change = dirchange(current_working_directory, dircount, directorylist, action)
    current_dir = change[0]
    select_dir = change[1]
    dirlist = change[2]
    dircount = change[3]
    directories = get_dir(change[0], change[1])
    subdirectories = directories[0]
    selected_dir = directories[1]
    selected_subdirectories = directories[2]
    return current_dir, select_dir, dirlist, dircount, subdirectories, selected_dir, selected_subdirectories
