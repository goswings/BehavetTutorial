from mailer import Message
import smtplib
import codecs
import configparser
import ast
import os, time

CONFIGPARSER = configparser.ConfigParser()

class MailConfig():
    def __init__(self,Config):
        CONFIGPARSER.read(Config)
        self.SUBJECT = CONFIGPARSER.get("Mail","SUBJECT")
        self.SENDOR = CONFIGPARSER.get("Mail","SENDOR")
        self.RECEIEVERS = CONFIGPARSER.get("Mail","RECEIEVERS")
        self.SMTPSETTING = CONFIGPARSER.get("Mail","SMTPSETTING")

def SendMail(MailConfig,Content,filename=None):
    message = Message(From=MailConfig.SENDOR,To=MailConfig.RECEIEVERS,charset="utf-8")
    message.Subject = MailConfig.SUBJECT
    message.Html = Content
    if filename != None:
        message.attach(filename)
    server = smtplib.SMTP(MailConfig.SMTPSETTING)
    server.starttls()
    server.sendmail(MailConfig.SENDOR, MailConfig.RECEIEVERS.split(";"), message.as_string())
    server.quit()

def GetFileContentToAll(filename):
    with codecs.open(filename, encoding='utf-8' , errors='ignore') as file:
        return file.read()

def GetFileContentToList(filename):
    with codecs.open(filename, encoding='utf-8' , errors='ignore') as file:
        return file.read().splitlines()

class DeviceSettingConfig():
    def __init__(self):
        self.Chrome = "Chrome"

def InitialDeviceSetting(config):
    InitConfig = configparser.ConfigParser()
    InitConfig.read(config)
    DeviceSetting = DeviceSettingConfig()
    for Device, Setting in InitConfig.items("Device"):
        setattr(DeviceSetting,Device,ast.literal_eval(Setting))
    return DeviceSetting

#def SaveScreenAsFile(context):
#        logtime=str(time.time())+".png"
#        context.browser.get_screenshot_as_file(os.getcwd()+"/Screen/"+logtime)
