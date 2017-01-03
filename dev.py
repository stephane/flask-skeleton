from skeleton import create_app, register_cli

app = create_app('config.DevelopmentConfig')
register_cli(app)
