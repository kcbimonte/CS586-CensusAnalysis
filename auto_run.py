import census_df as cdf
import folder_paths as fpaths


# To dataframe
def to_json(path=fpaths.alabama_path):
    cdf.read(path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for state_path in fpaths.location_paths:
        state_name = state_path.split("/")[1]

        print("Processing", state_name)

        print("\tStarting to create dataframe")

        to_json(state_path)

        print(state_name, "Processed")
