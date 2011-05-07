class GRLEReader:
    """Reads a RLE file formatted for Golly.

    Currently, it ignores any metadata associated with the file."""

    def __init__(self):
        pass

    def read_rle(self, rle):
        """Read RLE data into a stream of tokens.
        
        rle should be a file or file like object."""
        output = []

        for line in rle:
            if line[0] == 'x':
                continue # TODO parse this line.
            if line[0] == '#':
                continue
            output.extend(self.parse_line(line))
            if type(output[-1]) == EOFToken:
                break

        return output

    def parse_line(self, line):
        """Parse a RLE line into a series of tokens.
        
        A series like 3b$ would result in three 'b' StateTokens and one '$'"""
        output = []
        number_str = ''
        for char in line:
            if char in ['$', 'b', 'o']:
                if number_str != '':
                    for x in range(0, int(number_str)):
                        output.append(StateToken(char))
                    number_str = ''
                else:
                    output.append(StateToken(char))
            elif char.isdigit():
                number_str += char
            elif char == '!':
                output.append(EOFToken())
                break

        return output


class Token:
    def __init__(self, value):
        self.value = value


class StateToken(Token): pass


class EOFToken(Token):
    def __init__(self):
        self.value = ''
