from authApp.models.pruebas        import Pruebas
from authApp.models.dep_ips        import Dep_ips
from rest_framework                import serializers

class PruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Pruebas
        fields = ['testDate', 'positiveTests', 'negativeTests','indeterminateTests','totalTests', 'dep_ips']#'dep_ips', 

    def create(self, validated_data):
        pruebasInstance = Pruebas.objects.create(**validated_data)
        return pruebasInstance

