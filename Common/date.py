from datetime import datetime
def Timestamp():
		time=datetime.now()
		return "[%s:%s:%s%s]" % (time.date(), time.hour,time.minute.time.second)

