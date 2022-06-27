from rest_framework import serializers

from .models import (MentalHealthFeedback, PostBookingFeedback,
                             PostOrderFeedback, NpsFeedback, PostAppointmentFeedback)
# from patients.serializers import UserSerializer, PatientSerializer


class  MentalHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model =  MentalHealthFeedback
        exclude = ('created_at','updated_at')

    def create(self, validated_data):
        create = super().create(validated_data)
        # assert isinstance(create, object)
        return create


class  PostBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PostBookingFeedback
        exclude = ('created_at','updated_at')

    def create(self, validated_data):
        create = super().create(validated_data)

        # assert isinstance(create, object)
        return create


class  PostOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PostOrderFeedback
        exclude = ('created_at','updated_at')

    def create(self, validated_data):
        create = super().create(validated_data)

        # assert isinstance(create, object)
        return create


class  NpsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  NpsFeedback
        exclude = ('created_at','updated_at')

    def create(self, validated_data):
        create = super().create(validated_data)

        # assert isinstance(create, object)
        return create


class  PostAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PostAppointmentFeedback
        exclude = ('created_at','updated_at')

    def create(self, validated_data):
        create = super().create(validated_data)

        # assert isinstance(create, object)
        return create

#
# class PreDeliverySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PreDeliveryFeedback
#         exclude = ('user',)
#
#     def create(self, validated_data):
#         create = super().create(validated_data)
#
#         # Send Slack Notification
#         send_slack_message_async('feedback/slack/predelivery_feedback.slack', 'data', create)
#
#         return create
#
#
# class PostDeliverySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostDeliveryFeedback
#         exclude = ('user',)
#
#     def create(self, validated_data):
#         create = super().create(validated_data)
#
#         # Send Slack Notification
#         send_slack_message_async('feedback/slack/postdelivery_feedback.slack', 'data', create)
#
#         return create
#
#
# class PostDiagnosticsTestRegSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostDiagnosticsTestRegFeedback
#         exclude = ('user',)
#
#     def create(self, validated_data):
#         create = super().create(validated_data)
#
#         # Send Slack Notification
#         send_slack_message_async('feedback/slack/post_diagnostics_test_reg_feedback.slack', 'data', create)
#
#         return create

#
# class PostUploadingTestResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostUploadingTestResultFeedback
#         exclude = ('user',)
#
#     def validate(self, attrs):
#         errors = {}
#         error_msgs = {
#             "required": ["This field is required"],
#             "wrong_field": lambda x: ["This field does not exsist for {x} service"]
#         }
#
#         service_type = attrs.get('service_type')
#         center_experience_rating = attrs.get('center_experience_rating')
#         waiting_time = attrs.get('waiting_time')
#         customer_service_satisfaction = attrs.get('customer_service_satisfaction')
#         lab_experience_rating = attrs.get('lab_experience_rating')
#         home_experience_rating = attrs.get('home_experience_rating')
#         lab_technicians_rating = attrs.get('lab_technicians_rating')
#         home_experience_rating_comment = attrs.get('home_experience_rating_comment')
#
#         def check_if_available(properties):
#             for property in properties:
#                 if not property.get("value"):
#                     errors[property.get("name")] = error_msgs["required"]
#
#         if service_type == 'home service':
#             if any((center_experience_rating, center_experience_rating, waiting_time, customer_service_satisfaction,
#                     lab_experience_rating)):
#                 errors['service_type_error'] = [f'You used the wrong field for {service_type}']
#             check_if_available((
#                 {"name": "home_experience_rating", "value": home_experience_rating},
#                 {"name": "lab_technicians_rating", "value": lab_technicians_rating}
#             ))
#
#         if service_type == 'walk-in':
#             if any((home_experience_rating, home_experience_rating_comment, lab_technicians_rating)):
#                 errors['service_type_error'] = ['You used the wrong field']
#             check_if_available(
#                 (
#                     {"name": "center_experience_rating", "value": center_experience_rating},
#                     {"name": "waiting_time", "value": waiting_time},
#                     {"name": "customer_service_satisfaction", "value": customer_service_satisfaction},
#                     {"name": "lab_experience_rating", "value": lab_experience_rating}
#                 ))
#
#         if errors:
#             raise serializers.ValidationError(errors)
#
#         return attrs
#
#     def create(self, validated_data):
#         create = super().create(validated_data)
#
#         # Send Slack Notification
#         send_slack_message_async('feedback/slack/post_uploading_test_feedback.slack', 'data', create)
#
#         return create


# class SessionRatingSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#
#     class Meta:
#         model = SessionRating
#         fields = ['audio_rating', 'video_rating', 'session_rating', 'review', 'session', 'user', 'created_at']
#
#     def create(self, validated_data):
#         rating = SessionRating.objects.create(
#             audio_rating=validated_data.get('audio_rating'),
#             video_rating=validated_data.get('video_rating'),
#             session_rating=validated_data.get('session_rating'),
#             review=validated_data.get('review'),
#             session=validated_data.get('session'),
#             user=self.context['request'].user,
#         )
#
#         return rating


# class DoctorRatingSerializer(serializers.ModelSerializer):
#     user = PatientSerializer(read_only=True)
#
#     class Meta:
#         model = DoctorRating
#         fields = ['doctor_rating', 'review', 'session', 'user', 'created_at']
#
#     def create(self, validated_data):
#         rating = DoctorRating.objects.create(
#             doctor_rating=validated_data.get('doctor_rating'),
#             review=validated_data.get('review'),
#             session=validated_data.get('session'),
#             patient=self.context['request'].user.patient,
#         )
#
#         return rating
