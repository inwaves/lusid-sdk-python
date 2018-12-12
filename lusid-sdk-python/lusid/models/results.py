# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Results(Model):
    """Results.

    :param version:
    :type version: ~lusid.models.Version
    :param href:
    :type href: str
    :param values:
    :type values: str
    :param format: Possible values include: 'DataReader', 'Portfolio'
    :type format: str or ~lusid.models.enum
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'Version'},
        'href': {'key': 'href', 'type': 'str'},
        'values': {'key': 'values', 'type': 'str'},
        'format': {'key': 'format', 'type': 'str'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, version=None, href=None, values=None, format=None, links=None):
        super(Results, self).__init__()
        self.version = version
        self.href = href
        self.values = values
        self.format = format
        self.links = links
