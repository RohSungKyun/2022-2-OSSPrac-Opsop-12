from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      
      # 학번
<<<<<<< HEAD:TeamHw_3_Code/main.py
      result['Gender'] = request.form.get('Gender')# 성별을 get을 통해 flask에서 gender데이터를 받아옵니다.
      result['Major']=request.form.get('Major') # 학과
=======
      result['Number']=request.form.get('Number')
>>>>>>> 883ced13c4a9a8c30dd5c5b47f3311a36ca7dcf0:app/main.py

      # 성별
      result['Gender'] = request.form.get('Gender')
      
      # 학과
      result['Major']=request.form.get('Major')

      # 프로그래밍 언어
      result['languages'] = ', '.join(request.form.getlist('chkbox'))
      
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()