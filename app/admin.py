from django.contrib import admin
from .models import User_tel,User_info,Property_info,User_law_info,Tex_info,Room_info,Garden_info,Property_photo,Education_info,Planting_plan,Plant_type_doc,Plant_type_fact
admin.site.register(User_info)
admin.site.register(User_tel)
admin.site.register(Property_info)
admin.site.register(User_law_info)
admin.site.register(Room_info)
admin.site.register(Tex_info)
admin.site.register(Garden_info)
admin.site.register(Property_photo)
admin.site.register(Plant_type_doc)
admin.site.register(Education_info)
admin.site.register(Planting_plan)
admin.site.register(Plant_type_fact)
