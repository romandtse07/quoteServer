from flask import Flask, send_file, request
import pandas as pd
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        service = request.headers.get('service')
        margin = request.headers.get('margin')
    else:
        service = 'test'
        margin = 0
    dummy = pd.DataFrame([{'service':service, 'margin':margin}])
    excel_file = io.BytesIO()
    writer = pd.ExcelWriter(excel_file, engine='openpyxl')
    dummy.to_excel(writer, index=False)
    writer.close()
    excel_file.seek(0)
    return send_file(excel_file, attachment_filename=f'service.xlsx', as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)