import time
import pinproc

proc = pinproc.PinPROC(1)
proc.reset(1)

for x in range(255):
    proc.switch_update_rule(x, 'closed_nondebounced',
                           {'notifyHost': True, 'reloadActive': False}, [],
                            False)
    proc.switch_update_rule(x, 'open_nondebounced',
                            {'notifyHost': True, 'reloadActive': False}, [],
                            False)

while True:

    for event in proc.get_events():
        print(event)
        event_type = event['type']
        event_value = event['value']

        if event_type == pinproc.EventTypeSwitchClosedDebounced:
            print('+{}'.format(event_value))
        elif event_type == pinproc.EventTypeSwitchOpenDebounced:
            print('-{}'.format(event_value))

    proc.watchdog_tickle()
    proc.flush()
    time.sleep(.01)