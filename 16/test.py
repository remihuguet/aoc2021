import decoder

test_input = "16/test_input.txt"


inputs = [
    "D2FE28",
    "38006F45291200",
    "EE00D40C823060",
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
]


def test_hex_to_binary_str():
    assert decoder.hex_to_binary_str("D2FE28") == "110100101111111000101000"
    assert (
        decoder.hex_to_binary_str("38006F45291200")
        == "00111000000000000110111101000101001010010001001000000000"
    )
    assert (
        decoder.hex_to_binary_str("EE00D40C823060")
        == "11101110000000001101010000001100100000100011000001100000"
    )


def test_decode_header():
    packet = decoder.read_packet(inputs[0])
    assert isinstance(packet, decoder.Value)
    assert packet.version == 6
    assert packet.type == 4

    packet = decoder.read_packet(inputs[1])
    assert isinstance(packet, decoder.Operator)
    assert packet.version == 1
    assert packet.type == 6
    assert packet.length_type == 0
    assert len(packet.sub_packets) == 2
    assert isinstance(packet.sub_packets[0], decoder.Value)
    assert isinstance(packet.sub_packets[1], decoder.Value)

    packet = decoder.read_packet(inputs[2])
    assert isinstance(packet, decoder.Operator)
    assert packet.version == 7
    assert packet.type == 3
    assert packet.length_type == 1
