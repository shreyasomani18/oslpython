# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:49:52 2018

@author: iis
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:47:41 2018

@author: iis
"""

import datetime
import json
import urllib.request
from twilio.rest import Client



def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def url_builder(city_id):
    user_api = '94e977e317edd225d936f1715714b224'  # Obtain yours form: http://openweathermap.org/
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    return raw_api_dict


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')
    
    var='---------------------------------------'
    var1='Current weather in: {}, {}:'.format(data['city'], data['country'])
    #data['temp'], m_symbol, data['sky'])
    var2='Temperature: {}degrees Celsius, Sky: {}'.format(data['temp'], data['sky'])
    var3='MAX: {}, Min: {}'.format(data['temp_max'], data['temp_min'])
    var4=''
    var5='Wind Speed: {}'.format(data['wind'])
    var6='Humidity: {}'.format(data['humidity'])
    var7='Cloud: {}'.format(data['cloudiness'])
    var8='Pressure: {}'.format(data['pressure'])
    var9='Sunrise at: {}'.format(data['sunrise'])
    var10='Sunset at: {}'.format(data['sunset'])
    var11=''
    var12='Last update from the server: {}'.format(data['dt'])
    var13='---------------------------------------'
    
    #print(var1)

    client = Client("AC919117896ba281096e735dc977f59735", "99c756d17b6b9f213f6edc4fcdcd7a3a")
    client.messages.create(to="+918401091763", from_="+18327207612", body=var1+var2+var3+var5+var6+var7)
#+var5+var6+var7+var8+var9+var10+var11+var12+var13

if __name__ == '__main__':
    try:
        data_output(data_organizer(data_fetch(url_builder(1279233))))
    except IOError:
        print('no internet')