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

'''This program will look for a string in the stream else
    returns the whole stream back'''
def lex_string(stream):
    json_string = ''
    if stream[0] == const.DOUBLE_QUOTE:
        ''' if the first character is a quote then definitely a string follows
            and we will discard the quote and move ahead with capturing th string
            by running through a loop until we get one unquote/quote '''
        stream = stream[1:]
    else:
        # else we return empty character and the stream back to the calling method
        return json_string,stream

        # we will loop through to cature all strings until we find unquote/quote
    for c in stream:
        if c == const.DOUBLE_UNQUOTE:
            return json_string,stream[len(json_string)+1:]
        else:
            json_string += c

'''This program is a lexer which will take json stream and
    tokenize all the elements and create a liner list'''

def lex(stream):
    tokens = []

    while len(stream):
        json_string,stream = lex_string(stream)
        if json_string is not '':
            tokens.append(json_string)
            continue

        json_number,stream = lex_numbers(stream)
        if json_number is not None:
            tokens.append(json_number)
            continue

        if stream[0] in const.JSON_WHITESPACE:
            stream = stream[1:]

        elif stream[0] in const.JSON_SYNTAX:
            tokens.append(stream[0])
            stream = stream[1:]
        else:
            raise Exception('Unexpected character: {}'.format(stream[0]))
    return tokens

print(lex("{\"name\":\"Khitish\",\"age\":25,\"phone\":\"+919234567891\"}"))