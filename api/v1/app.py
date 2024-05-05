port = os.getenv('HBNB_API_PORT', 5000)

# Cross-Origin Resource Sharing
cors = CORS(app, resources={r'/*': {'origins': host}})
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# app_views BluePrint defined in api.v1.views
app.register_blueprint(app_views)
