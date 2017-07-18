from django.contrib import admin
from django import forms
from django.forms import models
from contest.models import Contest, Score, Student, Question, Answer

class ScoreFormSet(models.BaseInlineFormSet):
    def __init__(self, *args, **kwds):
        super(ScoreFormSet, self).__init__(*args, **kwds)
        initial = []
        for student in Student.objects.exclude(score__in=kwds['instance'].score_set.all()):
            print(student)
            temp = {'user':student, 'score':0}
            initial.append(temp)
        self.initial = initial
        self.extra += len(initial)

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        exclude = []

    def __init__(self, *args, **kwds):
        super(ScoreForm, self).__init__(*args, **kwds)
        initial = kwds.get('initial')
        if initial:
            print(initial)
            self._changed_data = initial.copy()

class ScoreInline(admin.TabularInline):
    model = Score
    form = ScoreForm
    formset = ScoreFormSet
    template = "admin/contest/edit_inline/tabular.html"
    extra = 0
    can_delete = False
    #exclude = ('user',)
    fields = ('user','score')
    #readonly_fields = ('user',)
    #def has_add_permission(self, request):
    #    return False

class ContestAdminForm(forms.ModelForm):
    class Meta:
        model = Contest
        exclude = []

#    def __init__(self, *args, **kwds):
#        super(ContestAdminForm, self).__init__(*args, **kwds)
#        if False and self.instance.pk is not None:
#            for student in Student.objects.exclude(score__in=self.instance.score_set.all()):
#                Score(user=student, contest=self.instance).save()

class ContestAdmin(admin.ModelAdmin):
    #class Media:
    #    css = {"all":("css/hide_admin_original.css",)}
    #form = ContestAdminForm
    inlines = [ScoreInline]

    def __init__(self, *args, **kwds):
        super(ContestAdmin, self).__init__(*args, **kwds)

admin.site.register(Contest, ContestAdmin)
