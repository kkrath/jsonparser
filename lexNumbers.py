import Constants as const
''' This program will read a number from a stream and
    after capturing the number return the rest of it'''
def lex_numbers(stream):
    json_number = ''

    number_characters = [str(d) for d in range(0,10)] + ['-','e','.']

    for c in stream:
        if c in number_characters:
            json_number += c
        else:
            break
    rest = stream[len(json_number):]

    if not len(json_number):
        return None,stream
    if '.' in json_number:
        return float(json_number),rest
    
    return int(json_number),rest




