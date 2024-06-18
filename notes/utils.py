# External Imports
import re

# Django Imports
from django.shortcuts import get_object_or_404

# Internal Imports


# Helper Constants
DONE = "[DONE]"

CHCK = '[CHCK]'
UNCH = '[UNCH]'


# Keyword Types
class KeywordTypes():
    CB   = '_cb_'

    @classmethod
    def get_vars(cls):
        attributes = vars(cls)
        cls_vars = []

        for key, value in attributes.items():
            if not callable(value) and not key.startswith("__") and key != 'get_vars':
                cls_vars.append(value)
        
        return cls_vars
    

# Utility functions

# Note model save path
def user_directory_path(instance, filename=""):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


# Update line status
def change_state(line):
    # TODO: Check with small keyword
    try:
        if line[:7] != (DONE + " "):
            line = DONE + " " + line
        else:
            line = line[7:]
    except Exception as err:
        pass

    return line


# Update note line
def update_line(note, line):
    old_line = line
    new_line = change_state(line)
    
    with open(note.upload.path, 'r') as f:
        note_contents = f.read()

    with open(note.upload.path, 'w') as f:
        note_contents = note_contents.replace(old_line, new_line)
        f.write(note_contents)
        note.save()


# Convert task to a dictionary
def get_task_dict(split_string):
    task_dict = {'state': '', 'item': '', 'text': ''}

    if split_string[0] == DONE:
        task_dict['state'] = 'checked'
        task_dict['item'] = split_string[1]
        task_dict['text'] = " ".join(split_string[2:])
    else:
        task_dict['state'] = ''
        task_dict['item'] = split_string[0]
        task_dict['text'] = " ".join(split_string[1:])

    return task_dict


# Gather tasks from notes
def get_tasks(notes, profile_settings):
    all_tasks_dict = {}

    for note in notes:
        with note.upload.open('r') as f:
            lines = f.readlines()
            for line in lines:
                for item in profile_settings:
                    m = re.search(repr(item), line)
                    if m:
                        if note.title not in all_tasks_dict.keys():
                            all_tasks_dict[note.title] = []

                        split_string = line.split()

                        all_tasks_dict[note.title].append(get_task_dict(split_string))

    return all_tasks_dict


# Update tasks in note contents
def update_tasks_status(request, form_data, all_tasks_dict):
    for field, value in form_data:
        if KeywordTypes.CB in field:
            split_string = field.split(KeywordTypes.CB)
            note_title = split_string[0]
            line = split_string[1]
            
            for items in all_tasks_dict[note_title]:
                if (items['item'] + ' ' + items['text']) == line:
                    try:
                        if value == CHCK:
                            items['state'] = 'checked'
                            note = get_object_or_404(request.user.note_set, title=note_title)
                            update_line(note, line)
                        elif value == UNCH:
                            items['state'] = ''
                            note = get_object_or_404(request.user.note_set, title=note_title)
                            update_line(note, DONE + ' ' + line)
                        else:
                            continue
                    except Exception as err:
                        pass
