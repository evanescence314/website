from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Student(User):
    class Meta:
        ordering = ["last_name", "first_name"]
        proxy = True

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

class Contest(models.Model):
    class Meta:
        ordering = ['-date', '-block']

    A_BLOCK = 1
    B_BLOCK = 2
    BOTH_BLOCK = 3
    BLOCK_CHOICES = (
        (A_BLOCK, 'A'),
        (B_BLOCK, 'B'),
        (BOTH_BLOCK, 'Both'),
    )

    name = models.CharField(max_length=200)
    date = models.DateField()
    block = models.IntegerField(choices=BLOCK_CHOICES)
    max_score = models.IntegerField(default=25)
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    num_quest = models.IntegerField(default=6)
    isWeighted = models.BooleanField(default=False)
    
    def buildQuestionSet():
        for i in range(num_quest):
            self.question_set.create(num=(i+1))
    
    def __str__(self):
        return "{} ({}) [{}]".format(self.name, self.date,
                                     dict(self.BLOCK_CHOICES)[self.block])

class Question(models.Model):
    class Meta:
        ordering = ['-contest', '-num']

    contest = models.ForeignKey(Contest)
    num = models.IntegerField()

    def getWeight():
        total = 0
        temp = self.getNumSolved()
        if temp == 0:
            return 0;
        for q in self.contest.question_set.all():
            temp1 = q.getNumSolved()
            if temp1 != 0:
                total += 1.0/temp1
        return 1.0/(total*temp);

    def getNumSolved():
        count = 0
        for ans in self.answer_set.all():
            if(ans.isCorrect):
                count+=1
        return count

    def __str__(self):
        return "{}: Question {}".format(self.contest, self.num)

class Score(models.Model):
    class Meta:
        ordering = ['user']
        unique_together = ('user','contest')

    user = models.ForeignKey(Student)
    contest = models.ForeignKey(Contest)
    score = models.DecimalField(max_digits=5, decimal_places=3)

    def getScore():
	score = 0
        for ans in self.answer_set.all():
            if ans.isCorrect:
                if contest.isWeighted:
                    total += ans.question.getWeight()*contest.max_score;
                else:
                    total += 1;

    def __str__(self):
        return "{} ({})".format(self.user, self.contest.name)

class Answer(models.Model):
    class Meta:
        ordering = ['-question', '-user']

    question = models.ForeignKey(Question)
    user = models.ForeignKey(Score)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s answer to {} is {}".format(self.user, self.question.num, self.isCorrect)
