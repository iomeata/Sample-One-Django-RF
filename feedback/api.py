from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import (
    MentalHealthFeedback, PostBookingFeedback, PostOrderFeedback, NpsFeedback, PostAppointmentFeedback)
from .serializers import (MentalHealthSerializer, PostBookingSerializer, PostOrderSerializer,
                          NpsSerializer, PostAppointmentSerializer)
from subscription.models import Subscription
from appointments.models import Appointment
from orders.models import Order



class MentalHealthView(viewsets.ModelViewSet):
    """API View for Mental Health Feedback."""
    serializer_class = MentalHealthSerializer
    queryset = MentalHealthFeedback.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new Mental Health Feedback."""
        instance = MentalHealthFeedback.objects.get(user=request.user)
        if instance and request.method == 'POST':
            return Response(
                {'data': 'There exists a rating for this review. Use PATCH.',
                 'id': instance.id}, status.HTTP_400_BAD_REQUEST)
        request.data['user'] = request.user.id
        request.data['subscription'] = Subscription.objects.get(user=request.user.id).id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)


class PostBookingView(viewsets.ModelViewSet):
    """API View for Post Booking Feedback."""
    serializer_class = PostBookingSerializer
    queryset = PostBookingFeedback.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new Post Booking Feedback."""
        request.data['user'] = request.user.id
        request.data['appointment'] = Appointment.objects.get(user=request.user.id).id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostOrderView(viewsets.ModelViewSet):
    """API View for Post Order Feedback."""
    serializer_class = PostOrderSerializer
    queryset = PostOrderFeedback.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new Post Order Feedback."""
        request.data['user'] = request.user.id
        request.data['order'] = Order.objects.get(user=request.user.id).id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class NpsView(viewsets.ModelViewSet):
    """API View for Nps Feedback."""
    serializer_class = NpsSerializer
    queryset = NpsFeedback.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new Nps Feedback."""
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostAppointmentView(viewsets.ModelViewSet):
    """API View for Post Appointment Feedback."""
    serializer_class = PostAppointmentSerializer
    queryset = PostAppointmentFeedback.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new Post Appointment Feedback."""
        request.data['user'] = request.user.id
        request.data['appointment'] = Appointment.objects.get(user=request.user.id).id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)










# class CustomCreateView(CreateModelMixin, GenericViewSet):
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=request.user)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
# class PreDeliveryApiView(CustomCreateView):
#     queryset = PreDeliveryFeedback.objects.all()
#     serializer_class = PreDeliverySerializer
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs):
#         """[After Order, Before Delivery Feedback Endpoint]
#         :params:
#          - experience_rating (required) choice field - [1,2,3,4,5]
#          - comment (optional)
#         """
#         return super().create(request, *args, **kwargs)
#
#
# class PostDeliveryApiView(CustomCreateView):
#     queryset = PostDeliveryFeedback.objects.all()
#     serializer_class = PostDeliverySerializer
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs):
#         """[After Delivery Feedback Endpoint] :params: - package_neatness (required) choice field - [1,2,3,4,
#         5] - timely_delivery (required) choice field - ['yes', 'no'] - rider_professionality (required) choice field
#         - [1,2,3,4,5] - users_satisfaction (required) choice field - ["unsatisfied", "not so satisfied", "satisfied",
#         "very satisfied"] - comment (optional)
#         """
#         return super().create(request, *args, **kwargs)
#
#
# class DiagnosticsCustomView(CreateModelMixin, GenericViewSet):
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=request.user)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
# class PostDiagnosticsTestRegApiView(DiagnosticsCustomView):
#     queryset = PostDiagnosticsTestRegFeedback.objects.all()
#     serializer_class = PostDiagnosticsTestRegSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs):
#         """[After Delivery Feedback Endpoint] :params: - booking_process (required) choice field - ["unsatisfied",
#         "not so satisfied", "satisfied", "very satisfied"] - comment (optional)
#         """
#         return super().create(request, *args, **kwargs)
#
#
# class PostUploadingTestResultApiView(DiagnosticsCustomView):
#     queryset = PostUploadingTestResultFeedback.objects.all()
#     serializer_class = PostUploadingTestResultSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs):
#         """[After Delivery Feedback Endpoint]
#             :params:
#             - service_type (required) choice field - ['walk-in', 'home service']
#             - refer_us (required) choice field - ['yes', 'no']
#             - refer_us_comment(optional)
#             - comment (optional)
#
#             if service-type is walk-in
#             - center_experience_rating (required) choice field - [1,2,3,4,5]
#             - center_experience_rating_comment (optional)
#             - waiting_time (required) choice field - ["less than 15
#                 minutes", "15-30 minutes", "30-60 minutes", "more than an hour"]
#             - customer_service_satisfaction (
#                 required) choice field - ["unsatisfied", "not so satisfied", "satisfied", "very satisfied"]
#             - lab_experience_rating (required) choice field - [1,2,3,4,5]
#
#             else if service type is home service
#             - home_experience_rating (required) choice field - [1,2,3,4,5]
#             - home_experience_rating_comment (optional)
#             - lab_technicians_rating (required) choice field - [1,2,3,4,5]
#
#
#         """
#         return super().create(request, *args, **kwargs)
#
#
# class DoctorAppointmentFeedbackApi(LoginRequiredMixin, viewsets.ModelViewSet):
#     queryset = SessionRating.objects.all()
#     serializer_class = SessionRatingSerializer
#
#     def create(self, request, *args, **kwargs):
#         """
#             Create doctor appointment feedback
#             [ref]
#         """
#         session = request.data['session']
#         rating = SessionRating.objects.filter(user=request.user, session=session)
#         if rating:
#             return Response([{'data': 'There exists a previous rating for this doctor'}], status.HTTP_400_BAD_REQUEST)
#
#         rating_serializer = SessionRatingSerializer(data=request.data, context={'request': request})
#         if rating_serializer.is_valid(raise_exception=True):
#             rating = rating_serializer.create(rating_serializer.validated_data)
#             #send_slack_message_async('feedback/slack/feedback.slack', 'rating', rating)
#             return Response(rating_serializer.data, status.HTTP_201_CREATED)
#
#
# class PatientAppointmentFeedbackApi(viewsets.ModelViewSet):
#     queryset = SessionRating.objects.all()
#     serializer_class = SessionRatingSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs):
#         """
#             Create patient appointment feedback
#             [ref]
#         """
#         session = request.data['session']
#         rating = SessionRating.objects.filter(user=request.user, session=session)
#         if rating:
#             return Response([{'data': 'There exists a previous rating'}], status.HTTP_400_BAD_REQUEST)
#
#         rating_serializer = SessionRatingSerializer(data=request.data, context={'request': request})
#         if rating_serializer.is_valid(raise_exception=True):
#             rating = rating_serializer.create(rating_serializer.validated_data)
#             #send_slack_message_async('feedback/slack/feedback.slack', 'rating', rating)
#             return Response(rating_serializer.data, status.HTTP_201_CREATED)
#
#     def retrieve(self, request, pk, *args, **kwargs):
#         """
#             Retrieve specific patient appointment feedback
#             :query_params:
#                 appointment=<appointment_id>
#             [ref]
#         """
#         rating = SessionRating.objects.get(id=pk)
#         return Response(SessionRatingSerializer(instance=rating).data, status.HTTP_200_OK)
#
#     def list(self, request, *args, **kwargs):
#         """
#             list appointment session feedback
#             [ref]
#         """
#         appointment = request.query_params.get('appointment')
#
#         ratings = SessionRating.objects.filter(session__appointment=appointment)
#         return Response(SessionRatingSerializer(instance=ratings, many=True).data, status.HTTP_200_OK)
#
#
# class DoctorRatingApi(viewsets.ModelViewSet):
#     queryset = DoctorRating.objects.all()
#     serializer_class = DoctorRatingSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def create(self, request, *args, **kwargs) -> Response:
#         """
#             Create doctor rating api
#             [ref]
#         """
#         session = request.data['session']
#         rating = DoctorRating.objects.filter(patient=request.user.patient, session=session)
#         if rating:
#             return Response([{'data': 'You have previously rated this doctor for this session'}],
#                             status.HTTP_400_BAD_REQUEST)
#
#         rating_serializer = DoctorRatingSerializer(data=request.data, context={'request': request})
#         if rating_serializer.is_valid(raise_exception=True):
#             rating_serializer.create(rating_serializer.validated_data)
#             return Response(rating_serializer.data, status.HTTP_201_CREATED)
#
#     def retrieve(self, request, pk, *args, **kwargs) -> Response:
#         """
#             retrieve specific doctor rating
#             [ref]
#         """
#         rating = DoctorRating.objects.get(id=pk)
#         return Response(DoctorRatingSerializer(instance=rating).data, status.HTTP_200_OK)
#
#     def list(self, request, *args, **kwargs) -> Response:
#         """
#             list doctor rating
#             [ref]
#         """
#         appointment = request.query_params.get('appointment')
#         doctor = request.query_params.get('doctor')
#         doctor_rating = request.data.get('rating')
#         ratings = DoctorRating.objects.all()
#         if appointment:
#             ratings = ratings.filter(session__appointment=appointment)
#         if doctor:
#             ratings = ratings.filter(session__appointment__doctor=doctor)
#         if doctor_rating:
#             ratings = ratings.filter(doctor_rating=doctor_rating)
#         return Response(DoctorRatingSerializer(instance=ratings, many=True).data, status.HTTP_200_OK)
