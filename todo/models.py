from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"

    session_key = models.CharField(max_length=40, db_index=True)
    title = models.CharField(max_length=300)
    description = models.CharField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} [{self.status}]"
