from django.shortcuts import render

# def home(request):
#     ref = db.reference('/Sensor')
#     sensor_data = ref.get()

#     temperature = sensor_data.get('temperature', 'N/A')
#     humidity = sensor_data.get('humidity', 'N/A')

#     context = {
#         'temperature': temperature,
#         'humidity': humidity,
#     }
#     return render(request, 'home.html', context)
def home(request):
    ref = db.reference('/Sensor')
    sensor_data = ref.get()

    # Ensure sensor_data is a dictionary, even if Firebase returns None
    if not isinstance(sensor_data, dict):
        sensor_data = {}

    temperature = sensor_data.get('temperature', 'N/A')
    humidity = sensor_data.get('humidity', 'N/A')

    context = {
        'temperature': temperature,
        'humidity': humidity,
    }
    return render(request, 'home.html', context)






def details(request):
    ref = db.reference('/SensorHistory')  # Assuming historical data is under 'SensorHistory'
    sensor_history = ref.get()

    temp_data = []
    humi_data = []

    if sensor_history:
        for timestamp, values in sensor_history.items():
            temp_data.append({
                'timestamp': timestamp,
                'temperature': values.get('temperature', 'N/A')
            })
            humi_data.append({
                'timestamp': timestamp,
                'humidity': values.get('humidity', 'N/A')
            })

    context = {
        'temp_data': temp_data,
        'humi_data': humi_data,
    }
    return render(request, 'details.html', context)

def about(request):
    return render(request, 'about.html')

def live(request):
    return render(request, 'live.html')





from django.shortcuts import render
from .firebase_init import db  # import the db from firebase_init

def sensor_data_view(request):
    ref = db.reference('/Sensor')  # This is where you stored 'temperature' and 'humidity'
    sensor_data = ref.get()

    temperature = sensor_data.get('temperature', 'N/A')
    humidity = sensor_data.get('humidity', 'N/A')

    context = {
        'temperature': temperature,
        'humidity': humidity,
    }
    return render(request, 'home.html', context)










# a special Django API view that returns latest temperature and humidity (in JSON)
# Create a special Django API view that returns latest temperature and humidity (in JSON)
# 2	Use JavaScript fetch() (or AJAX) to call that API every few seconds
# 3	Update the values in your HTML page automatically without reload
from django.http import JsonResponse
from .firebase_init import db

def get_sensor_data(request):
    ref = db.reference('/Sensor')
    sensor_data = ref.get()

    temperature = sensor_data.get('temperature', 'N/A')
    humidity = sensor_data.get('humidity', 'N/A')

    return JsonResponse({
        'temperature': temperature,
        'humidity': humidity,
    })










# Create an API to send old data:
from django.http import JsonResponse
from .models import SensorData

def sensor_history(request):
    data = SensorData.objects.all().order_by('-timestamp')[:50]  # Get last 50 records
    temp_data = []
    humi_data = []
    timestamps = []

    for entry in reversed(data):  # Reverse so earliest first
        temp_data.append(entry.temperature)
        humi_data.append(entry.humidity)
        timestamps.append(entry.timestamp.strftime("%H:%M:%S"))

    return JsonResponse({
        'temperature': temp_data,
        'humidity': humi_data,
        'timestamps': timestamps,
    })



from .models import SensorData

def sensor_data(request):
    # Your code to get latest temperature and humidity
    temperature = 33
    humidity = 60

    # Save to database
    SensorData.objects.create(temperature=temperature, humidity=humidity)

    return JsonResponse({'temperature': temperature, 'humidity': humidity})








import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase only once globally (already done?)
# Reference your /Sensor node
def live_view(request):
    ref = db.reference('/Sensor')
    data = ref.get()
    
    temperature = data.get('temperature', 0)
    humidity = data.get('humidity', 0)
    air_quality = data.get('air_quality', 0)

    context = {
        'temperature': temperature,
        'humidity': humidity,
        'air_quality': air_quality
    }

    return render(request, 'live.html', context)


from django.http import JsonResponse

def get_latest_data(request):
    ref = db.reference('/Sensor')
    data = ref.get()

    temperature = data.get('temperature', 0)
    humidity = data.get('humidity', 0)
    air_quality = data.get('air_quality', 0)

    return JsonResponse({
        'temperature': temperature,
        'humidity': humidity,
        'air_quality': air_quality
    })






###################################################################### ye chal rha h poora
