import sqlite3
import json


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

    def fetch_rand_w1(self):
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

    def update_zentren(self, value):
        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "INSERT INTO Zentren VALUES" + value
        try:
            cursor.execute(statement)

            conn.commit()
            print(cursor.rowcount, "record inserted.")

        except:
            conn.rollback()

        conn.close()

    def update_consent(self, value):
        conn = sqlite3.connect(self.mamphi_db)
        cursor = conn.cursor()
        statement = "INSERT INTO Informed_consent VALUES" + value
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
        statement = "INSERT INTO Random_Week_1" + value
        try:
            cursor.execute(statement)

            conn.commit()
            print(cursor.rowcount, "record inserted.")

        except:
            conn.rollback()

        conn.close()

    def get_weekly_list_german(self):
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

    def get_weekly_list_uk(self):
        conn = sqlite3.connect(self.mamphi_db)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        statement = "SELECT * FROM Zentren WHERE Land = 'UK'"
        cursor.execute(statement)
        results = cursor.fetchall()

        conn.commit()
        conn.close()

        list_patient = json.dumps([dict(ix) for ix in results])
        # number_patient = len(list_patient)
        return list_patient

    def get_weekly_list(self, land):

        if land == "Germany":
            conn = sqlite3.connect(self.mamphi_db)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            statement = "SELECT * FROM Zentren WHERE Land = 'D'"

            cursor.execute(statement)
            results = cursor.fetchall()

            conn.commit()
            conn.close()
            list_patient = json.dumps([dict(ix) for ix in results])
            # number_patient = len(list_patient)
            return list_patient

        elif land == "UK":
            conn = sqlite3.connect(self.mamphi_db)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            statement = "SELECT * FROM Zentren WHERE Land = 'UK'"
            cursor.execute(statement)
            results = cursor.fetchall()

            conn.commit()
            conn.close()
            list_patient = json.dumps([dict(ix) for ix in results])
            # number_patient = len(list_patient)
            return list_patient

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
