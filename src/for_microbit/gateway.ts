radio.onDataPacketReceived(({receivedString}) => {
    serial.writeLine(receivedString)
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), () => {
    radio.sendString(serial.readLine())
})
radio.setGroup(0)

