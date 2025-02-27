import os
import pandas as pd
import json


def read_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path, delimiter=';')
    elif file_path.endswith(".json"):
        try:
            return pd.read_json(file_path, lines=True)
        except ValueError:
            with open(file_path, 'r') as file:
                data = file.readlines()
            data = [json.loads(line) for line in data]
            return pd.DataFrame(data)
    return pd.DataFrame()


def determine_player_type(row):
    if row['runs'] > 500 and row['wickets'] > 50:
        return "All-Rounder"
    elif row['runs'] > 500 and row['wickets'] <= 50:
        return "Batsman"
    elif row['runs'] <= 500:
        return "Bowler"
    return None


def main():
    common_folder = "C:\\Users\\vkudke\\Downloads\\assignment\\assignment\\inputDataSet"
    customer1_folder = "C:\\Users\\vkudke\\Downloads\\assignment\\assignment\\OutPut_Dataset\\Customer1"
    customer2_folder = "C:\\Users\\vkudke\\Downloads\\assignment\\assignment\\OutPut_Dataset\\Customer2"
    temp_folder = "C:\\Users\\vkudke\\Downloads\\assignment\\assignment\\ResultFolder"

    file_names = ["testDataSet1.csv", "testDataSet2.json"]
    dataframes = [read_data(os.path.join(common_folder, file_name)) for file_name in file_names]

    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df['Player Type'] = merged_df.apply(determine_player_type, axis=1)

    # Fill NaN values in 'wickets' column with 0 and convert to integer
    merged_df['wickets'] = merged_df['wickets'].fillna(0).astype(int)

    # Filter the data based on the given conditions
    filtered_df = merged_df.dropna(subset=['runs', 'wickets'])
    filtered_df = filtered_df[(filtered_df['age'] <= 50) & (filtered_df['age'] >= 15)]

    odi_df = filtered_df[filtered_df['eventType'] == 'ODI']
    test_df = filtered_df[filtered_df['eventType'] == 'TEST']

    os.makedirs(customer1_folder, exist_ok=True)
    os.makedirs(customer2_folder, exist_ok=True)

    odi_output_file = os.path.join(customer2_folder, "odi.csv")
    odi_df.to_csv(odi_output_file, index=False, sep=';')

    test_output_file = os.path.join(customer1_folder, "test.csv")
    test_df.to_csv(test_output_file, index=False, sep=';')

    # Add 'Result' column
    def check_result(row):
        if pd.isna(row['runs']) or pd.isna(row['wickets']):
            return "FAIL"
        if row['age'] > 50 or row['age'] < 15:
            return "FAIL"
        return "PASS"

    merged_df['Result'] = merged_df.apply(check_result, axis=1)

    final_output_file = os.path.join(temp_folder, "test_result.csv")
    merged_df.to_csv(final_output_file, index=False)

    print(f"Final merged data saved to: {final_output_file}")
    print(f"ODI results saved to: {odi_output_file}")
    print(f"Test results saved to: {test_output_file}")


if __name__ == "__main__":
    main()
