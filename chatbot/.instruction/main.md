Given the complexity of the task, it's not possible to provide a full code implementation in one response. However, I can guide you through the process and provide code snippets for each part of your projects.

## Task 1: Building the Chatbot with Python, Django, and Machine Learning

### 1.1. Set up the Django and Django REST Framework project:

```sh
pip install django
pip install djangorestframework
django-admin startproject medical_chatbot
cd medical_chatbot
python manage.py startapp chat
```
Then modify the `DATABASES` section in `settings.py` according to your MySQL configuration.

### 1.2. Create a Chat Model:

In `chat/models.py`:

```python
from django.db import models

class Chat(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

After creating the model, run the following commands to create the corresponding database table:

```sh
python manage.py makemigrations
python manage.py migrate
```

### 1.3. Create a Chat Serializer:

In `chat/serializers.py`:

```python
from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
```

### 1.4. Build the Chatbot:

This part is complex and requires a deep understanding of machine learning concepts and medical data. You'll need to choose a suitable model architecture, preprocess your data appropriately, and train your model. This is a simplified example of how you might define and train a model using Keras:

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding

model = Sequential()
model.add(Embedding(10000, 128))
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
```

### 1.5. Create a Chat View:

In `chat/views.py`:

```python
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Chat
from .serializers import ChatSerializer

class ChatView(APIView):
    def post(self, request):
        message = request.data['message']
        # Here, process the message using your chatbot model and generate a response
        response = 'This is a sample response.'
        chat = Chat.objects.create(user_id=request.user.id, message=message, response=response)
        serializer = ChatSerializer(chat)
        return JsonResponse(serializer.data)
```

### 1.6. Secure the API:

Django REST Framework provides several authentication and permission options. To use token-based authentication, first install the package:

```sh
pip install djangorestframework_simplejwt
```

Then, in your `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework_simplejwt',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

## Task 2: Creating the Flutter UI for the Chatbot

For detailed Flutter code, I recommend referring to Flutter's extensive documentation and tutorials. Here is a rough outline for your tasks:

### 2.1. Set up Flutter Project:

```sh
flutter create chatbot_ui
cd chatbot_ui
```

### 2.2. Create the UI:

You'll need to create a widget for the chat messages and a text field for input.

### 2.3. Connect to the API:

```dart
import 'package:http/http.dart' as http;

final response = await http.post(
  Uri.parse('http://<your-server-url>/chat/'),
  headers: <String, String>{
    'Content-Type': 'application/json; charset=UTF-8',
  },
  body: jsonEncode(<String, String>{
    'message': 'Hello, this is my message.',
  }),
);
```

### 2.4. Manage state:

This will depend on your chosen state management pattern. If you're using `provider`, you might create a `ChatModel` class that extends `ChangeNotifier`, and call `notifyListeners()` whenever the chat messages change.

### 2.5. Handle errors:

```dart
try {
  final response = await http.post(...);
  if (response.statusCode == 200) {
    // If the server returns a 200 OK response,
    // then parse the JSON.
    return Post.fromJson(jsonDecode(response.body));
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load post');
  }
} catch (e) {
  // Handle the exception
}
```

These examples are simplified and you need to adjust them according to your data and requirements. Developing a medical chatbot involves a significant amount of work and expertise in several areas, including backend web development, machine learning, Flutter development, and healthcare. It's also critically important to handle user data securely, especially in a healthcare context.

Also, please be aware that training a machine learning model on user conversations, as you suggested, raises serious privacy and ethical issues. You should only do this with the informed consent of your users, and you should ensure that you are complying with all relevant laws and regulations, such as the GDPR in Europe.