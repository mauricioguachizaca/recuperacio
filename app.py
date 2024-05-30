from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        app.config.from_object('config.config.Config')
    except Exception as e:
        print(f"Error loading configuration: {str(e)}")

    with app.app_context():
        from routes.router import router
        app.register_blueprint(router)

    return app
