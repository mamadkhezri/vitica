from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username,phone_number, full_name, password):
        if not email:
            raise ValueError("The Email field must be set")
        if not full_name:
            raise ValueError("The Full name field must be set")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            phone_number=phone_number,
            full_name=full_name,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, phone_number, password):
        user = self.create_user(email, username, full_name, phone_number, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
       
