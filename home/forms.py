from django.forms import ModelForm

from home.models import Student, Subject, Teacher


class StudentForm(ModelForm):

    class Meta:

        model = Student

        fields = ['name',
                  'surname',
                  'age',
                  'sex',
                  'address',
                  'description',
                  'birthday',
                  'email',
                  'social_url'
                  ]


class SubjectForm(ModelForm):

    class Meta:

        model = Subject

        fields = ['name_of_subject']


class TeacherForm(ModelForm):

    class Meta:

        model = Teacher

        fields = ['name', 'surname']
