from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', path='edu_site:', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('#', '')
    config.add_route('artc', '/{artc_name}')
    config.scan('.views')
    return config.make_wsgi_app()
