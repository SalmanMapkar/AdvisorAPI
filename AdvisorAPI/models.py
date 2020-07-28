from django.db import models


class AdvisorDataModel(models.Model):
    AdvisorId=models.AutoField(primary_key=True)
    AdvisorName=models.CharField(max_length=50)
    AdvisorPhotoURL=models.URLField()

    def __str__(self):
        return str(self.AdvisorName)

class AdvisorBookingModel(models.Model):
    BookingId=models.AutoField(primary_key=True)
    UserId=models.ForeignKey('UserAPI.UserModel', on_delete=models.CASCADE)
    AdvisorId=models.ForeignKey(AdvisorDataModel, on_delete=models.CASCADE)
    BookingTime=models.DateTimeField(null=False)

    def __str__(self):
        return str(self.BookingId)
