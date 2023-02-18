from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.add_route('hello_json', '/howdy.json')
    config.add_route('hello-xml', '/howdy.xml')
    config.scan('views')
    return config.make_wsgi_app()

if __name__ == '__main__':
    app = main({})
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
