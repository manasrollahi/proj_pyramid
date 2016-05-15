from pyramid.events import subscriber
from pyramid.interfaces import IBeforeRender
from pyramid.renderers import get_renderer
from pyramid.view import (
    view_config,
    view_defaults)


@view_defaults(renderer='templates/index.pt')
class Views:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def index(request):
        return {'name': 'edu site'}

    @view_config(route_name='artc' , renderer='templates/article.pt')
    def article(self):
        arct_name=self.request.matchdict['artc_name']
        return {'pagetitle': arct_name}

    # @view_config(route_name='#')
    # def artc(self):
    #     arct_name=self.request.matchdict['artc_name']
    #     return arct_name


@subscriber(IBeforeRender)
def globals_factory(event):
    master = get_renderer('templates/master.pt').implementation()
    event['master'] = master