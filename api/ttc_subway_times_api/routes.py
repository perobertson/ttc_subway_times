def init_routes(app):
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'