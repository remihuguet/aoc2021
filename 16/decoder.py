def read_input(input_file):
    with open(input_file, "r") as f:
        return [i for i in f.readlines()]


class BasePacket:
    def __init__(self, packet_str: str):
        self._packet_str = packet_str

    @property
    def version(self):
        return int(self._packet_str[:3], 2)

    @property
    def type(self):
        return int(self._packet_str[3:6], 2)


class Value(BasePacket):
    @property
    def value(self):
        pass


class Operator(BasePacket):
    @property
    def length_type(self):
        return int(self._packet_str[6:7])

    @property
    def sub_packets(self):
        packets = []
        if self.length_type == 0:
            _subpackets_len = int(self._packet_str[7:22], 2)
            _subpackets_str = self._packet_str[22 : 22 + _subpackets_len]
            total_length = 0
            print(_subpackets_str)
            while total_length < _subpackets_len:
                _subpackets_str = _subpackets_str[total_length:]
                print(_subpackets_str)
                if _subpackets_str[3:6] == "100":
                    # VALEUR
                    current_index = 11
                    bin_repre = _subpackets_str[:current_index]
                    while bin_repre[-5:].startswith("1"):
                        bin_repre += _subpackets_str[current_index : current_index + 5]
                        current_index += 5
                    packets.append(Value(bin_repre))
                    total_length += len(bin_repre)
                else:
                    pass
            else:
                # OPERATEUR
                pass
        return packets


def hex_to_binary_str(hex_str) -> str:
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def read_packet(packet_str: str) -> BasePacket:
    bin_repre = hex_to_binary_str(packet_str)

    type = bin_repre[3:6]
    if type == "100":
        return Value(bin_repre)
    else:
        return Operator(bin_repre)
