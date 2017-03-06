from django.contrib import admin
from . models import Doctor, Laboratory_Test, Patient, Laboratory, Session, Laboratory_Technician

admin.site.register(Doctor)
admin.site.register(Laboratory_Test)
admin.site.register(Patient)
admin.site.register(Laboratory)
admin.site.register(Session)
admin.site.register(Laboratory_Technician)
