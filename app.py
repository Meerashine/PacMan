from flask import Flask
import main # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    #return main.your_function_in_the_module()
    return main.main()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)