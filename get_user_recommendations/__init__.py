import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    user_id = req.params.get('user_id')

    if not user_id:
        return func.HttpResponse("[ERROR] : No user ID provided !")
    else:
        request_url = "http://armeloc.pythonanywhere.com/get_recommendation/771"
        r = requests.post(url)
        return func.HttpResponse(str(r.text)) 
