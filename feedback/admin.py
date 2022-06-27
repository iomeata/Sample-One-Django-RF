from django.contrib import admin
from .models import (MentalHealthFeedback, PostBookingFeedback,
                     PostOrderFeedback, NpsFeedback, PostAppointmentFeedback)

admin.site.register(MentalHealthFeedback)
admin.site.register(PostBookingFeedback)
admin.site.register(PostOrderFeedback)
admin.site.register(NpsFeedback)
admin.site.register(PostAppointmentFeedback)
