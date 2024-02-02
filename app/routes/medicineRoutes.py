import numpy as np
import pandas as pd

from app import app
from flask import Flask, render_template, url_for, request, redirect, jsonify
def load_data(file_path):
    columns = ['productid', 'productndc', 'producttypename', 'proprietaryname',
               'proprietarynamesuffix', 'nonproprietaryname', 'dosageformname',
               'routename', 'startmarketingdate', 'endmarketingdate',
               'marketingcategoryname', 'applicationnumber', 'labelername',
               'substancename', 'active_numerator_strength', 'active_ingred_unit',
               'pharm_classes', 'deaschedule', 'ndc_exclude_flag',
               'listing_record_certified_through']

    data = np.genfromtxt(file_path, delimiter='\t', dtype=None, names=columns, encoding='latin-1')
    df = pd.DataFrame(data)

    # Generate random prices between $10 and $1000
    random_prices = np.random.uniform(10, 1000, size=len(df))

    # Add a new column 'price' to the DataFrame
    df['price'] = random_prices

    return df

df = load_data('C:\\Users\\Yashwant Chavan\\Medicine_Backend\\Medicine_API\\dataset\\product.txt')



@app.route("/api/ProprietaryName/<string:query>")
#Get Medicine with Proprietary Name
def get_rows_by_partial_proprietaryname_json(query):
    result_df = df[df['proprietaryname'].str.contains(query, case=False, na=False)]
    return result_df.to_json(orient='records')

@app.route("/api/SubstanceName/<string:query>")
#Get Medicine with Substance Name
def get_rows_by_partial_substancename_json(query):
    result_df = df[df['substancename'].str.contains(query, case=False, na=False)]
    return result_df.to_json(orient='records')

@app.route("/api/NonProprietaryName/<string:query>")
#Get Medicine with Non Proprietary Name
def get_rows_by_partial_nonproprietaryname_json(query):
    result_df = df[df['nonproprietaryname'].str.contains(query, case=False, na=False)]
    return result_df.to_json(orient='records')

@app.route("/api/DiseaseName/<string:query>")
#Get Medicine with Disease Name
def get_rows_by_partial_proprietarynamesuffix_json(query):
  result_df = df[df['proprietarynamesuffix'].str.contains(query, case=False, na=False)]
  return result_df.to_json(orient='records')