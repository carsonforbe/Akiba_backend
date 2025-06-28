from django.db import models
from uuid import uuid4

# Create your models here.
class Notification(models.Model):
    TYPE_CHOICES = [
        ('CONTRRIBUTION_DUE', 'Contribution Due'),
        ('CONTRIBUTION_RECEIVED', 'Contribution Received'),
        ('PAYOUT_RECEIVED', 'Payout Received'),
        ('GOAL_PROGRESS', 'Goal Progress'),
        ('MEMBERSHIP_UPDATE', 'Membership Update'),
    ]
    
    CHANNEL_CHOICES = [
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        ('PUSH_NOTIFICATION', 'Push Notification'),
        ('IN_APP', 'In-App Notification'),
    ]
    
    notification_id = models.AutoField(primary_key=True, default=uuid4)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES)
    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

