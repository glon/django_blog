from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .forms import CreateCourseForm
from .models import Course


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




