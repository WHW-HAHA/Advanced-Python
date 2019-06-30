## Be more Pythonic


# hashable, the variable has unique address
'''
#1  __format__ built in
'''
class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_simple_display(self):
        return f'{self.name}({self.age})'

    def get_long_display(self):
        return f'{self.name} is {self.age} years old.'
        # f'', format

piglei = student('piglei', '18')
# OUTPUT: piglei(18)
print(piglei.get_simple_display())
# OUTPUT: piglei is 18 years old.
print(piglei.get_long_display())

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __format__(self, format_spec):
        if format_spec == 'long':
            return f'{self.name} is {self.age} years old.'
        elif format_spec == 'simple':
            return f'{self.name}({self.age})'
        raise ValueError('invalid format spec')

## the first argument of __func__ is always objective
## for instance, self, __str__()
piglei = Student('piglei', '18')
print('{0:simple}'.format(piglei)) # the argument is piflei
print('{0:long}'.format(piglei))


'''
#2 __getitem__ 
'''
class Events:
    def __init__(self, events):
        self.events = events

    def is_empty(self):
        return not bool(self.events)

    def list_events_by_range(self, start, end):
        return self.events[start:end]

events = Events([
    'computer started',
    'os launched',
    'docker started',
    'os stopped',
])

# 判断是否有内容，打印第二个和第三个对象
if not events.is_empty():
    print(events.list_events_by_range(1, 3))

