radio.onReceivedNumber(function (receivedNumber) {
    Recep = receivedNumber
})
let Recep = 0
radio.setGroup(1)
basic.forever(function () {
    if (Recep == 1) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 100)
        basic.showNumber(Recep)
    }
    if (Recep == 2) {
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 100)
        basic.showNumber(Recep)
    }
    if (Recep == 3) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 100)
        basic.showNumber(Recep)
    }
})
