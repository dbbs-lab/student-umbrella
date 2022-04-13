import pandas as pd

data = pd.read_csv("datasets/immigration.csv")

def get_total_df(df):
    totals = df["AreaName"].str.contains("Total")
    total_rows = df[totals]
    years = total_rows.columns[4:-1]
    immi_data = total_rows[years].to_numpy().astype(float)
    region_names = total_rows["AreaName"]
    immi_dict = {region: immi_data[i, :] for i, region in enumerate(region_names)}
    total_df = pd.DataFrame(immi_dict)
    total_df["years"] = years
    return total_df

df = get_total_df(data)
