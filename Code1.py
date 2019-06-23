# Hanwei Wang 23-06-2019

class Handler():
    '''

    '''
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result in None: match.group(0)
            return result
        return substitution


class HTMLRender(Handler):
    '''
    
    '''



