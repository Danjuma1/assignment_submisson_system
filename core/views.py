from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_lecturer, user_is_student

from .forms import CourseCreateForm, AssignmentCreateForm, AssignmentSubmissionForm
from .models import Course, Assignment, AssignmentSubmission


class HomeView(ListView):
    paginate_by = 6
    template_name = 'core/index.html'
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        return self.model.objects.all()



# COURSE CREATE VIEW
class CourseCreateView(CreateView):
    template_name = 'core/lecturer/course_create.html'
    form_class = CourseCreateForm
    extra_context = {
        'title': 'New Course'
    }
    success_url = reverse_lazy('core:course')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'lecturer':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CourseCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# VIEW FOR COURSE LIST
class CourseView(ListView):
    model = Course
    template_name = 'core/lecturer/courses.html'
    context_object_name = 'courses'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_lecturer, user_is_student)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')  # filter(user_id=self.request.user.id).order_by('-id')


# VIEW SINGLE COURSE VIEW
def course_single(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, "core/lecturer/view_course.html", {'course': course})


# ASSIGNMENT CREATE VIEW
class AssignmentCreateView(CreateView):
    template_name = 'core/lecturer/assignment_create.html'
    form_class = AssignmentCreateForm
    extra_context = {
        'title': 'New Assignment'
    }
    success_url = reverse_lazy('core:assignment-list')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'lecturer':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AssignmentCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# VIEW FOR ASSIGNMENT LIST
class AssignmentView(ListView):
    model = Assignment
    template_name = 'core/lecturer/assignments.html'
    context_object_name = 'assignment'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_student, user_is_lecturer)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()  # filter(user_id=self.request.user.id).order_by('-id')


# VIEW SINGLE ASSIGNMENT
def assignment_single(request, id):
    assignment = get_object_or_404(Assignment, id=id)
    return render(request, "core/lecturer/view_assignment.html", {'assignment': assignment})



# DELETE ASSIGNMENT VIEW
class AssignmentDeleteView(DeleteView):
    model = Assignment
    success_url = reverse_lazy('core:assignment-list')


# ASSIGNMENT SUBMISSION VIEW
class AssignmentSubmissionView(CreateView):
    template_name = 'core/lecturer/assignment_submission.html'
    form_class = AssignmentSubmissionForm
    # extra_context = {
    #     'title': 'New Exam'
    # }
    success_url = reverse_lazy('core:course')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'student':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AssignmentSubmissionView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



# VIEW FOR Assignment Submission List
class AssignmentSubmissionListView(ListView):
    model = AssignmentSubmission
    template_name = 'core/lecturer/assignment_submission_list.html'
    context_object_name = 'assignment_submission'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_lecturer, user_is_student)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')  # filter(user_id=self.request.user.id).order_by('-id')


# ASSIGNMENT SUBMISSION DELETE VIEW
class AssignmentSubmissionDelete(DeleteView):
    model = AssignmentSubmission
    success_url = reverse_lazy('core:assignment-submission-list')

