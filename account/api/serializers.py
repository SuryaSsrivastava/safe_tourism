from rest_framework import serializers

from account.models import Account,profile


class RegistrationSerializer(serializers.ModelSerializer):
    	
	password	= serializers.CharField(style={'input_type': 'password'}, write_only=True)
	

	class Meta:
		model = Account
		fields = ['email', 'username', 'password']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']

		if len(password) < 8:
			raise serializers.ValidationError({'message': 'Passwords must be at least 8 character long'})
		account.set_password(password)
		account.save()
		return account


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields=('user','first_name','last_name','age')
        read_only_fields = ('created','updated')

    def to_representation(self, instance):
        self.fields['user'] =  RegistrationSerializer(read_only=True)
        return super(ProfileSerializer, self).to_representation(instance)