"""
Page objects for ad-hoc USM lists or tables based on Bootstrap/Patternfly
containers.
"""

from webstr.core import DynamicPageObject, PageObject
from webstr.common import timeouts
from usmqe.web.tendrl.common import models as m_usmcontainers
import webstr.common.containers.pages as containers


class UsmListRow(DynamicPageObject):
  """
  Item/row of a USM List.
  """
  _model = m_usmcontainers.UsmListRow
  _required_elems = ['_root']


class UsmList(containers.ContainerBase):
  """
  USM List.
  """
  _model = m_usmcontainers.UsmList
  _row_class = UsmListRow
  _required_elems = ['_root']


class UsmTableRow(containers.ContainerRowBase):
  """
  Row in USM Table.
  """
  _model = m_usmcontainers.UsmTableRow
  _required_elems = ['_root']


class UsmTable(containers.ContainerBase):
  """
  USM Table.
  """
  _model = m_usmcontainers.UsmTable
  _row_class = UsmTableRow
  _required_elems = ['_root']
