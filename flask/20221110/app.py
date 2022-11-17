from flask import Flask, render_template, request
  
app = Flask(__name__)

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/input_app', methods=['POST'])
def input_app():
    id = request.form['id']
    pwd = request.form['pwd']
    address = request.form['address']
    favorite = request.form['favorite']
    file = open('data.txt', 'a')
    file.write(id+'\n')
    file.write(pwd+'\n')
    file.write(address+'\n')
    file.write(favorite+'\n')
    file.close()
  
  
if __name__=='__main__':
    app.run(debug=True)
  