import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

class ValetApi():
    
    BASE_URL = "https://www.bankofcanada.ca/valet"

    def get_available_series(self):
        res = requests.get(f"{self.BASE_URL}/lists/series/csv")
        return res.text
    
    def get_available_groups(self):
        res = requests.get(f"{self.BASE_URL}/lists/groups/csv")
        return res.text

    def get_group_detail(self, group_name, format="csv"):
        """ Avaiable format: json, xml, csv"""
        res = requests.get(f"{self.BASE_URL}/groups/{group_namme}/csv")
        return res.text

    def get_serie_detail(self, serie_name, format="csv"):
        """ Avaiable format: json, xml, csv"""
        res = requests.get(f"{self.BASE_URL}/series/{serie_name}/csv")
        return res.text

    def get_serie_observations(self, serie_name, start_date=None, format="csv"):
        """ Avaiable format: json, xml, csv"""
        options = f"?start_date={start_date}" if start_date else ""
        res = requests.get(f"{self.BASE_URL}/observations/{serie_name}/csv{options}")
        return res.text

    def build_cvs_with_serie(self, serie_name, **kwargs):
        raw_res = self.get_serie_observations(serie_name, **kwargs)

        col1 = []
        col2 = []
        start_processing = False

        for line in raw_res.splitlines():
            if line.__contains__("OBSERVATIONS"):
                start_processing = True
                continue
            if not start_processing:
                continue
            elements = line.replace('"', '').split(",")
            print(elements)
            if len(elements) == 2:
                col1.append(elements[0])
                col2.append(elements[1])

        col1_name, col2_name = col1.pop(0), col2.pop(0)
        d = {col1_name: col1, col2_name: col2}
        df = pd.DataFrame(data=d)

        plt.plot(df[col1_name], df[col2_name])

        df.to_csv(f"data/CanBankValetApi/{col2_name}.csv")
        return df

valet = ValetApi()

print(valet.build_cvs_with_serie("V121820", start_date="2012-01-01"))
print(valet.get_serie_detail("V121820"))
