import argparse
from admin.mamphi import Mamphi


def populate_data(path_to_center_sheet, path_to_consent_sheet, path_to_rand_w1_sheet,
                  path_to_rand_w2_sheet, db_filename):

    mamphi = Mamphi(path_to_center_sheet=path_to_center_sheet, path_to_consent_sheet=path_to_consent_sheet,
                    path_to_rand_w1_sheet=path_to_rand_w1_sheet, path_to_rand_w2_sheet=path_to_rand_w2_sheet,
                    db_filename=db_filename)

    mamphi.create_center_table()
    mamphi.create_consent_table()
    mamphi.create_table_randomisation_week1()
    mamphi.create_table_randomisation_week2()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_center_sheet')
    parser.add_argument('--path_to_consent_sheet')
    parser.add_argument('--path_to_rand_w1_sheet')
    parser.add_argument('--path_to_rand_w2_sheet')
    parser.add_argument('--db_filename')
    args = parser.parse_args()

    path_to_center_sheet = args.path_to_center_sheet
    path_to_consent_sheet = args.path_to_consent_sheet
    path_to_rand_w1_sheet = args.path_to_rand_w1_sheet
    path_to_rand_w2_sheet = args.path_to_rand_w2_sheet
    db_filename = args.db_filename

    populate_data(path_to_center_sheet=path_to_center_sheet, path_to_consent_sheet=path_to_consent_sheet,
                  path_to_rand_w1_sheet=path_to_rand_w1_sheet, path_to_rand_w2_sheet=path_to_rand_w2_sheet,
                  db_filename=db_filename)


if __name__ == '__main__':
    main()
