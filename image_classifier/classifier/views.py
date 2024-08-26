from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImageUpload
from .serializers import ImageUploadSerializer
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image_obj = serializer.save()

            # Carregar o modelo TensorFlow
            model = load_model('path_to_your_model.h5')

            # Processar a imagem
            img = image.load_img(image_obj.image.path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)

            # Fazer a inferência
            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions, axis=1)

            # Atualizar a classificação no banco de dados
            image_obj.classification = str(predicted_class)
            image_obj.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
