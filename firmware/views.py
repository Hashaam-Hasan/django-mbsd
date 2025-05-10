# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from .forms import FirmwareUploadForm
# import os
# from django.conf import settings

# # Firebase Admin SDK
# import firebase_admin
# from firebase_admin import credentials, db

# # Initialize Firebase (only once)
# if not firebase_admin._apps:
#     cred = credentials.Certificate('iot-web-c9f97-firebase-adminsdk-fbsvc-95ca970a67.json')
#     firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://iot-web-c9f97-default-rtdb.asia-southeast1.firebasedatabase.app'
#     })

# # To hold the firmware information after upload
# firmware_info = {
#     'version': '',
#     'file_url': '',
# }

# def firmware_upload(request):
#     if request.method == 'POST':
#         form = FirmwareUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Extract version and file
#             version = form.cleaned_data['version']
#             bin_file = form.cleaned_data['bin_file']

#             # ✅ Use the original uploaded filename
#             filename = bin_file.name
#             save_path = os.path.join(settings.MEDIA_ROOT, 'firmwares', filename)

#             # Create directories if they don't exist
#             os.makedirs(os.path.dirname(save_path), exist_ok=True)

#             # Write the firmware file to disk
#             with open(save_path, 'wb+') as dest:
#                 for chunk in bin_file.chunks():
#                     dest.write(chunk)

#             # Build full file URL
#             # file_url = request.build_absolute_uri(f"/media/firmwares/{filename}")

#                         # Replace with your machine's LAN IP address
#             # host_ip = "192.168.205.73"  # <-- your Django server IP
#             # file_url = f"http://{host_ip}:8000/media/firmwares/{filename}"


#             # Build file URL using ngrok domain # Use ngrok public URL instead
#             ngrok_domain = "https://6071-39-34-138-50.ngrok-free.app"
#             file_url = f"{ngrok_domain}/media/firmwares/{filename}"
#             print(f"File uploaded: {file_url}")


#             print(f"File uploaded: {file_url}")  # This will show in the Django server console

#             # Update local dictionary
#             firmware_info['file_url'] = file_url

#             # ✅ Push firmware info to Firebase Realtime Database
#             db.reference('firmware').set({
#                 'firmware_url': file_url
#             })

#             # Send a JSON response with the success message and file URL
#             return JsonResponse({
#                 'message': 'Firmware uploaded successfully!',
#                 'file_url': file_url
#             })
#         else:
#             # Log form errors to the console
#             print(form.errors)

#             return JsonResponse({
#                 'message': 'Form is invalid. Please try again.',
#                 'errors': form.errors  # This will show the validation errors
#             })
#     else:
#         form = FirmwareUploadForm()

#     return render(request, 'firmware_upload.html', {'form': form})





# def check_firmware(request, device_ip):
#     """
#     This view will check if there's a new firmware version available and return the URL for the firmware.
#     In this case, we simulate a simple check based on the firmware version.
#     """
#     if firmware_info['file_url']:
#         return JsonResponse({'firmware_url': firmware_info['file_url']})
#     else:
#         return JsonResponse({'message': 'No firmware update available'})


















from django.shortcuts import render
from django.http import JsonResponse
from .forms import FirmwareUploadForm
import os
from django.conf import settings

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate('iot-web-c9f97-firebase-adminsdk-fbsvc-95ca970a67.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://iot-web-c9f97-default-rtdb.asia-southeast1.firebasedatabase.app'
    })

# Global firmware info holder (optional)
firmware_info = {
    'version': '',
    'file_url': '',
}

def firmware_upload(request):
    if request.method == 'POST':
        form = FirmwareUploadForm(request.POST, request.FILES)
        if form.is_valid():
            version = form.cleaned_data['version']
            bin_file = form.cleaned_data['bin_file']
            filename = bin_file.name
            save_path = os.path.join(settings.MEDIA_ROOT, 'firmwares', filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, 'wb+') as dest:
                for chunk in bin_file.chunks():
                    dest.write(chunk)

            ngrok_domain = "https://ed0c-39-34-133-154.ngrok-free.app"
            file_url = f"{ngrok_domain}/media/firmwares/{filename}"
            firmware_info['file_url'] = file_url

            # ✅ Push to Firebase
            db.reference('firmware').set({
                'firmware_url': file_url
            })

            return JsonResponse({
                'message': 'Firmware uploaded successfully!',
                'file_url': file_url
            })
        else:
            print(form.errors)
            return JsonResponse({
                'message': 'Form is invalid.',
                'errors': form.errors
            })
    else:
        form = FirmwareUploadForm()
    return render(request, 'firmware_upload.html', {'form': form})

def check_firmware(request, device_ip):
    """
    This view will check if there's a new firmware version available and return the URL for the firmware.
    In this case, we simulate a simple check based on the firmware version.
    """
    if firmware_info['file_url']:
        return JsonResponse({'firmware_url': firmware_info['file_url']})
    else:
        return JsonResponse({'message': 'No firmware update available'})