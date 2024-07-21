from .get_data_by_month import *

def get_oil_elec_data():
    cars = list(get_cars_by_month('202406'))
    oilData = []
    electricData = []
    for i in cars:
        if i.energyType == '汽油':
            oilData.append([i.model, i.sales,i.energyType])
        elif i.energyType == '纯电动':
            electricData.append([i.model, i.sales,i.energyType])
    oilData = oilData[:10]
    electricData = electricData[:10]
    return(oilData,electricData)