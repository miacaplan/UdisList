from django.shortcuts import render
from django.views.generic import ListView


class MyView(ListView):

    # def bar(self):
    #     return sum([x.amount for x in self.get_queryset()])


    def get_context_object_name(self, object_list):
        d = super().get_context_object_name(object_list)
        d['foo'] = 123
        return d


    {{ view.bar }}