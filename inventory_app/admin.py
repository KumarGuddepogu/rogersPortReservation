from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


#Register your models here.

@admin.register(WGR, WRS, IGW, MX, WAS, CGW, DGW, SIGR, cSDE, dSDE, WPR,CgwReservations,
                DgwReservations, CsdeReservations, DsdeReservations, IgwReservations,
                MxReservations, SigrReservations, WasReservations,WgrReservations, WprReservations, WrsReservations)
class ViewAdmin(ImportExportModelAdmin):
    pass
