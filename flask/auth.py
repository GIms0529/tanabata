from flask import Flask, render_template, request
  
app = Flask(__name__)
  
@app.route('auth')
def auth():
    return render_template('auth.html')
  
@app.route('/output', methods=['POST'])
def output():
    id = request.form['id']
    pwd = request.form['pwd']
      
    true_id = 'tanaka'			
    true_pwd = 'masahiko'			
      
    if true_id==id and true_pwd==pwd:
        kekka = 'いらっしゃいませ！'			
    else:
        kekka = 'IDかパスワードが、ちがいます'		
      
    return kekka
  
  
if __name__=='__main__':
    app.run(debug=True)
  