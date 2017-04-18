"""
Some usefull model classes for common work with tendrl web
"""

from webstr.core import WebstrModel, By, PageElement
from webstr.common.form import models as form
import webstr.patternfly.dropdown.models as dropdown


class ListMenuModel(WebstrModel):
    """
    auxiliary model for list menu (filter and order fields)
    """
    filter_by = form.Select(
        By.XPATH,
        '//select[contains(@ng-model, "filterBy")]')
    filter_input = form.TextInput(By.ID, 'filter')
    order_by = form.TextInput(
        By.XPATH,
        '//select[contains(@ng-model, "orderBy")]')
    order_btn = form.Button(
        By.XPATH,
        '//button[contains(@ng-init, "Order")]')


class UpperMenuModel(WebstrModel):
    """
    Common model for upper menu
    """
    # left part of upper navbar
#    events_link
#    node_discovery_link
#    tasks_link
#    about_link
    user_link = PageElement(By.ID, locator="userlogout")


class UserMenuModel(dropdown.DropDownMenuModel):
    """
    Common page model for main page - user page
    """
    logout = PageElement(by=By.LINK_TEXT, locator="Logout")
