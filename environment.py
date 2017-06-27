from behave.log_capture import capture
from Common import CommonFunction

@capture
def before_all(context):
    context.DeviceSetting = CommonFunction.InitialDeviceSetting("Configuration/Config.ini")
    print("before_all")

@capture
def after_all(context):
    print("after_all")

@capture
def before_feature(context, feature):
    print("before_feature")

@capture
def after_feature(context, feature):
    print("after_feature")

@capture
def before_scenario(context, scenario):
    print("before_scenario")

@capture
def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
#    if scenario.status == "failed":
#        CommonFunction.SaveScreenAsFile(context)

@capture
def before_step(context, step):
    print("before_step")

@capture
def after_step(context, step):
    print("after_step")

@capture
def before_tag(context, tag):
    print("before_tag")

@capture
def after_tag(context, tag):
    print("after_tag")
