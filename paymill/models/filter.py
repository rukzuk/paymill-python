# coding=utf-8
__author__ = 'yalnazov'


class Filter(object):

    OPERATOR = dict(LESS_THAN="<",
                    GREATER_THAN=">",
                    EQUAL="",
                    INTERVAL="-")

    def __init__(self, key, values=tuple(), operator=OPERATOR['EQUAL']):
        if key is None:
            raise ValueError('None passed for key to Filter!')

        if values[0] is None:
            raise ValueError('None passed for value to Filter!')

        self.key = key
        self.values = values
        self.operator = operator

        if len(self.values) > 1 and self.values[1] is None:
            self.operator = Filter.OPERATOR['EQUAL']
        elif len(self.values) > 1:
            self.operator = Filter.OPERATOR['INTERVAL']

    def to_dict(self):
        result = str(str(self.values[0]) + self.operator)
        if len(self.values) > 1 and self.values[1] is not None:
            result += self.values[1]
        result = dict([(str(self.key), str(result))])
        return result


class FilterList(Filter):

    def __init__(self, *filters):
        self.filters = filters

    def to_dict(self):
        combined_dict = dict()
        for filtr in self.filters:
            combined_dict.update(filtr.to_dict())
        return combined_dict
