"""
https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
"""
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):
    # 60s --> 1 min.
    # 60m or 3600 --> 1 hour
    if seconds is None:
        return "now"
    
    results = []

    for name, sec in times:
        whole = seconds // sec

        if whole:
            if whole > 1:
                name += 's'
            results.append(str(whole) + ' ' + name)

        seconds = seconds % sec
    return ', '.join(results[:-1]) + ' and ' + results[-1] if len(results) > 1 else results[0]


print(format_duration(1)) # "1 second"
print(format_duration(62)) #"1 minute and 2 seconds"
print(format_duration(120)) #"2 minutes"
print(format_duration(3600)) #"1 hour"
print(format_duration(3662)) #"1 hour, 1 minute and 2 seconds"
print(format_duration(7324))

