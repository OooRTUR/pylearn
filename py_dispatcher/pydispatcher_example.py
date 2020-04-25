from pydispatch import dispatcher

SIGNAL = 'first-singal'

def handle_event(sender):
    print("signal was sent by ", sender)

dispatcher.connect(handle_event, signal=SIGNAL, sender=dispatcher.Any)

first_sender = object()
second_sender = {}

def main():
    dispatcher.send(signal=SIGNAL, sender=first_sender)
    dispatcher.send(signal=SIGNAL, sender=second_sender)

if __name__ == '__main__':
    main()