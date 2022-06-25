def on_received_number(receivedNumber):
    global Recep
    Recep = receivedNumber
radio.on_received_number(on_received_number)

Recep = 0
radio.set_group(1)

def on_forever():
    if Recep == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
        basic.show_number(Recep)
    if Recep == 2:
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 100)
        basic.show_number(Recep)
    if Recep == 3:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
        basic.show_number(Recep)
basic.forever(on_forever)
