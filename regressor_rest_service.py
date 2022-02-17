import pickle

from flask import Flask,request
import math


regressor_spyder = pickle.load(open('classifier.pickle','rb'))

app = Flask(__name__)

@app.route('/model',methods=['POST'])
def hello_world():
    request_data = request.get_json(force=True)
    overall_qual = request_data['OverallQual']
    exter_qual = request_data['ExterQual']
    bsmt_qual = request_data['BsmtQual']
    total_bsmt_sf = request_data['TotalBsmtSF']
    first_floor_sf = request_data['1stFlrSF']
    gr_liv_area = request_data['GrLivArea']
    full_bath = request_data['FullBath']
    kitchen_qual = request_data['KitchenQual']
    garage_cars = request_data['GarageCars']
    garage_area = request_data['GarageArea']
    prediction = regressor_spyder.predict([[overall_qual,exter_qual,bsmt_qual,total_bsmt_sf,first_floor_sf,gr_liv_area,full_bath,kitchen_qual,garage_cars,garage_area]])
    return "The predicted house price is {}".format(prediction)

if __name__ == "__main__":
    app.run(port=8000,debug=True)