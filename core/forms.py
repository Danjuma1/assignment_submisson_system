from django import forms
from .models import Course, Assignment, AssignmentSubmission


# FORM TO CREATE A COURSE
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_title', 'course_code', 'lecturer_name', 'course_description', 'end_date']

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['course_title'].label = "Course Title"
        self.fields['course_code'].label = "Course Code"
        self.fields['lecturer_name'].label = "Lecturer's Name"
        self.fields['course_description'].label = "Description"
        self.fields['end_date'].label = "End Date"

        self.fields['course_title'].widget.attrs.update(
            {
                'placeholder': 'Enter Course Title',
            }
        )

        self.fields['course_code'].widget.attrs.update(
            {
                'placeholder': 'Enter Course Code',
            }
        )

        self.fields['lecturer_name'].widget.attrs.update(
            {
                'placeholder': 'Lecturer Name',
            }
        )

        self.fields['course_description'].widget.attrs.update(
            {
                'placeholder': 'Description',
            }
        )

    def is_valid(self):
        valid = super(CourseCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(CourseCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course


# ASSIGNMENT CREATE FORM
class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'content', 'marks', 'deadline']

    def __init__(self, *args, **kwargs):
        super(AssignmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Assignment Title"
        self.fields['content'].label = "Content"
        self.fields['marks'].label = "Marks"
        self.fields['deadline'].label = "Submission Deadline"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Enter A Title',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Content',
            }
        )

        self.fields['marks'].widget.attrs.update(
            {
                'placeholder': 'Enter Marks',
            }
        )

        self.fields['deadline'].widget.attrs.update(
            {
                'placeholder': 'Submission Deadline',
            }
        )

    def is_valid(self):
        valid = super(AssignmentCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course


# ASSIGNMENT SUBMISSION FORM

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['name', 'matric_no', 'content', 'file']

    def __init__(self, *args, **kwargs):
        super(AssignmentSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Full Name"
        self.fields['matric_no'].label = "Matric Number"
        self.fields['content'].label = "Answer"
        self.fields['file'].label = "Or Upload File"

        self.fields['name'].widget.attrs.update(
            {
                'placeholder': 'Enter Your Full Name',
            }
        )

        self.fields['matric_no'].widget.attrs.update(
            {
                'placeholder': 'Your Matriculation Number',
            }
        )

        self.fields['content'].widget.attrs.update(
            {
                'placeholder': 'Write Your Answer Here',
            }
        )

        self.fields['file'].widget.attrs.update(
            {
                'placeholder': 'Upload Your FILE Here',
            }
        )

    def is_valid(self):
        valid = super(AssignmentSubmissionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentSubmissionForm, self).save(commit=False)
        if commit:
            course.save()
        return course

