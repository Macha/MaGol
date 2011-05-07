
class GRLEReader:
    def __init__(self):
        pass

    def read_rle(self, rle_data):
        output = []

        for line in rle_data:
            if line[0] == 'x':
                continue # TODO parse this line.
            if line[0] == '#':
                continue
            output.extend(self.parse(line))
            if type(output[-1]) == EOFToken:
                break

        return output

    def parse(self, line):
        output = []
        number = ''
        for char in line:
            if char in ['$', 'b', 'o']:
                if number != '':
                    for x in range(0, int(number)):
                        output.append(StateToken(char))
                    number = ''
                else:
                    output.append(StateToken(char))
            elif char.isdigit():
                number += char
            elif char == '!':
                break

        output.append(EOFToken())
        return output

class Token:
    def __init__(self, value):
        self.value = value


class StateToken(Token): pass


class EOFToken(Token):
    def __init__(self):
        self.value = ''
