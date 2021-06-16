from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/set_val', methods=['POST'])
def set_route():

    prop = request.headers["prop"]
    val = request.headers["val"]

    headers = {
        'prop': prop,
        'val': val
    }

    requests.post('http://db_server:7000/set_val', headers=headers)

    return ""


@app.route('/')
def home():
    values = requests.get('http://db_server:7000/get')
    return """
    
             <b>current values:"""+values.text+"""</b>
    
             <input id="prop"/>
             <input id="val"/>
             <button onclick="update()">update</button>
             
             <script>
               
                
                async function update(){ 
                    await fetch(
                        'http://localhost/set_val',
                        { 
                            headers: {
                                prop: document.getElementById('prop').value,
                                val: document.getElementById('val').value
                            },
                            method: 'POST'
                        }
                    ); 
                    location.reload()
                }

             </script>
        """
