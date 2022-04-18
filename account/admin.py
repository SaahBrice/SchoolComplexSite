from django.contrib import admin
from account.models import CustomUser, Principal, Teachers, Students, Subjects, Academic_years, Classes, Sequences, Results
# Register your models here.
admin.site.register(Principal)
admin.site.register(Teachers)
admin.site.register(Students)
admin.site.register(Academic_years)
admin.site.register(Classes)
admin.site.register(Subjects)
admin.site.register(Sequences)
admin.site.register(Results)
admin.site.register(CustomUser)
