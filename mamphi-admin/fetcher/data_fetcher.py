import sqlite3
import json
import pandas as pd


class MamphiDataFetcher:
    mamphi_db = ""

    def __init__(self, mamphi_db=mamphi_db):
        self.mamphi_db = mamphi_db

    def fetch_center(self):
        """
        The for fetching center items
        :return: center list as json
        """
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

    def get_center_german(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        statement = "SELECT * FROM Zentren WHERE Land = 'D'"

        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        # results_json = json.dumps([dict(ix) for ix in results])
        list_patient = json.dumps([dict(ix) for ix in results])
        # number_patient = len(list_patient)

        return list_patient

    def get_center_uk(self):
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

    def fetch_consent(self):
        """
        Method for fetching all informed consent
        :return: Informed consent as json file
        """
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

    def fetch_rand_w1(self):
        """

        :return: Items for the first randomization week as json
        """
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Random_Woche_1"
        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def fetch_rand_w2(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Random_Woche_2"
        cursor.execute(statement)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def update_zentren(self, center_json):
        """

        :rtype: object
        :param center_json: json string of the value to be inserted in the database
        """
        center = json.loads(center_json)

        # Compute center Id manually
        values = []
        if center['Land'] == "D":
            german_center = self.get_center_german()
            german_center = pd.read_json(german_center)
            zentrum_id = german_center['Zentrum_Id'].max() + 1
            values.append(zentrum_id)
        else:
            uk_center = self.get_center_uk()
            uk_center = pd.read_json(uk_center)
            zentrum_id = uk_center['Zentrum_Id'].max() + 1
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

    def update_consent(self, consent_json):

        consent_item = json.loads(consent_json)
        values = []
        # compute patient id manually
        consent_list = self.fetch_consent()
        consent_list = pd.read_json(consent_list)
        patient_id = consent_list['Patient_Id'].max() + 1

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

    def update_rand_w1(self, value):
        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "INSERT INTO Random_Week_1" + value
        try:
            cursor.execute(statement)

            conn.commit()
            print(cursor.rowcount, "record inserted.")

        except:
            conn.rollback()

        conn.close()

    def update_rand_w2(self, value):
        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "INSERT INTO Random_Woche_1" + value
        try:
            cursor.execute(statement)

            conn.commit()
            print(cursor.rowcount, "record inserted.")

        except:
            conn.rollback()

        conn.close()

    def fetch_missing_consent(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Informed_consent WHERE Einwilligung = 'nan' AND Datum != 'NaT'"
        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def fetch_incomplete_consent(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Informed_consent WHERE Einwilligung = 'nan'"
        cursor.execute(statement)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def fetch_consent_after_randomisation(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        statement = "SELECT * FROM Informed_consent WHERE Datum > '2019.06.03'"
        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()
        results_json = json.dumps([dict(ix) for ix in results])

        return results_json

    def get_number_of_patient_per_center_by_week_1(self):

        results = self.fetch_rand_w1()

        data = pd.read_json(results)

        number_patient_per_center = data.groupby(['Zentrum'])['Patient_Id'].count()

        center = [idx for idx in number_patient_per_center.index]
        number_of_patient = [value for value in number_patient_per_center.values]

        df = pd.DataFrame({'Zentrum': center, 'Number_Of_Patient': number_of_patient})
        weekly_list = df.to_json(orient='records')

        return weekly_list

    def get_number_patient_per_center_per_country_by_week_1(self):
        """

        :return: List of patient per center for both country as  JSON
        """
        weekly_list = self.get_number_of_patient_per_center_by_week_1()
        load_list = json.loads(weekly_list)
        list_german = []
        list_uk = []

        for el in load_list:
            if el['Zentrum'] < 200:
                list_german.append(el)
            else:
                list_uk.append(el)

        results = {'Germany': list_german, 'UK': list_uk}

        return json.dumps(results)

    def get_number_of_patient_per_center_by_week_2(self):

        results = self.fetch_rand_w2()

        data = pd.read_json(results)

        number_patient_per_center = data.groupby(['Zentrum'])['Patient_Id'].count()

        center = [idx for idx in number_patient_per_center.index]
        number_of_patient = [value for value in number_patient_per_center.values]

        df = pd.DataFrame({'Zentrum': center, 'Number_Of_Patient': number_of_patient})
        weekly_list = df.to_json(orient='records')

        return weekly_list

    def get_number_patient_per_center_per_country_by_week_2(self):
        """

        :return: Return list of patient per center in both country
        """
        weekly_list = self.get_number_of_patient_per_center_by_week_2()
        load_list = json.loads(weekly_list)
        list_german = []
        list_uk = []

        for el in load_list:
            if el['Zentrum'] < 200:
                list_german.append(el)
            else:
                list_uk.append(el)

        results = {'Germany': list_german, 'UK': list_uk}

        return json.dumps(results)

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

        print("An item has been removed")

    def retrieve_centres_with_number_of_patient(self):
        week1 = self.get_number_of_patient_per_center_by_week_1()
        week2 = self.get_number_of_patient_per_center_by_week_2()

        week1_df = pd.read_json(week1)
        week2_df = pd.read_json(week2)

        sum_weekly_records = pd.concat([week1_df, week2_df], ignore_index=True)
        records = sum_weekly_records.groupby(['Zentrum']).sum()

        centres = self.fetch_center()
        centres = pd.read_json(centres)
        centres['NP'] = 0

        for idx in records.index:
            centres.loc[centres['Zentrum_Id'] == idx, 'NP'] = records['Number_Of_Patient'][idx]

        return centres.to_json(orient='records')

    def retrieve_monitoring_plan(self):
        centres = self.retrieve_centres_with_number_of_patient()
        data = json.loads(centres)

        for item in data:
            if 0 < item['NP'] < 5:
                visites = pd.date_range(start='6/1/2019', periods=5, freq='3M')
                item['Monitor_Visite'] = visites.strftime("%Y-%m-%d").tolist()
            elif 4 < item['NP'] < 10:
                visites = pd.date_range(start='6/1/2019', periods=5, freq='2M')
                item['Monitor_Visite'] = visites.strftime("%Y-%m-%d").tolist()
            elif item['NP'] >= 10:
                visites = pd.date_range(start='6/1/2019', periods=5, freq='M')
                item['Monitor_Visite'] = visites.strftime("%Y-%m-%d").tolist()

        return json.dumps(data)
