from django import template
from django.core.exceptions import ObjectDoesNotExist

from ..models import MenuItem

register = template.Library()


def get_item_parents(parent):
    """Возвращает список идентификаторов родителей для указанного элемента."""
    active_item_parents = []
    while parent is not None:
        active_item_parents.append(parent.id)
        parent = parent.parent
    return active_item_parents


def get_item_children(item_val, active_parent_id, selected_item_ids):
    """Возвращает список дочерних элементов для указанного родителя."""
    active_item_children = [
        item for item in item_val.filter(parent_id=active_parent_id)
    ]
    for child in active_item_children:
        if child["id"] in selected_item_ids:
            child["child_items"] = get_item_children(
                item_val, child["id"], selected_item_ids
            )
    return active_item_children


@register.inclusion_tag("app_menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    """Возвращает словарь данных для включения в шаблон меню."""
    items = MenuItem.objects.filter(menu__name=menu_name)
    item_val = items.values()
    root_items = [item for item in item_val.filter(parent=None)]

    try:
        active_item = items.get(slug=context["request"].GET[menu_name])
        active_item_parents = get_item_parents(active_item)

        for parent in root_items:
            if parent["id"] in active_item_parents:
                parent["child_items"] = get_item_children(
                    item_val, parent["id"], active_item_parents
                )

        return {"items": root_items, "menu_name": menu_name}

    except (KeyError, ObjectDoesNotExist):
        return {"items": root_items, "menu_name": menu_name}
