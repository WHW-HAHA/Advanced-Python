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
    def __init__(self):
        pass

    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_docenment(self):
        print('</body></html>')

    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em> %s </em>'%match.group(1)
    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        print(data)

class Rule():
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block) <=70 and block[-1] == ':'

class TitleRule(HeadingRule):
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self,block)

class ListItemRule(Rule):
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    type = 'list'
    inside = False
    def condition(self, block):
        return True
    def action(self,block, handler):
        if not self.inside and ListItemRule.condition(self,block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    type = 'paragraph'
    def condition(self, block):
        return True

def line(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in file:
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []





