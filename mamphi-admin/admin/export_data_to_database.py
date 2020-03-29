from admin.data import populate_data


class MamphiData:

    db_filename = 'data/mamphi.db'
    path_to_center_sheet = 'data/sheets/Mamphi_Zentren.xlsx'
    path_to_consent_sheet = 'data/sheets/Mamphi_Informed_consent.xlsx'
    path_to_rand_w1_sheet = 'data/sheets/Mamphi_Randomisierung_Woche_1.xlsx'
    path_to_rand_w2_sheet = 'data/sheets/Mamphi_Randomisierung_Woche_2.xlsx'

    def __init__(self):
        self.db_filename = self.db_filename
        self.path_to_center_sheet = self.path_to_center_sheet
        self.path_to_consent_sheet = self.path_to_consent_sheet
        self.path_to_rand_w2_sheet = self.path_to_rand_w2_sheet
        self.path_to_rand_w1_sheet = self.path_to_rand_w1_sheet

    def export_data(self):
        populate_data(path_to_center_sheet=self.path_to_center_sheet,
                      path_to_consent_sheet=self.path_to_consent_sheet,
                      path_to_rand_w1_sheet=self.path_to_rand_w1_sheet,
                      path_to_rand_w2_sheet=self.path_to_rand_w2_sheet,
                      db_filename=self.db_filename)


if __name__ == '__main__':
    data = MamphiData()
    data.export_data()
