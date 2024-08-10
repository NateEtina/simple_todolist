from django.db import models

class Tasklist(models.Model):
    listTitle = models.CharField(max_length=100, blank=True, default='Untitled')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.listTitle

class Task(models.Model):
    taskline = models.TextField()
    completed = models.BooleanField(default=False)
    parentlist = models.ForeignKey(Tasklist, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.taskline[0:50] # It shall cut the 50 first strings of the task