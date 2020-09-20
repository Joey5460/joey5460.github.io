# -*- coding: utf-8 -*-

# Copyright © 2012-2017 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Voice directive for reStructuredText."""

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from nikola.plugin_categories import RestExtension
from nikola.utils import req_missing
import re

embedded_html = """
<div id="testdiv">
        <p>{text}</p>
</div>
"""

class Plugin(RestExtension):
    """Plugin for reST voice directive."""

    name = "rest_voice"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        directives.register_directive('literalinclude', Include)
        self.site.register_shortcode('literalinclude', _gen_voice_embed)
        return super(Plugin, self).set_site(site)

class Include(Directive):
    """reST extension for insert voice ."""

    has_content = False
    required_arguments = 1
    optional_arguments = 999
    def run(self):
        """Run voice directive."""
        filePath="/home/fossy/projs/website/joey5460.github.io/files/attachment/"+self.arguments[0];
        text = str()
        with open(filePath) as f:
            tmpln = f.readline()
            flag = False
            while tmpln:
                obj= re.match(r'^//!', tmpln)
                if obj:
                    flag = not flag
                elif flag:
                    text+=tmpln
                tmpln = f.readline()
        options = {
	    'text': text,
	    }
        return [nodes.raw('',embedded_html.format(**options) , format='html')]


def _gen_voice_embed(url, *q, **kw):
    return '<div class="text-error">{0}</div>'.format(url)
