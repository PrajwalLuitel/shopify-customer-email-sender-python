import pandas as pd
import json
import requests

def get_dataframe(url):
    """
    Gets the data in json format from the API and returns the pandas dataframe.
    """
    df1 = pd.DataFrame()
    # GET / admin/api/2020-10/customers/count.json
    JSON_customers = requests.get(
        url)
    if 'json' in JSON_customers.headers.get('Content-Type'):
        content = json.dumps(JSON_customers.json(), indent=4, sort_keys=True)
        nested = json.loads(content)
        customers = pd.json_normalize(nested["customers"])
        df1 = pd.DataFrame(customers, columns=[
                           'id', 'first_name', 'last_name', 'email', 'orders_count', 'total_spent'])
    else:
        print("Response content is not in JSON format")
        js = 'spam'

    return df1

# Reads the html template and returns the content as string
def read_html_template(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

# Reads the text template file and returns the content as string
def read_text_template(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data