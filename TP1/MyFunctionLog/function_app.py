import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="LogRequestFunction")  # Le nom de la fonction doit être unique dans votre projet
@app.route(route="logrequest", auth_level=func.AuthLevel.ANONYMOUS)  # Vérifiez que "ANONYMOUS" est en majuscule
def log_request(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Request received: {req.get_body().decode('utf-8')}")
    
    # Extraire les données de la requête
    try:
        log_data = req.get_json()  # Obtenez les données JSON de la requête
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)
    
    logging.info(f"Log data: {log_data}")  # Journaliser les données du log

    # Si vous avez besoin de traiter les logs ou d'autres actions, faites-le ici

    return func.HttpResponse("Log received!", status_code=200)
