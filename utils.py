from datetime import datetime, timedelta

'''
1. Sleep Onset
'''
def sleep_onset_workdays(SPrepw, SLatw):
    SOw = SPrepw + SLatw
    return SOw

def sleep_onset_freedays(SPrepf, SLatf):
    SOf = SPrepf + SLatf
    return SOf

def sleep_onset(SOw, SPrepw, SLatw):
    return SOw + SPrepw + SLatw

'''
2. Sleep Duration
'''
def sleep_duration_workdays(SEw, SOw):
    SDw = SEw - SOw
    return SDw

def sleep_duration_freedays(SEf, SOf):
    SDf = SEf - SOf
    return SDf

'''
3. Total Time In Bed 
'''
def total_time_in_bed_workdays(GUw, BTw):
    TBTw = GUw - BTw
    return TBTw

def total_time_in_bed_freedays(GUf, BTf):
    TBTf = GUf - BTf
    return TBTf

'''
4. Mid Sleep
'''
def midsleep_workdays(SOw, SDw):
    MSW = SOw + SDw/2
    return MSW

def midsleep_freedays(SOf, SDf):
    MSF = SOf + SDf/2
    return MSF

'''
5. Weekly Sleep Duration
'''
def weekly_sleep_duration(SDw, WD, SDf):
    SDweek = (SDw * WD + SDf * 2)/7
    return SDweek

'''
6. Chronotype
'''
def chronotype(SDf, SDw, MSF):
    # only computable is alarm = No
    if SDf <= SDw:
        MSFsc = MSF
    elif SDf > SDw:
        MSFsc = MSF - (SDf - SDweek)/2
    return MSFsc

'''
7. Social Jet Lag
'''

def relative_social_jet_lag(MSF, MSW):
    SJLrel = MSF - MSW
    return SJLrel