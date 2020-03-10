from flask import Flask, jsonify, request
from fetcher.data_fetcher import MamphiDataFetcher
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

fetcher = MamphiDataFetcher('../../data/mamphi.db')


@app.route('/mamphi/consents')
@cross_origin()
def get_consents():
    return jsonify(fetcher.fetch_consent())


@app.route('/mamphi/consents/incomplete')
@cross_origin()
def get_incomplete_consents():
    return jsonify(fetcher.fetch_incomplete_consent())


@app.route('/mamphi/consents/missing')
@cross_origin()
def get_missing_consent():
    return jsonify(fetcher.fetch_missing_consent())


@app.route('/mamphi/consents/later')
@cross_origin()
def get_content_after_rand():
    return jsonify(fetcher.fetch_consent_after_randomisation())


@app.route('/mamphi/center')
@cross_origin()
def get_center():
    return jsonify(fetcher.fetch_center())


@app.route('/mamphi/random-week1')
@cross_origin()
def get_rand_w1():
    return jsonify(fetcher.fetch_rand_w1())


@app.route('/mamphi/center/update', methods=["POST"])
@cross_origin()
def upload_center():
    center_json = request.get_json()
    print(center_json)
    fetcher.update_zentren(json.dumps(center_json))
    return jsonify(center_json)


@app.route('/mamphi/consents/update', methods=["POST"])
@cross_origin()
def upload_consent():
    consent_json = request.get_json()
    print(consent_json)
    fetcher.update_consent(json.dumps(consent_json))
    return jsonify(consent_json)


@app.route('/mamphi/random-week2')
@cross_origin()
def get_ran_w2():
    return jsonify(fetcher.fetch_rand_w2())


@app.route('/mamphi/patient/center/week1')
@cross_origin()
def get_number_of_patient_per_center_by_week_1():
    return jsonify(fetcher.get_number_patient_per_center_per_country_by_week_1())


@app.route('/mamphi/patient/center/week2')
@cross_origin()
def get_number_of_patient_per_center_by_week_2():
    return jsonify(fetcher.get_number_patient_per_center_per_country_by_week_2())

# TODO implement api for adding and deleting center and consent via httpRequest
# TODO implement api for fetching monitoring plan


if __name__ == '__main__':
    app.run()
