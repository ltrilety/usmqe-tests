# vim: set tabstop=2 shiftwidth=2 softtabstop=2 colorcolumn=120:
"""
Common page model for navigation bars.
"""


#import pytest

#import urllib.parse

from webstr.core import WebstrModel, By, PageElement
from webstr.common.form import models as form


#location = urllib.parse.urljoin(pytest.config.getini("usm_web_url"), "/#")


class NavMenuBarsModel(WebstrModel):
    """
    Common page model for the main page - navigation.
    """
    #location = urllib.parse.urljoin(pytest.config.getini("usm_web_url"), "/#")
    # left part of upper navbar
    navbar_toggle = form.Button(by=By.XPATH,
                                locator='//*[@class="navbar-toggle"]')
    navbar_brand = PageElement(by=By.XPATH,
                               locator='//*[@class="navbar-brand"]')

    # right part of upper navbar
    alerts_link = PageElement(
        by=By.XPATH,
        locator='//*[@data-template="views/base/alert-dropdown.tpl.html"]')
    hosts_link_menu_locator = \
        '//*[@data-template="views/base/discovered-hosts.tpl.html"]'
    hosts_link_menu = PageElement(
        by=By.XPATH,
        locator=hosts_link_menu_locator)

    progress_link_locator = \
        '//*[@data-template="views/base/progress-dropdown.tpl.html"]'
    progress_link = PageElement(
        by=By.XPATH,
        locator=progress_link_locator)

    user_link_locator = \
        '//*[@data-template="views/base/admin-dropdown.tpl.html"]'
    user_link = PageElement(by=By.XPATH, locator=user_link_locator)

    # left navbar
    dashboard_link = PageElement(by=By.LINK_TEXT, locator="Dashboard")
    clusters_link = PageElement(by=By.LINK_TEXT, locator="Clusters")
    hosts_link = PageElement(by=By.LINK_TEXT, locator="Hosts")
    storages_link = PageElement(by=By.LINK_TEXT, locator="Storage")
    # Storages sub-menu links
    pools_link = PageElement(by=By.LINK_TEXT, locator="Pools")
    rbds_link = PageElement(by=By.LINK_TEXT, locator="RBDs")
    admin_link = PageElement(by=By.LINK_TEXT, locator='Admin')
    # Admin sub-enu links
    tasks_link = PageElement(by=By.LINK_TEXT, locator='Tasks')
    events_link = PageElement(by=By.LINK_TEXT, locator='Events')
    users_link = PageElement(by=By.LINK_TEXT, locator='Users')
    ldap_settings_link = PageElement(by=By.LINK_TEXT, locator='Ldap Settings')
    mail_settings_link = PageElement(by=By.LINK_TEXT, locator='Mail Settings')