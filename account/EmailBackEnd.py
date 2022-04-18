from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend



class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print('heeeyyyy')
        try:
            user = UserModel.objects.get(email=username)
            print(user)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                print(user)
                return user
        return None
