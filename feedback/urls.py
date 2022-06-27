from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import api

app_name = 'feedback'

router = DefaultRouter()
router.register('mental-health', api.MentalHealthView)
# router.register('predelivery', api.PreDeliveryApiView)
# router.register('postdelivery', api.PostDeliveryApiView)
# router.register('post-uploading-test', api.PostUploadingTestResultApiView)
# router.register('post-diagnostics', api.PostDiagnosticsTestRegApiView, basename='post-diagnostics')
# router.register('patient/rate-appointment', api.PatientAppointmentFeedbackApi)
# router.register('patient/rate-doctor', api.DoctorRatingApi)
# router.register('doctor/rate-appointment', api.DoctorAppointmentFeedbackApi)

urlpatterns = [
    path('api/', include(router.urls), name="api"),
]