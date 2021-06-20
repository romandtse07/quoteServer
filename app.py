from flask import Flask, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def main():
    dummy = pd.DataFrame([{'ugh':1, 'wut':2}])
    excel_file = io.BytesIO()
    writer = pd.ExcelWriter(excel_file, engine='openpyxl')
    dummy.to_excel(writer, index=False)
    writer.close()
    excel_file.seek(0)
    return send_file(excel_file, attachment_filename='dummy.xlsx', as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)