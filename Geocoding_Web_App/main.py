from flask import Flask, render_template, request
import pandas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        print('Files ', request.files)
        items = {}
        fields = []
        try:
            fileName = request.files['file_upload']
            print('File name: ', fileName)

            data_csv = pandas.read_csv(fileName)
            fields = data_csv.columns.values
            items = data_csv.to_dict('records')
        except:
            print("Handling file error")

        print('Data: ', items)
        return render_template('success.html', fields=fields, items=items)
    else: 
        return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
