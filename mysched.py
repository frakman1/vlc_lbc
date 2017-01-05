import schedule
import time
import datetime
import os

def job(t):

    today = datetime.datetime.now()
    
    print "I'm working...", today
    
    now = str(datetime.datetime.now())
    now = now.replace("-","_")
    now = now.replace(":","_")
    now =now.replace(" ", "")
    filename = now
    print filename
    cmd = "START /B vlc --intf dummy -vvv http://media-ice.musicradio.com/LBCLondonMP3Low --sout=#duplicate{dst=display,dst=file{mux=ps,dst="+filename+"lbc.mpg}} --run-time=14400 vlc://quit "

    print cmd
    os.system(cmd)

    return

def kill(t):
  print "killing task at %s" % datetime.datetime.now()
  cmd="Taskkill /IM vlc.exe /F"
  os.system(cmd)
  
  return



schedule.every().day.at("04:59").do(job,'It is JOB time!')
schedule.every().day.at("09:00").do(kill,'It is KILL time!')


while True:
    schedule.run_pending()
    time.sleep(1) # wait one second
    now = str(datetime.datetime.now())
    now = now.replace("-","_")
    now = now.replace(":","_")
    now =now.replace(" ", "")
    print now
    
