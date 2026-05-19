from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        
        # 1. Handle Premium Inquiry Form (Millwork / Architectural)
        if 'contact_submit' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            project_interest = request.POST.get('project_interest')
            message_text = request.POST.get('message')

            # Ensure required fields are not empty
            if name and email and message_text:
                
                # Email layout for your Admins
                admin_message = f"""
New Design Inquiry Received:

Name: {name}
Email: {email}
Project Interest: {project_interest}

Message:
{message_text}
"""
                
                # Email layout for the customer
                user_message = f"""
Hi {name},

Thank you for reaching out to Life in Pieces! We have safely received your architectural woodwork inquiry regarding '{project_interest}'. 

Our team will review your project details and get back to you shortly.

Your Copy of the Details:
{message_text}
------------------------------------

Best regards,
Life in Pieces Team
"""
                try:
                    # Send notice to admin list (parsed from settings)
                    send_mail(
                        subject=f"New Project Inquiry: {project_interest} from {name}",
                        message=admin_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=settings.ADMIN_EMAIL,
                        fail_silently=False,
                    )

                    # Send dynamic confirmation receipt back to the client
                    send_mail(
                        subject="Thank you for contacting Life in Pieces!",
                        message=user_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email],
                        fail_silently=False,
                    )

                    messages.success(request, "Your inquiry has been sent successfully!")
                    return redirect('index')
                    
                except Exception as e:
                    print("SMTP Email transmission error:", e)
                    messages.error(request, "Systems failed to send out the confirmation email.")
            else:
                messages.error(request, "Please fill out all fields completely before submitting.")

        # 2. Handle Secondary Carousel / Service Form (If still used on page)
        elif 'carousel_submit' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            service = request.POST.get('service')
            message_text = request.POST.get('message')

            if name and email and message_text:
                admin_message = f"""
New Service Request:
Name: {name}
Email: {email}
Phone: {phone}
Service: {service}
Message: {message_text}
"""
                user_message = f"""
Hi {name},
Thank you for your interest. We received your request for '{service}' and will contact you shortly.
"""
                try:
                    send_mail(
                        subject=f"New Service Inquiry from {name}",
                        message=admin_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=settings.ADMIN_EMAIL,
                        fail_silently=False,
                    )
                    send_mail(
                        subject="We've received your request!",
                        message=user_message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email],
                        fail_silently=False,
                    )
                    messages.success(request, "Your request has been submitted!")
                    return redirect('index')
                except Exception as e:
                    print("Email Error:", e)
                    messages.error(request, "Submission processing error.")

    # GET request processing falls back here
    return render(request, "main/index.html")

def about(request):
    return render(request,"main/about.html")

def service(request):
    return render(request,"main/service.html")

def project(request):
    return render(request,"main/project.html")

def contact(request):
    return render(request,"main/contact.html")