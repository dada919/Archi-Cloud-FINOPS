import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="LogRequestFunction")  # Ceci doit correspondre au nom de votre fonction
@app.route(route="logrequest", auth_level=func.AuthLevel.ANONYMOUS)
def log_request(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Request received: {req.get_body()}")
    return func.HttpResponse("Log received!", status_code=200)
