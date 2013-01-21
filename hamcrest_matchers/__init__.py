from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

class responds_to(BaseMatcher):
    def __init__(self, method_name):
        self.method_name = method_name

    def _matches(self, obj):
        return hasmethod(obj, self.method_name)

    def describe_to(self, description):
        description.append("an object responding to %s" % self.method_name)

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append("no such method in %s" % repr(item))