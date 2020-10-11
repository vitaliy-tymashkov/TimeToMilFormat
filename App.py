'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00 AM on a 12-hour clock and 00:00:00 on a 24-hour clock.
      Noon is 12:00:00 PM on 12-hour clock and 12:00:00 on 24-hour clock
'''
import re

input = '12:33:12pM'

def convert(input):

    pattern = '^((1[0-2]|0?[1-9]):([0-5][0-9]):([0-5][0-9])([AaPp][Mm])$)'
    timeTemplate = re.compile(pattern)
    match = re.match(timeTemplate, input)

    if match is None:
        raise Exception('Illegal arguments - input [{}] doesn\'t match time pattern [{}]'.format(input, pattern))

    print("Input = {}".format(input))

    textGroup = match.group(1)
    isPm = True if (textGroup[:-2].casefold() == 'PM') else False
    textGroup = textGroup[:-2]
    ss = textGroup[-2:]
    textGroup = textGroup[:-3]
    mm = textGroup[-2:]
    textGroup = textGroup[:-3]
    hh = textGroup

    if isPm:
        if hh == '12':
            hh = '00'
        else:
            hh = hh + 12
        result = "{}:{}:{}".format(hh,mm,ss)
    else:
        if hh == '12':
            hh = '00'
        else:
            pass
        result = "{}:{}:{}".format(hh,mm,ss)

    return result



try:
    print('Result = ' + convert(input))
except Exception as e:
    print("Exception ", e)
