from fetcher.data_fetcher import MamphiDataFetcher
from flask import Flask, render_template
# from admin.export_data_to_database import MamphiData
import json

# TODO Remove comments to export data from excel sheet to database if database not available
# data = MamphiData()
# data.export_data()
# db = data.db_filename

db = '../data/mamphi.db'  # db = "../" + data.db_filename

fetcher = MamphiDataFetcher(mamphi_db=db)

app = Flask(__name__)


@app.route("/")
def description():
    return render_template("description.html")


@app.route("/mamphi/center%list")
def center():
    zentren = json.loads(fetcher.fetch_center())
    return render_template("center.html", zentren=zentren)


@app.route("/mamphi/patient%consent")
def consent():
    consents = json.loads(fetcher.fetch_consent())
    incomplete_consents = json.loads(fetcher.fetch_incomplete_consent())
    missing_consents = json.loads(fetcher.fetch_missing_consent())
    consents_after_randomization = json.loads(fetcher.fetch_consent_after_randomisation())

    options = [
        {'text': "Bitte Liste auswählen", 'value': None},
        {'text': "Vollstandige Liste der Einwilligungen", 'value': 1},
        {'text': "Liste der fehlenden Einwilligungen", 'value': 2},
        {'text': "Liste der unvollständigen Einwillungen", 'value': 3},
        {'text': "Liste der verspätete Einwilligungen", 'value': 4}
    ]

    return render_template("consent.html", consents=consents, incomplete_consents=incomplete_consents,
                           missing_consents=missing_consents, consents_after_randomization=consents_after_randomization,
                           options=options)


@app.route("/mamphi/randomisation%week=1")
def random_w_1():
    results = json.loads(fetcher.fetch_rand_w1())

    return render_template("random_w_1.html", results=results)


@app.route("/mamphi/randomisation%week=2")
def random_w_2():
    results = json.loads(fetcher.fetch_rand_w2())

    return render_template("random_w_2.html", results=results)


@app.route("/mamphi/monitor/planing")
def monitoring():
    results = json.loads(fetcher.retrieve_monitoring_plan())

    return render_template("monitorplan.html", monitoringplan=results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
