import pandas as pd
import sqlite3


class Mamphi:

    def __init__(self, path_to_center_sheet, path_to_consent_sheet, path_to_rand_w1_sheet, path_to_rand_w2_sheet,
                 db_filename):
        self.path_to_center_sheet = path_to_center_sheet
        self.path_to_consent_sheet = path_to_consent_sheet
        self.path_to_rand_w1_sheet = path_to_rand_w1_sheet
        self.path_to_rand_w2_sheet = path_to_rand_w2_sheet
        self.db_filename = db_filename

    def create_center_table(self):
        center_data = pd.read_excel(self.path_to_center_sheet)

        # Create Table Center
        sql_center_table = """ CREATE TABLE IF NOT EXISTS Zentren(
                                    Zentrum_Id smallint,
                                    Land varchar(255),
                                    Ort varchar(255),
                                    Pruefer varchar(255),
                                    Monitor varchar(255)
                                    )"""

        # create connection to database
        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()
        cursor.execute(sql_center_table)

        # Create rows of value
        rows = center_data.values

        for i in range(len(rows)):
            value = "({},'{}','{}','{}','{}')".format(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4])
            statement = "INSERT INTO Zentren VALUES" + value
            try:
                cursor.execute(statement)

                conn.commit()
                print(cursor.rowcount, "record inserted.")

            except:
                conn.rollback()

        conn.close()

        print('Successfully created database table center')

    def create_consent_table(self):

        consent_data = pd.read_excel(self.path_to_consent_sheet)

        connection = sqlite3.connect(self.db_filename)

        # prepare a cursor object
        cursor = connection.cursor()

        # Create Table Informed_consent
        patient_table_statement = """ CREATE TABLE IF NOT EXISTS Informed_consent(
                                    Patient_Id smallint,
                                    Zentrum smallint,
                                    Einwilligung varchar(255),
                                    Datum date
                                    )"""

        # print(patient_table_statement)
        cursor.execute(patient_table_statement)

        # Create rows of values
        rows = consent_data.values

        for i in range(len(rows)):
            values = "({},{},'{}','{}')".format(rows[i][0], rows[i][1], rows[i][2], rows[i][3])
            insert_statement = "INSERT INTO Informed_consent VALUES" + values

            try:
                # Execute SQL command
                cursor.execute(insert_statement)
                # Commit the change
                connection.commit()
                print(cursor.rowcount, "record inserted.")

            except:
                # Rollback in case there is any error
                connection.rollback()
            # if i !=len(rows)-2:
            # values_p +=','

        connection.close()
        print('Successfully created database table Informed_consent')

    def create_table_randomisation_week1(self):
        """

        :rtype: object
        """
        random_week1_data = pd.read_excel(self.path_to_rand_w1_sheet)

        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()

        querie_create_table_rand_w1 = """CREATE TABLE IF NOT EXISTS Random_Woche_1(
                                    Patient_Id smallint,
                                    Zentrum smallint,
                                    Behandlungsarm varchar(255),
                                    Datum date
                                  )"""

        cursor.execute(querie_create_table_rand_w1)

        rows = random_week1_data.values

        for i in range(len(rows)):
            value = "({},{},'{}','{}')".format(rows[i][0], rows[i][1], rows[i][2], rows[i][3])

            sql = "INSERT INTO Random_Woche_1 VALUES" + value

            try:
                # Execute SQL Command
                cursor.execute(sql)
                # Commit changes
                conn.commit()
                print(cursor.rowcount, "record inserted.")
            except:
                conn.rollback()
            # if i != len(rows)-2:
            # values += ","

        conn.close()

        print('Successfully created database table random_Week_1')

    def create_table_randomisation_week2(self):

        random_week2_data = pd.read_excel(self.path_to_rand_w2_sheet)

        conn = sqlite3.connect(self.db_filename)
        cursor = conn.cursor()

        querie_create_table_rand_w2 = """CREATE TABLE IF NOT EXISTS Random_Woche_2(
                                    Patient_Id smallint,
                                    Zentrum smallint,
                                    Behandlungsarm varchar(255),
                                    Datum date
                                  )"""

        cursor.execute(querie_create_table_rand_w2)

        rows = random_week2_data.values

        for i in range(len(rows)):
            value = "({},{},'{}','{}')".format(rows[i][0], rows[i][1], rows[i][2], rows[i][3])

            sql = "INSERT INTO Random_Woche_2 VALUES" + value

            try:
                # Execute SQL Command
                cursor.execute(sql)
                # Commit changes
                conn.commit()
                print(cursor.rowcount, "record inserted.")
            except:
                conn.rollback()
            # if i != len(rows)-2:
            # values += ","

        conn.close()

        print('Successfully created database table Random_Week_2')
