calls=0
def count_calls ():
    global calls
    calls = calls + 1
def string_info (string):
    print ((len (string), (string.upper()), string.lower()))
    count_calls()
def is_contains (string,list_to_search):
    count_calls()
    string_low=string.lower()
    list_to_search_low = [s.lower() for s in list_to_search]
    if string_low in list_to_search_low:
         print('True',end='')
    else:
         print('False',end='')
    return ''


string_info("CAPYBARA")
string_info("ARMAGEDDON")
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
