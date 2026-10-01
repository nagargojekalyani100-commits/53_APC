from abc import ABC, abstractmethod


class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


# Create objects
password = PasswordAuthentication()
otp = OTPAuthentication()
biometric = BiometricAuthentication()

# Interact through the abstract interface
methods = [password, otp, biometric]

for method in methods:
    method.authenticate()