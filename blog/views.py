from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Session


def home(request):
    context = {
        'posts': Post.objects.all(),
        'sessions': Session.objects.all()
    }
    return render(request, 'blog/home.html', context)


def form_submit(request, self):
    if request.method == "POST":
        Session.uid = 'tuesday1uid'
        Session.eid = 'tuesday1eid'
        Session.qid = 'tuesday1qid'
        Session.aid = 'tuesday1aid'
        Session.save(self)
        messages.success(request, f'new session form submitted')
        return redirect('blog-home')


class UidSessionListView(ListView):
    model = Session
    template_name = 'blog/uid_sessions.html'
    context_object_name = 'sessions'
    ordering = ['-session_date']

    def get_queryset(self):
        return Session.objects.filter(uid=self.kwargs.get('uid')).order_by('-session_date')


class QidSessionListView(ListView):
    model = Session
    template_name = 'blog/qid_sessions.html'
    context_object_name = 'sessions'
    ordering = ['-session_date']

    def get_queryset(self):
        return Session.objects.filter(qid=self.kwargs.get('qid')).order_by('-session_date')


class CidSessionListView(ListView):
    model = Session
    template_name = 'blog/cid_sessions.html'
    context_object_name = 'sessions'
    ordering = ['-session_date']

    def get_queryset(self):
        return Session.objects.filter(cid=self.kwargs.get('cid')).order_by('-session_date')


class AidSessionListView(ListView):
    model = Session
    template_name = 'blog/aid_sessions.html'
    context_object_name = 'sessions'
    ordering = ['-session_date']

    def get_queryset(self):
        return Session.objects.filter(aid=self.kwargs.get('aid')).order_by('-session_date')


class DateSessionListView(ListView):
    model = Session
    template_name = 'blog/date_sessions.html'
    context_object_name = 'sessions'
    ordering = ['-uid']

    def get_queryset(self):
        # need to figure out how to filter by day, month, year only for this. not exact time.
        # this is done in one of the earlier videos
        return Session.objects.filter(session_date=self.kwargs.get('session_date')).order_by('-uid')


class SessionListView(ListView):
    model = Session
    template_name = 'blog/home.html'
    context_object_name = 'sessions'
    ordering = ['-session_date']


class SessionDetailView(DetailView):
    model = Session


class SessionCreateView(CreateView):
    model = Session
    fields = ['uid', 'cid', 'qid', 'aid']


class UidListView(ListView):
    pass


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def other(request):
    context = {}
    system = request.POST.get('system', None)
    timing = request.POST.get('timing', None)
    context['system'] = system
    return render(request, 'blog/other.html', context)


#class