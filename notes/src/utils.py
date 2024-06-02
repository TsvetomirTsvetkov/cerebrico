# Utilities


# Constants
ITEM = "ITEM"
PRIORITY = 1

CB_TYPE = "CheckButton"
CB_TEMPLATE = """
<div>
    <input type="checkbox" id="{}" name="{}"/>
    <label for={}>{}</label>
</div>
"""

TYPE_DICT = {
    CB_TYPE: CB_TEMPLATE,
}
