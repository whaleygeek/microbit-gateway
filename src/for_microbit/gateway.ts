let data = ""
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), () => {
    data = serial.readLine()
    radio.sendString(data)
})
radio.onDataPacketReceived(({receivedString}) => {
    serial.writeLine(receivedString)
})
radio.setGroup(0)
