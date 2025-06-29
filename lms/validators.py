from rest_framework import serializers


class OnlyYouTubeValidator:
    """
    Валидатор проверяет вхождение слова "youtube.com" в строке.
    В случае отсутствия данного слова в url вызывается исключение ValidationError.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if "youtube.com" not in value.get(self.field):
            raise serializers.ValidationError("Ссылка ведет на другой ресурс, отличный от youtube.com")
