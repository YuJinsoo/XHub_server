from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=100)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, null=True)
    age_limit = models.DateField(blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    CATEGORY_CHOICE = (("축구(풋살)", "축구(풋살)"), ("농구", "농구"), ("배트민턴", "배트민턴"), ("볼링", "볼링"), ("테니스", "테니스"), ("골프", "골프"))
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=50, blank=True, null=True)
    
    GENDER_CHOICE = (("M", "남"), ("W", "여"), ("X", "무관"))
    gender_limit = models.CharField(choices=GENDER_CHOICE, max_length=50, default="X")
    
    STATUS_CHOICE = (("모집중", "모집중"), ("모집완료", "모집완료"), ("모집종료", "모집종료"), ("취소", "취소"))
    status = models.CharField(choices=STATUS_CHOICE, max_length=50, default="모집중")

    location = models.CharField(max_length=255)  # 고민
    # 참여자
    # meeting_member = models.ManyToManyField(User, blank=True, null=True)  # 고민
    meeting_member = models.CharField(max_length=255, blank=True, null=True)

    max_participants = models.PositiveIntegerField()
    current_participants = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)

    def __repr__(self):
        return f"{self.id}:{self.title}-{self.description}-{self.created_at}"
    
    def add_participant(self):
        if self.current_participants < self.max_participants:
            self.current_participants += 1
            self.save()

    def remove_participant(self):
        if self.current_participants > 1:
            self.current_participants -= 1
            self.save()
    
    


class MeetingChat(models.Model):
    role = models.ForeignKey("Meeting", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)  # TextFields 고려
    created_at = models.DateTimeField(auto_now_add=True)
