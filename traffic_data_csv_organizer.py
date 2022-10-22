import pandas as pd
from pathlib import Path

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

x = 0
# df_number = str(x)
# df_name = "df_" + df_number
# df_list = []
# new_df = pd.DataFrame()

column_list = ["DATE_TIME",
               "LONGITUDE",
               "LATITUDE",
               "MINIMUM_SPEED",
               "MAXIMUM_SPEED",
               "AVERAGE_SPEED",
               "NUMBER_OF_VEHICLES"]

result_df = pd.DataFrame()

latitude_detector = {x: False}
while True:
    if abs(csv_data['LATITUDE'].values[x] - csv_data['LATITUDE'].values[x+1]) < 0.0000001:
        # MINIMUM_SPEED,MAXIMUM_SPEED,AVERAGE_SPEED,NUMBER_OF_VEHICLES
        if not list(latitude_detector.values())[0]:
            new_df = pd.DataFrame(
                csv_data[csv_data["LATITUDE"] == csv_data['LATITUDE'].values[x]],
                columns=column_list)
            same_point_min_speed = \
                new_df['MINIMUM_SPEED'].values.mean()
            same_point_max_speed = \
                new_df['MAXIMUM_SPEED'].values.mean()
            same_point_average_speed = \
                new_df['AVERAGE_SPEED'].values.mean()
            same_point_number_of_vehicles = \
                new_df['NUMBER_OF_VEHICLES'].values.mean()
            dict_for_result = {
                "DATE_TIME": csv_data['DATE_TIME'].values[x],
                "LONGITUDE": csv_data['LONGITUDE'].values[x],
                "LATITUDE": csv_data['LATITUDE'].values[x],
                "MINIMUM_SPEED": same_point_min_speed,
                "MAXIMUM_SPEED": same_point_max_speed,
                "AVERAGE_SPEED": same_point_average_speed,
                "NUMBER_OF_VEHICLES": same_point_number_of_vehicles
            }
            # result_df = pd.DataFrame(
            #     dict_for_result,
            #     columns=list(dict_for_result.keys()),
            #     index=pd.Index([x]))
            result_df = result_df.append(dict_for_result, ignore_index=True)

            print("result_df.index: ", result_df.index)
            print(result_df)
            latitude_detector = {csv_data['LATITUDE'].values[x]: True}

        x += 1
        # if x == len(csv_data)-50:
        #     result_df.to_csv('../data/editted_traffic_data.csv', index=False)
        #     print("csvvvvvvvvv")
        #     break

        if x%1000==1:
            print("x-if: ", x) # 121217 row count
    else:
        if list(latitude_detector.values())[0]:
            latitude_detector = {csv_data['LATITUDE'].values[x]: False}
        # if x%1000==1:
        #     print("x-else: ", x)
        # if  x > len(csv_data.index):
        #     print("dewam")
        print("x-else: ", x)
        x += 1



# filepath = Path('/home/ataparlar/itu/GEO403E - GIS Projects/Project/data/original_data/out1.csv')
# filepath.parent.mkdir(parents=True, exist_ok=True)
# result_df.to_csv(filepath)


