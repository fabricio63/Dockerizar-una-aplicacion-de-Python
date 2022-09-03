
import requests
from flask import Flask, render_template,request
# input text
inp ='ariana grande'


def apple_API_search(inp):

    #results dictionary
    results_appleAPI = []
    #request to Itunes API
    URL = "https://itunes.apple.com/search?term={}".format(inp.replace(" ","+"))
    page = requests.get(URL)

    #extracting relevant data
    for i in page.json()['results']:
        
        var = {'track_name': i['trackName'], 'artistName': i['artistName'],'kind': i['kind']}

        results_appleAPI.append(var)




    return results_appleAPI





def TVmaze_API_search(inp):
    #results dictionary
    results_TVmazeAPI = []
    


    #request to Itunes API
    URL = "https://api.tvmaze.com/search/people?q={}".format(inp.replace(' ','+')) + "&embed=castcredits"
    page = requests.get(URL)

    page = page.json()[0]

    id_artista = page['person']['id']


    URL1 = "https://api.tvmaze.com/people/{}?embed=castcredits".format(id_artista)


    page1 = requests.get(URL1)

    raw_data = page1.json()['_embedded']['castcredits']





    for i in raw_data:
    
        link_var = i['_links']['show']['href']
        page2 = requests.get(link_var)


        name = page2.json()['name']
        var = {'show_name': page2.json()['name'],'artist_name':inp,'kind':"tv show"}

        results_TVmazeAPI.append(var)


    return results_TVmazeAPI



app = Flask(__name__)

@app.route('/home', methods =['GET', 'POST'])
def home():
    if request.method=='POST':
        artist_name = request.form['artist_search']   
        TVmaze_results = []
        apple_results = []
        try:
            TVmaze_results = TVmaze_API_search(artist_name) 
        except:
            pass
        try:
            apple_results = apple_API_search(artist_name)  
        except:
            pass
         
        
        return render_template('search.html',links = TVmaze_results,links1 = apple_results)

    else:
        return render_template('search.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
