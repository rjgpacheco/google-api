import re
import pandas as pd
from googleapiclient.discovery import build

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Utilities
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def sheet_urt_to_id(url):
    matches = re.findall(r"https://docs.google.com/spreadsheets/d/(\S+)/", url)
    if len(matches) > 0:
        return matches[0]
    else:
        return None


def parse_sheet_id(string):
    if "docs.google.com" in string:
        return sheet_urt_to_id(string)
    else:
        return string


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Class
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Sheet:
    """
    Interface with Google Sheets rest API
    Reference: https://developers.google.com/sheets/api/reference/rest
    """

    def __init__(self):
        raise NotImplementedError

    def _append(self):
        "Appends values to a spreadsheet."
        raise NotImplementedError

    def _batchClear(self):
        "Clears one or more ranges of values from a spreadsheet."
        raise NotImplementedError

    def _batchClearByDataFilter(self):
        "Clears one or more ranges of values from a spreadsheet."
        raise NotImplementedError

    def _batchGet(self):
        "Returns one or more ranges of values from a spreadsheet."
        raise NotImplementedError

    def _batchGetByDataFilter(self):
        "Returns one or more ranges of values that match the specified data filters."
        raise NotImplementedError

    def _batchUpdate(self):
        "Sets values in one or more ranges of a spreadsheet."
        raise NotImplementedError

    def _batchUpdateByDataFilter(self):
        "Sets values in one or more ranges of a spreadsheet."
        raise NotImplementedError

    def _clear(self):
        "Clears values from a spreadsheet."
        raise NotImplementedError

    def _get(self):
        "Returns a range of values from a spreadsheet."
        raise NotImplementedError

    def _update(self):
        "Sets values in a range of a spreadsheet."
        raise NotImplementedError

    def read_range(self):
        raise NotImplementedError

    def read_sheet(self):
        raise NotImplementedError

