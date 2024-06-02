# External Imports

# Django Imports

# Internal Imports


# Utility functions
def toggle_editable(form, disabled=False):
    for fieldname in form.fields:
        form.fields[fieldname].disabled = disabled
    
    return form
