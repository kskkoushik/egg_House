from flask import Flask, render_template , request
from mdb import  sold_tokens , data , get_all_data

app = Flask(__name__)



@app.route("/")
def first():
     sold_tokens = 0
     value_sold = 0
     all_users = get_all_data()
     for user in all_users:
       sold_tokens += user['sold']
       value_sold += user['sold_val']
     return render_template('mainPage.html' , sold_tokens = sold_tokens , value_sold = value_sold)


@app.route('/sold_submit' , methods = ['POST'])
def sold_tok():
  name = str(request.form['name'])
  sold = int(request.form['tokensold'])
  type = str(request.form['token_type'])
  name = name.upper()
  i = sold_tokens(name , type , sold)
  if i == -1 :
    return name + ' your name is not found in team EggHouse'
  else :
    return name + ' your stats updated sucessfully'
    
@app.route('/view_submit' , methods = ['POST'])
def view_data():
   name = str(request.form['name'])
   name = name.upper()
   details = data(name)
   return render_template('view.html' , details = details)
   
@app.route('/view_everyones_details' , methods= ['POST'])
def list_gen():
  users = get_all_data()
  return render_template('viewlist.html' , users = users)

if __name__ == "__main__" :

   app.run(host = '0.0.0.0' , debug = True)
