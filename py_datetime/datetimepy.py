import  datetime
import  time
import  json

date = datetime.date(2012,12,14)

print(date.year)
print(date.day)

print(datetime.date.today())
print(datetime.datetime.today())

a = datetime.datetime.today().strftime("%Y%m%d")
print(a)
print(type(a))

now = datetime.datetime.now()
then = datetime.datetime(2017,2,6)

delta = now - then

print(delta)
print(type(delta))

print(delta.days)

print(time.gmtime())

a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
print(a)



obj ={
    'name' : 'Do job',
}

obj['date'] = datetime.datetime.now()

def myconverter(d):
    if isinstance(d, datetime.datetime):
        return "{}-{}-{} {}:{}".format(d.year, d.month, d.day, d.hour, d.minute)

print(json.dumps(obj, default=myconverter))


# with open("data.json", "w") as write_file:
#     json.dump(obj, write_file, default=myconverter, indent=4)

data = None
with open("data.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
print(data['date'])
datetimeobj = datetime.datetime.strptime(data['date'],'%Y-%m-%d %H:%M')
print(datetimeobj)