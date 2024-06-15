# External Imports
from markdown import Markdown
import re

# Django Imports

# Internal Imports
from notes.src.extensions import KeywordExtension


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


# Markdown parser
def parse_lines(lines, profile_settings):
    parser = Markdown(extensions=[KeywordExtension(profile_settings=profile_settings)])

    parsed_lines = parser.reset().convert(lines)

    return parsed_lines


# Update line status
def update_line(line):
    try:
        if line[:7] != (DONE + " "):
            line = DONE + " " + line
        else:
            line = line[7:]
    except Exception as err:
        pass

    return line


# Update note line
def update_note(note, line):
    old_line = line
    new_line = update_line(line)
    
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
