from flask import Flask, render_template, request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    query = ''
    results = []
    if request.method == 'POST':
        query = request.form['query']
        try:
            results = run_search(query)
        except HttpError as error:
            print(f'An error occurred: {error}')
    return render_template('search.html', query=query, results=results)

def run_search(query):
    # Your existing code to run a Google Cloud Search query goes here
    # For example:
    # credentials = service_account.Credentials.from_service_account_file('path-to-your-service-account-key.json')
    # service = build('cloudsearch', 'v1', credentials=credentials)
    # response = service.query().list(query=query).execute()
    # return response.get('results', [])
    return (results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

