radio.onDataPacketReceived(({receivedString}) => {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.A, () => {
    radio.sendString("A")
})
input.onButtonPressed(Button.B, () => {
    radio.sendString("B")
})
radio.setGroup(0)

