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

embedded_html = """
<audio controls="controls">  
   <source src="{path}">  
</audio> 
<a href="javascript:showhide('{v_id}')">
            Click to show/hide.
</a>
<div id={v_id} style="display:none;">
        <p>{eng}</p>
</div>
<script>
function showhide(id) 
{{var event = document.getElementById(id);
event.style.display = (event.style.display == 'block') ? 'none' : 'block';
}}
</script>
"""

class Plugin(RestExtension):
    """Plugin for reST voice directive."""

    name = "rest_voice"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        directives.register_directive('voice', Voice)
        self.site.register_shortcode('voice', _gen_voice_embed)
        return super(Plugin, self).set_site(site)



class Voice(Directive):
    """reST extension for insert voice ."""

    has_content = False
    required_arguments = 1
    optional_arguments = 999
    def run(self):
        """Run voice directive."""
        #voice_path="../../thai-mp3/".join(self.arguments[0]);
        voice_path="../../voice/"+self.arguments[0];
        voice_id = self.arguments[0].split('.')[0]
        options = {
	    'path': voice_path,
	    'eng': self.arguments[1],
            'v_id':voice_id,
	    }
        #html = _gen_voice_embed(" ".join(self.arguments))
        return [nodes.raw('',embedded_html.format(**options) , format='html')]


def _gen_voice_embed(url, *q, **kw):
    return '<div class="text-error">{0}</div>'.format(url)
