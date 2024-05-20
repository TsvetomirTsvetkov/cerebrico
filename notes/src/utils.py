SEPARATOR = "#"
ITEM = "ITEM"
PRIORITY = 1
IS_PREFIX = True # TODO: add it per item

TODO_ITEM = "TODO"
TODO_TEMPLATE = """
<div>
    <input type="checkbox" id="{}" name="{}"/>
    <label for={}>{}</label>
</div>
"""

AP_ITEM = "AP"
AP_TEMPLATE = """
<div>
    <p hidden>{}{}{}</p>
    <h3>[Action Point] {}</h3>   
</div>
"""

ITEMS_DICT = {
    TODO_ITEM: TODO_TEMPLATE,
    AP_ITEM: AP_TEMPLATE,
}
