import json
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import redirect, render
from django.views import View

from .forms import CreateCourseForm, CreateLessonForm
from .models import Course, Lesson


# Create your views here.
class AboutView(TemplateView):
    template_name = "course/about.html"


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/course_list.html'


class UserMixin:
    def get_queryset(self):
        qs = super(UserMixin, self).get_queryset()
        return qs.filter(user=self.request.user)


class UserCourseMixin(UserMixin, LoginRequiredMixin):
    model = Course
    login_url = '/account/login/'


class ManageCourseListView(UserCourseMixin, ListView):
    context_object_name = "courses"
    template_name = 'course/manage_course_list.html'


class CreateCourseView(UserCourseMixin, CreateView):
    fields = ['title', 'overview']
    template_name = 'course/create_course.html'

    def post(self, request, *args, **kwargs):
        form = CreateCourseForm(data=request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.user = self.request.user
            new_course.save()
            return redirect('course:manage_course')
        return self.render_to_response({'form':form})


class DeleteCourseView(UserCourseMixin, DeleteView):
    # template_name = 'course/delete_course_confirm.html'
    success_url = reverse_lazy('course:manage_course')

    def dispatch(self, request, *args, **kwargs):
        resp = super(DeleteCourseView, self).dispatch(request, *args, **kwargs)
        if self.request.is_ajax():
            response_data = {'result':'OK'}
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            return resp

class CreateLessonView(LoginRequiredMixin, View):
    model = Lesson
    login_url = '/account/login/'

    def get(self, request, *args, **kwargs):
        form = CreateLessonForm(user=self.request.user)
        return render(request, "course/create_lesson.html", {'form':form})

    def post(self, request, *args, **kwargs):
        form = CreateLessonForm(self.request.user, request.POST, request.FILES)
        if form.is_valid():
            new_lesson = form.save(commit=False)
            new_lesson.user = self.request.user
            new_lesson.save()
            return redirect("course:manage_course")

