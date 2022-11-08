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
      result['Gender'] = request.form.get('Gender')# 성별을 get을 통해 flask에서 gender데이터를 받아옵니다.
      result['Major']=request.form.get('Major') # 학과

      # 프로그래밍 언어 -> hint) ','.join(list명)을 사용하면 list 안에 있는 항목들이 ','로 나누어져 출력됨.

      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()
