from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

from patients.models import Patient
from subscription.models import Subscription
from appointments.models import Appointment
from orders.models import Order

RATING = (
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
)
YES_NO = (("yes", "yes"), ("no", "no"))
SATISFACTION = (
    ("unsatisfied", "unsatisfied"),
    ("not so satisfied", "not so satisfied"),
    ("satisfied", "satisfied"),
    ("very satisfied", "very satisfied")
)

DELAY_CHOICE = (
    ("less than 15 minutes", "less than 15 minutes"),
    ("15-30 minutes", "15-30 minutes"),
    ("30-60 minutes", "30-60 minutes"),
    ("more than an hour", "more than an hour")
)


class MentalHealthFeedback(models.Model):
    """Mental Health Model."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    subscription = models.ForeignKey(
        Subscription, related_name='subscription_mental_health', on_delete=models.CASCADE)
    session_rating = models.IntegerField(
        null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    session_review = models.TextField(blank=True, default='', null=True)
    follow_up = models.CharField(choices=YES_NO, max_length=50)
    no_follow_up_review = models.TextField(blank=True, default='', null=True)
    nps_rating = models.IntegerField(
        null=False, validators=[MinValueValidator(1), MaxValueValidator(10)])
    nps_review = models.TextField(blank=True, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Mental Health Feedback"

    def __str__(self):
        return self.user.email


class PostBookingFeedback(models.Model):
    """Post Booking Model."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    appointment = models.ForeignKey(
        Appointment, related_name='appointment_post_booking', on_delete=models.CASCADE)
    booking_satisfaction = models.CharField(choices=SATISFACTION, max_length=50)
    post_booking_review = models.TextField(blank=True, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Post Booking Feedback"

    def __str__(self):
        return self.user.email


class PostOrderFeedback(models.Model):
    """Post Order Model."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    post_order_rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    post_order_review = models.TextField(blank=True, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Post Order Feedback"

    def __str__(self):
        return self.user.email


class NpsFeedback(models.Model):
    """NPS Model."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nps_rating = models.IntegerField(
        null=False, validators=[MinValueValidator(1), MaxValueValidator(10)])
    nps_review = models.TextField(blank=True, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Nps Feedback"

    def __str__(self):
        return self.user.email


class PostAppointmentFeedback(models.Model):
    """Post Appointment Model."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    appointment = models.ForeignKey(
        Appointment, related_name='appointment_post_appointment', on_delete=models.CASCADE)
    doctor_rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    post_appointment_satisfaction = models.CharField(choices=SATISFACTION, max_length=50)
    video_rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    audio_rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    audio_video_review = models.TextField(blank=True, default='', null=True)
    post_appointment_review = models.TextField(blank=True, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Post Appointment Feedback"

    def __str__(self):
        return self.user.email