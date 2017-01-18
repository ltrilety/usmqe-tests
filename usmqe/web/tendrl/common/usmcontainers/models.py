"""
Page elements for ad-hoc USM lists or tables based on Bootstrap/Patternfly
containers.
"""


from webstr.core import By
from webstr.core import WebstrModel, DynamicWebstrModel
from webstr.core import PageElement, RootPageElement, NameRootPageElement


class UsmListModel(WebstrModel):
    """
    USM List model.
    """
    LIST_XPATH = ".//*[contains(@class, 'col-md-12')]"
    _root = RootPageElement(By.XPATH, LIST_XPATH)
    rows = PageElement(By.XPATH, './/*[contains(@class,"blade-view")]', as_list=True)


class UsmListRowModel(DynamicWebstrModel):
    """
    Item/row of a USM List.
    """
    _root = None
    """
    One needs to define XPath locator for a particular row by it's name. Eg.::
  
      _root = NamedRootPageElement(
        by=By.XPATH,
        locator='(' + UsmList.LIST_XPATH + '//*[contains(@class,"blade-view")]) SOMETHING-WITH-%s'))
    """
  
  
class UsmTableModel(WebstrModel):
    """
    USM Table model.
    """
    _root = RootPageElement(By.XPATH, "//table[contains(@class,'table')]")
    rows = PageElement(By.XPATH, "./tbody/tr", as_list=True)
  
  
class UsmTableRowModel(DynamicWebstrModel):
    """
    Row of an USM Table.
    """
    _root = NameRootPageElement(By.XPATH, "//table[contains(@class,'table')]/tbody/tr[%d]")
