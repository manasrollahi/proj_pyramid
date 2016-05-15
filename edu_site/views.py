from pyramid.view import (
    view_config,
    view_defaults)


@view_defaults(renderer='templates/index.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def my_view(request):
        return {'name': 'edu site'}
