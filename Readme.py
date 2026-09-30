Data_of_Human = {}
Data_of_Enviorment= {}
Data_of_Enviorment["Temperature"] = float(input("Enter Temperature ="))
Data_of_Human["Age"] = int(input("Enter Age ="))
Data_of_Human["Occupation"] = input("Enter occupation = ")
Data_of_Enviorment["AQI"]  = float(input("Enter AQI ="))
Data_of_Human["Human Condition"] = input("Enter Human Disease if any =")
Data_of_Enviorment["Humidity"] = int(input("Enter Humidity ="))
Data_of_Enviorment["Wind Speed"] = float(input("Enter wind speed = "))
Data_of_Enviorment["UV Index"] = int(input("Enter UI index ="))
print(Data_of_Enviorment)
print(Data_of_Human)


# Temperature
def temperature(temp):
    if temp < 15:
        return 1
    elif temp <= 30:
        return  0
    else:
        return  2
#Humidity 
def humidity(hum):
    if hum < 30:
        return 1
    elif hum>= 30 and hum <= 60:
        return 0
    elif hum> 60 and hum <= 80:
        return 1  
    else: 
        return 2
#wind speed
def wind_speed(ws):
    if  0<=ws<= 15:
        return 0
    elif ws <= 30:
        return 1
    else:
        return 2
#AQI
def AQI(aqi):
    if  0<=aqi<=50:
        return 0
    elif aqi <= 100:
        return 1
    else:
        return  2
#UV index
def UV_Index(uv):
    if 0<=uv<=2:
        return 0
    elif  uv <= 5:
        return 1
    elif uv <= 7:
        return 2
    else:
        return 2
# Age
def age(a):
    if 0<=a<=12:
        return 1
    elif a<=59:
        return 0
    else:
        return 1
# occupation
def occupation(oc):
    if oc == "Indoor":
        return 0
    elif oc == "Mixed":
        return 1
    elif oc == "Outdoor":
        return 2
    else:
        return 0
#  Health condition         
def health_condition(hc):
    if hc == "nil":
        return 0
    elif hc == "Asthma":
        return 2
    elif hc == "respiratory related problems":
        return 2
    else:
        return 1
temp_s = temperature(Data_of_Enviorment["Temperature"])
hum_s = humidity(Data_of_Enviorment["Humidity"])
ws_s = wind_speed(Data_of_Enviorment["Wind Speed"])
aqi_s = AQI(Data_of_Enviorment["AQI"])
uv_s = UV_Index(Data_of_Enviorment["UV Index"])
age_s = age(Data_of_Human["Age"])
occupation_s = occupation(Data_of_Human["Occupation"])
health_s = health_condition(Data_of_Human["Human Condition"])

    
risk_Data_of_Human = {}
risk_Data_of_Enviorment= {}
risk_Data_of_Enviorment["Temperature"] = temp_s
risk_Data_of_Human["Age"] = age_s
risk_Data_of_Human["Occupation"] = occupation_s
risk_Data_of_Enviorment["AQI"]  = aqi_s
risk_Data_of_Human["Human Condition"] = health_s
risk_Data_of_Enviorment["Humidity"] = hum_s
risk_Data_of_Enviorment["Wind Speed"] = ws_s
risk_Data_of_Enviorment["UV Index"] = uv_s
print(risk_Data_of_Enviorment)
print(risk_Data_of_Human)




total_risk = (aqi_s*4) + (temp_s*3) + (health_s*4) + (hum_s*2) + (uv_s*2) + (ws_s) + (occupation_s) + (age_s)

result = {}
result["Total risk score"] = total_risk


if  0<=total_risk<=8:
    result["Risk"] = "Low"
elif total_risk<=18:
    result["Risk"] = "Moderate"     
else:
    result["Risk"] = "High"

print(result)
  