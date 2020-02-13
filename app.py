from flask import Flask, render_template, request,redirect , url_for
from pymongo import MongoClient
# from flask_bootstrap import Btstrap


app = Flask(__name__, template_folder='templates')
#bootstrap = Bootstrap(app)

@app.route('/welcome', methods=['GET'])
def samplefunction():
    client = MongoClient('localhost', 27017, maxPoolSize=50)
    db = client.BE
    collection = db['locationsFinal']
    cursor = collection.find({})
    data = ''
    ll = []
    for document in cursor:
        #   print(document)
          ll.append(document)
          data += '[' + str(document['loc']['lat']) + ',' + str(document['loc']['lng']) + '],'
    data = data[:-1]
    #print(data)
    return render_template('map.html', data=ll)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def logindisplayfunction():
    #login page render
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)     




if __name__ == '__main__':
     app.run(debug=True)