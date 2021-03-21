import sqlite3
import json
import pandas as pd


class MamphiDataFetcher:

    mamphi_db = ""

    def __init__(self, mamphi_db=mamphi_db):
        self.mamphi_db = mamphi_db

    def fetch_center(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Zentren"
        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def fetch_consent(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Informed_consent"
        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def fetch_rand_week(self, week):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Random_Woche_{}".format(week)
        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def get_center_by_land(self, land):

        if land == "Germany":
            conn = sqlite3.connect(self.mamphi_db)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            statement = "SELECT * FROM Zentren WHERE Land = 'D'"

            cursor.execute(statement)
            results = cursor.fetchall()

            conn.commit()
            conn.close()
            german_center = json.dumps([dict(ix) for ix in results])
            # number_patient = len(list_patient)
            return german_center

        elif land == "UK":
            conn = sqlite3.connect(self.mamphi_db)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            statement = "SELECT * FROM Zentren WHERE Land = 'GB'"
            cursor.execute(statement)
            results = cursor.fetchall()

            conn.commit()
            conn.close()
            uk_center = json.dumps([dict(ix) for ix in results])
            # number_patient = len(list_patient)
            return uk_center

    def update_zentren(self, center_json):
        """

        :rtype: object
        :param center_json: json string of the value to be inserted in the database
        """
        center = json.loads(center_json)

        # Compute center Id manually
        values = []
        if center['Land'] == "D":
            zentrum_id = self.getMaxZentrumID(country='D') + 1
            values.append(zentrum_id)
        else:
            zentrum_id = self.getMaxZentrumID(country='GB') + 1
            values.append(zentrum_id)

        for idx in center.values():
            values.append(idx)

        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "INSERT INTO Zentren VALUES" + str(tuple(values))
        try:
            cursor.execute(statement)

            conn.commit()
            print(cursor.rowcount, "record inserted.")

        except:
            conn.rollback()

        conn.close()

    def getMaxZentrumID(self, country):

        statement = "SELECT max(Zentrum_Id) as MAX_ID " \
                    "FROM Zentren WHERE Land = '{}'".format(country)

        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        response = cursor.execute(statement)
        result = response.fetchall()

        return result[0][0]

    def getMaxPatientID(self):

        statement = "SELECT max(Patient_Id) " \
                    "FROM Informed_consent" \

        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        response = cursor.execute(statement)
        result = response.fetchall()

        return result[0][0]

    def update_consent(self, consent_json):

        consent_item = json.loads(consent_json)
        values = []
        # search for max patient id
        patient_id = self.getMaxPatientID() + 1

        values.append(patient_id)

        for idx in consent_item.values():
            values.append(idx)

        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "INSERT INTO Informed_consent VALUES" + str(tuple(values))
        try:
            cursor.execute(statement)

            conn.commit()
            print(cursor.rowcount, "record inserted.")

        except:
            conn.rollback()

        conn.close()


    def update_rand_week(self, value, week):
        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "INSERT INTO Random_Week_{}".format(week) + value
        try:
            cursor.execute(statement)

            conn.commit()
            print(cursor.rowcount, "record inserted.")

        except:
            conn.rollback()

        conn.close()

    def get_center_list_country(self, country):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        statement = "SELECT * FROM Zentren WHERE Land = 'D'" if country == "Deutschland" \
            else "SELECT * FROM Zentren WHERE Land = 'GB'"

        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        # results_json = json.dumps([dict(ix) for ix in results])
        list_patient = json.dumps([dict(ix) for ix in results])
        # number_patient = len(list_patient)

        return list_patient

    def fetch_consent_list(self, consent):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if consent is "missing":
            statement = "SELECT * FROM Informed_consent WHERE Einwilligung = 'nan' AND Datum != 'NaT'"
        elif consent is "incomplete":
            statement = "SELECT * FROM Informed_consent WHERE Einwilligung = 'nan'"
        else:
            statement = "SELECT * FROM Informed_consent WHERE Datum > '2019.06.03'"

        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def get_number_of_patient_per_center_by_week(self, week):

        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        statement = "SELECT Random_Woche_{}.Zentrum, COUNT(Random_Woche_{}.Zentrum) as Number_Of_Patient" \
                    "FROM Random_Woche_{} GROUP BY Random_Woche_2.Zentrum;".format(week, week, week)

        cursor.execute(statement)
        results = cursor.fetchall()
        conn.commit()
        conn.close()

        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def get_number_patient_per_center_per_country_by_week(self, week):
        """

        :return: Return list of patient per center in both country
        """

        weekly_list_german = json.loads(self.get_number_patient_per_center_by_week_in_country(week, 'D'))
        weekly_list_uk = json.loads(self.get_number_patient_per_center_by_week_in_country(week, 'GB'))

        results = {'Germany': weekly_list_german, 'UK': weekly_list_uk}

        return json.dumps(results)

    def get_number_patient_per_center_by_week_in_country(self, week, country):

        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        statement = "SELECT tab1.Zentrum as Zentrum, tab1.Anzahl as Number_Of_Patient, tab2.Land " \
                    "FROM " \
                    "(SELECT Random_Woche_{}.Zentrum, COUNT(Random_Woche_{}.Zentrum) as Anzahl " \
                    "FROM Random_Woche_{} GROUP BY Random_Woche_{}.Zentrum) tab1 LEFT JOIN " \
                    "(SELECT Zentrum_Id, Land FROM Zentren) tab2 ON tab1.Zentrum = tab2.Zentrum_Id " \
                    "WHERE Land = '{}'".format(week, week, week, week, country)

        cursor.execute(statement)
        results = cursor.fetchall()
        conn.commit()
        conn.close()

        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def fetch_center_ids(self):

        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = "SELECT Zentrum_Id FROM Zentren"
        response = cursor.execute(query)
        results = response.fetchall()

        center_ids = [dict(idx) for idx in results]

        return json.dumps(center_ids)

    def remove_center_by_id(self, center_id):
        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "DELETE FROM Zentren WHERE Zentrum_Id = {}".format(center_id)
        cursor.execute(statement)
        conn.commit()
        conn.close()

    def remove_consent_by_id(self, patient_id):
        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "DELETE FROM Informed_consent WHERE Patient_Id = {}".format(patient_id)
        cursor.execute(statement)
        conn.commit()
        conn.close()

        print("An item have been removed")

    def retrieve_centres_with_number_of_patient(self):

        statement = "SELECT Zentrum_Id, Number_Of_Patient " \
                    "FROM " \
                    "(SELECT Zentrum_Id FROM Zentren ORDER BY Zentrum_Id ASC) " \
                    "LEFT JOIN (SELECT Zentrum, SUM(Anzahl) as Number_Of_Patient " \
                    "FROM " \
                    "(SELECT Random_Woche_1.Zentrum, COUNT(Random_Woche_1.Zentrum) as Anzahl " \
                    "FROM Random_Woche_1 GROUP BY Random_Woche_1.Zentrum " \
                    "UNION SELECT Random_Woche_2.Zentrum, COUNT(Random_Woche_2.Zentrum) as Anzahl " \
                    "FROM Random_Woche_2 GROUP BY Random_Woche_2.Zentrum) " \
                    "GROUP BY Zentrum) ON Zentrum_Id = Zentrum;"

        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(statement)
        results = cursor.fetchall()
        conn.commit()
        conn.close()

        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def retrieve_monitoring_plan(self):

        statement = "SELECT tab1.Zentrum_Id, tab1.Land, tab1.Ort, tab1.Pruefer, tab1.Monitor, tab2.Gesamtanzahl as NP " \
                    "FROM " \
                    "(SELECT * FROM Zentren ORDER BY Zentrum_Id ASC) tab1 " \
                    "JOIN (SELECT Zentrum_Id, Gesamtanzahl " \
                    "FROM " \
                    "(SELECT Zentrum_Id FROM Zentren ORDER BY Zentrum_Id ASC) " \
                    "LEFT JOIN (SELECT Zentrum, SUM(Anzahl) as Gesamtanzahl " \
                    "FROM " \
                    "(SELECT Random_Woche_1.Zentrum, COUNT(Random_Woche_1.Zentrum) as Anzahl " \
                    "FROM Random_Woche_1 GROUP BY Random_Woche_1.Zentrum " \
                    "UNION SELECT Random_Woche_2.Zentrum, COUNT(Random_Woche_2.Zentrum) as Anzahl " \
                    "FROM Random_Woche_2 GROUP BY Random_Woche_2.Zentrum) " \
                    "GROUP BY Zentrum) ON Zentrum_Id = Zentrum) tab2 ON tab1.Zentrum_Id = tab2.Zentrum_Id;"

        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(statement)
        results = cursor.fetchall()
        conn.commit()
        conn.close()

        results_dict = [dict(ix) for ix in results]

        for item in results_dict:

            if item['NP']:
                if 0 < item['NP'] < 5:
                    visites = pd.date_range(start='6/1/2019', periods=5, freq='3M')
                    item['Monitor_Visite'] = visites.strftime("%Y-%m-%d").tolist()
                elif 4 < item['NP'] < 10:
                    visites = pd.date_range(start='6/1/2019', periods=5, freq='2M')
                    item['Monitor_Visite'] = visites.strftime("%Y-%m-%d").tolist()
                elif item['NP'] >= 10:
                    visites = pd.date_range(start='6/1/2019', periods=5, freq='M')
                    item['Monitor_Visite'] = visites.strftime("%Y-%m-%d").tolist()

        return json.dumps(results_dict)
