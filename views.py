from pyramid.view import (
    view_config,
    view_defaults
    )


XMLRESP = \
"""<?xml version='1.0' encoding='utf-8' ?>
<hello>
  <name id='123'>Hello View (howdy)</name>
</hello>
"""

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')  # /
    def home(self):
        return {'name': 'Home View'}

    @view_config(route_name='hello')
    @view_config(route_name='hello_json', renderer='json')
    def hello(self):
        return {'name': 'Hello View (howdy)'}

    @view_config(route_name='hello-xml', renderer=None)
    def helloxml(self):
        response = self.request.response
        response.content_type = "application/xml"
        response.text = XMLRESP
        return response
