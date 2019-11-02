
valid_time = ['morning','noon','afternoon','evening','night']
valid_source = ['online','paper']

def read_news( time_of_day = valid_time[0], source = valid_source[0]):
    if time_of_day.lower() not in valid_time or source.lower() not in valid_source:
        print('invalid arguments')
        return None
    print("reading the news in the{} (source: {})".format(time_of_day.lower(),source.lower()))

##main

read_news('mrerer','PEAE')
read_news( 'morning')
read_news()
read_news( 'afternoOn','Paper')



