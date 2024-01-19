from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from .models import Contact
from modules.services.utils import send_message_to_telegram_service_channel


def contact(request):
    if request.method == 'POST':
        page = request.META.get('HTTP_REFERER')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        request_text = f'⭐️ New request from page {page}.\n\n<b>Name:</b> {name}\n<b>Phone:</b> {phone}\n<b>Email:</b> {email}'

        if request.POST['listing']:
            listing = request.POST['listing']
            request_text += f'\n<b>Listing:</b> {listing}'
        else:
            listing = None
        if request.POST['listing_id']:
            listing_id = request.POST['listing_id']
            request_text += f'\n<b>Listing_ID:</b> {listing_id}'
        else:
            listing_id = None

        if request.POST['user_id']:
            user_id = request.POST['user_id']
        else:
            user_id = None

        message = request.POST['message']
        if message:
            request_text += f'\n<b>Message:</b> {message}'

        feedback_method = request.POST.get('feedback_method', False)
        if feedback_method:
            request_text += f'\n<b>Feedback_method:</b> {feedback_method}'

        realtor_email = request.POST['realtor_email']
        consent_processing_personal_data = request.POST.get('consent_processing_personal_data', False) == 'on'

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                # return JsonResponse({"result": 'You have already made an inquiry for this listing'})
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        contact = Contact(listing=listing,
                          listing_id=listing_id,
                          name=name, email=email,
                          phone=phone,
                          message=message,
                          user_id=user_id,
                          consent_processing_personal_data=consent_processing_personal_data,
                          page=page,
                          feedback_method=feedback_method)
        contact.save()

        send_message_to_telegram_service_channel(request_text)

        # Send email
        # send_mail(
        #   'Property Listing Inquiry',
        #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #   'iprabhatdev@gmail.com',
        #   [realtor_email, 'random@gmail.com'],
        #   fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

        return JsonResponse({"result": _('Your request has been submitted, a realtor will get back to you soon')})
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
