# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 12:16:20 2018

@author: Shreya Somani
"""
import twilio
import twilio.rest
from twilio.rest import TwilioRestClient
accountSid = "AC919117896ba281096e735dc977f59735"
authToken = "99c756d17b6b9f213f6edc4fcdcd7a3a"
twilioClient = TwilioRestClient(accountSid, authToken)
myTwilioNumber = "+18327207612"
destCellPhone = "+918401091763"
myMessage = twilioClient.messages.create(body = "whatever", from_=myTwilioNumber, to=destCellPhone)