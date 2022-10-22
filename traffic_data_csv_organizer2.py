import pandas as pd
from pathlib import Path


def same_point_data_frame_extractor(df):
    # new_df = pd.DataFrame()
    for index, row in df.iterrows():
        """
        The index in here is the row number in the edited data.
        The index in the row variable is the row number in the original data.
        """

        if index == 0:
            first_value = row["LATITUDE"]
            new_df = pd.DataFrame(row, columns=csv_data.columns)
            new_df = new_df.append(row)
            continue
        if index == 1:
            second_value = row["LATITUDE"]
            new_df = new_df.append(row)

        if abs(first_value - second_value) < 0.0000001:
            # print(new_df)
            new_df = new_df.append(row)

            second_value = first_value
            first_value = row["LATITUDE"]
            # print("\n")
    return new_df


csv_data = pd.read_csv("../data/original_data/traffic_density_202105.csv")

csv_data.sort_values(["LATITUDE"],
                    axis=0,
                    ascending=[False],
                    inplace=True)


csv_data.to_dict()
same_point_min_speed = 0
same_point_max_speed = 0
same_point_average_speed = 0
same_point_number_of_vehicles = 0

# new_df = csv_data[csv_data["LATITUDE"]==]

#DATE_TIME,LONGITUDE,LATITUDE,GEOHASH,MINIMUM_SPEED,MAXIMUM_SPEED,AVERAGE_SPEED,NUMBER_OF_VEHICLES

column_list = ["DATE_TIME",
               "LONGITUDE",
               "LATITUDE",
               "MINIMUM_SPEED",
               "MAXIMUM_SPEED",
               "AVERAGE_SPEED",
               "NUMBER_OF_VEHICLES"]

x = 0
# same_point_min_speed = pd.DataFrame()
# same_point_max_speed = pd.DataFrame()
# same_point_average_speed = pd.DataFrame()
# same_point_number_of_vehicles = pd.DataFrame()

# reset the index numbers from 0
csv_data = csv_data.reset_index()

same_df = pd.DataFrame(columns=csv_data.columns)
result_df = pd.DataFrame(columns=csv_data.columns)

first_value = 0
second_value = 0
for index_csv, row_csv in csv_data.iterrows():
    """
    The index in here is the row number in the edited data.
    The index in the row variable is the row number in the original data.
    """
    # same_df = same_point_data_frame_extractor(csv_data)
    # print(same_df)
    same_df = pd.DataFrame(columns=csv_data.columns)

    for index_same, row_same in same_df.iterrows():
        if index_same == 0:
            first_value = row_same["LATITUDE"]
            same_df = same_df.drop(same_df.index)
            # same_df = pd.DataFrame(row_same, columns=csv_data.columns)
            same_df = same_df.append(row_same)
            continue
        if index_same == 1:
            second_value = row_same["LATITUDE"]
            same_df = same_df.append(row_same)

        if abs(first_value - second_value) < 0.0000001:
            # print(new_df)
            same_df = same_df.append(row_same)

            second_value = first_value
            first_value = row_same["LATITUDE"]
            # print("\n")

    same_point_min_speed = \
        same_df['MINIMUM_SPEED'].values.mean()
    same_point_max_speed = \
        same_df['MAXIMUM_SPEED'].values.mean()
    same_point_average_speed = \
        same_df['AVERAGE_SPEED'].values.mean()
    same_point_number_of_vehicles = \
        same_df['NUMBER_OF_VEHICLES'].values.mean()
    dict_for_result = {
        "index": same_df["index"].values[0],
        "DATE_TIME": same_df['DATE_TIME'].values[index_csv],
        "LONGITUDE": same_df['LONGITUDE'].values[index_csv],
        "LATITUDE": same_df['LATITUDE'].values[index_csv],
        "GEOHASH": same_df['GEOHASH'].values[index_csv],
        "MINIMUM_SPEED": same_point_min_speed,
        "MAXIMUM_SPEED": same_point_max_speed,
        "AVERAGE_SPEED": same_point_average_speed,
        "NUMBER_OF_VEHICLES": same_point_number_of_vehicles
    }
    result_df = result_df.append(dict_for_result, ignore_index=True)
    print(result_df)

    # for index_same_df, row_same_df in same_df:
    #     new_df = pd.DataFrame(
    #         csv_data[csv_data["LATITUDE"] == csv_data['LATITUDE'].values[x]],
    #         columns=column_list)
    #     same_point_min_speed = \
    #         new_df['MINIMUM_SPEED'].values.mean()
    #     same_point_max_speed = \
    #         new_df['MAXIMUM_SPEED'].values.mean()
    #     same_point_average_speed = \
    #         new_df['AVERAGE_SPEED'].values.mean()
    #     same_point_number_of_vehicles = \
    #         new_df['NUMBER_OF_VEHICLES'].values.mean()
    #     dict_for_result = {
    #         "DATE_TIME": csv_data['DATE_TIME'].values[x],
    #         "LONGITUDE": csv_data['LONGITUDE'].values[x],
    #         "LATITUDE": csv_data['LATITUDE'].values[x],
    #         "MINIMUM_SPEED": same_point_min_speed,
    #         "MAXIMUM_SPEED": same_point_max_speed,
    #         "AVERAGE_SPEED": same_point_average_speed,
    #         "NUMBER_OF_VEHICLES": same_point_number_of_vehicles
    #     }


    # if index_csv == 0:
    #     first_value = row_csv["LATITUDE"]
    #     new_df = pd.DataFrame(row_csv, columns=csv_data.columns)
    #     new_df = new_df.append(row_csv)
    #     continue
    # if index_csv == 1:
    #     second_value = row_csv["LATITUDE"]
    #     new_df = new_df.append(row_csv)
    #
    # if abs(first_value - second_value) < 0.0000001:
    #
    #     print(new_df)
    #     new_df = new_df.append(row_csv)
    #
    #
    #     second_value = first_value
    #     first_value = row_csv["LATITUDE"]
    #     print("\n")

