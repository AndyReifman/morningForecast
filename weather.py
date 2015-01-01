import smtplib
import urllib.request, json

##This block is entirely for sending the messages
username = 'morningForecast@gmail.com'
password = 'Raistlin3'
=======
##This block is entirely for sending the messages
username = 'morningForecast@gmail.com'
password = 'morningWeather'
>>>>>>> Finally updating with a mostly finished project
fromaddr = 'morningForecast@gmail.com'
toaddrs = '2077518722@vzwpix.com'
#'2077518722@vzwpix.com'
def send_text(msg):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

#Here starts everything for the weather part!
def getForecast():
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?cnt=7&units=meteric&mode=json&q=Albany,ny"
    req = urllib.request.Request(url)
    response= urllib.request.urlopen(req)
    return json.loads(response.read().decode("UTF-8"))

forecast = getForecast()
#print("Forecast for Albany", forecast['city']['country'])

=======
forecast = getForecast()
#print("Forecast for Albany", forecast['city']['country'])
msg = ""
goodString = "Good morning. "
msg = msg + goodString
day = forecast['list'][0]
minTemp = round(day['temp']['min']-273.15,1)
maxTemp = round(day['temp']['max']-273.15,1)
temp = round(day['temp']['day']-273.15,1)
temp = (temp*9/5) + 32
minTemp = (minTemp*9/5) + 32
maxTemp = (maxTemp*9/5) + 32
msg = msg + "The min temp today is "+str(minTemp) +"\n"
msg = msg + "The max temp today is "+str(maxTemp)+"\n"
msg  = msg + "The temp right now is " + str(temp)+ "\n"
msg = msg + "The temp right now is " + str(temp)+ "\n"
>>>>>>> Finally updating with a mostly finished project
if maxTemp < 45:
    tempString = " It\'s pretty cold out, you'll want a jacket\n"
    msg = msg + tempString
wind = day['speed']
if wind > 10 and maxTemp < 50 and maxTemp > 45:
    windString = " It\'s pretty windy out, you'll want a jacket\n"
    msg = msg + windString
try:
    rain = day['rain']
    if rain > 1:
        rainString = "There is a good chance of rain today, you may want an umbrella"
        msg = msg + rainString
except KeyError:
    pass
try:
    snow = day['snow']
    snowString = " It's going to snow today. Enjoy."
    msg = msg + snowString
except KeyError:
    pass

send_text(msg)

