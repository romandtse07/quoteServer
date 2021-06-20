from flask import Flask, send_file, request
import pandas as pd
import io

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    service = request.args.get('service')
    margin = request.args.get('margin')
    # in case for testing
    service = 'test' if service is None else service
    margin = 0 if margin is None else service
    dummy = pd.DataFrame([{'service': service,
                           'margin': margin}])
    excel_file = io.BytesIO()
    writer = pd.ExcelWriter(excel_file, engine='openpyxl')
    dummy.to_excel(writer, index=False)
    writer.close()
    excel_file.seek(0)
    return send_file(excel_file, attachment_filename=f'{service}.xlsx', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
