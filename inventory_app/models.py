from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone as tz


class JuniperNetwork(models.Model):
    id = models.AutoField(primary_key=True)
    Router_Ports = models.CharField(max_length=100, unique=True)
    Site = models.CharField(max_length=100, blank=False)
    Router = models.CharField(max_length=100, blank=False)
    Slot = models.CharField(max_length=100, blank=False)
    Module_Description = models.CharField(max_length=100, blank=False)
    Port_Name = models.CharField(max_length=100, blank=False)
    Port_Status = models.CharField(max_length=100, blank=False)
    Categories = models.CharField(max_length=100, null=True, blank=True)
    Negotiated_Speed = models.CharField(max_length=100, null=True, blank=True)
    Bandwidth = models.CharField(max_length=100, blank=False)
    Optics = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.Router_Ports

    def get_data(self):
        return {
            'id': self.id,
            'Router_Ports': self.Router_Ports,
            'Site': self.Site,
            'Router': self.Router,
            'Slot': self.Slot,
            'Module_Description': self.Module_Description,
            'Port_Name': self.Port_Name,
            'Port_Status': self.Port_Status,
            'Categories' : self.Categories,
            'Negotiated_Speed': self.Negotiated_Speed,
            'Bandwidth': self.Bandwidth,
            'Optics': self.Optics
        }


class WGR(JuniperNetwork):
    class Meta:
        verbose_name_plural = "WGR"

    pass


class WRS(JuniperNetwork):
    class Meta:
        verbose_name_plural = "WRS"

    pass


class IGW(JuniperNetwork):
    class Meta:
        verbose_name_plural = "IGW"

    pass


class MX(JuniperNetwork):
    class Meta:
        verbose_name_plural = "MX"

    pass


class WAS(JuniperNetwork):
    class Meta:
        verbose_name_plural = "WAS"

    pass


class CiscoNetwork(models.Model):
    id = models.AutoField(primary_key=True)
    Router_Ports = models.CharField(max_length=100, unique=True)
    Site = models.CharField(max_length=100, blank=False)
    Router = models.CharField(max_length=100, blank=False)
    Slot = models.CharField(max_length=100, blank=False)
    # Module_Description = models.CharField(max_length=100, blank=False)
    Port_Name = models.CharField(max_length=100, blank=False)
    Port_Status = models.CharField(max_length=100, blank=False)
    Categories = models.CharField(max_length=100, null=True, blank=True)
    Negotiated_Speed = models.CharField(max_length=100, null=True, blank=True)
    Bandwidth = models.CharField(max_length=100, blank=False)
    Optics = models.CharField(max_length=100, blank=True)
    Card = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "CGW"
        abstract = True

    def __str__(self):
        return self.Router_Ports

    def get_data(self):
        return {
            'id': self.id,
            'Router_Ports': self.Router_Ports,
            'Site': self.Site,
            'Router': self.Router,
            'Slot': self.Slot,
            # 'Module_Description': self.Module_Description,
            'Port_Name': self.Port_Name,
            'Port_Status': self.Port_Status,
            'Categories' : self.Categories,
            'Negotiated_Speed': self.Negotiated_Speed,
            'Bandwidth': self.Bandwidth,
            'Optics': self.Optics,
            'Card': self.Card
        }


class CGW(CiscoNetwork):
    class Meta:
        verbose_name_plural = "CGW"

    pass


class DGW(CiscoNetwork):
    class Meta:
        verbose_name_plural = "DGW"

    pass


class SIGR(JuniperNetwork):
    class Meta:
        verbose_name_plural = "SIGR"

    pass


class cSDE(JuniperNetwork):
    class Meta:
        verbose_name_plural = "cSDE"

    pass


class dSDE(JuniperNetwork):
    class Meta:
        verbose_name_plural = "dSDE"

    pass


class WPR(JuniperNetwork):
    class Meta:
        verbose_name_plural = "WPR"

    pass


class AllReservations(models.Model):
    # Router_Port_id = models.ForeignKey(CGW, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=150, blank = True)
    project_number = models.CharField(max_length=100, blank=False)
    project_name = models.CharField(max_length=100, blank=False)
    target_date = models.DateField()
    order_date = models.DateField('Ordered At', null=False,
                                  db_column='order_date', blank=False,
                                  default=tz.now)

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        if self.user:
            self.user_name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f'reserved by {self.user_name}'


class CgwReservations(AllReservations):
    Router_Ports = models.OneToOneField(CGW, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "CgwReservations"


class DgwReservations(AllReservations):
    Router_Ports = models.OneToOneField(DGW, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "DgwReservations"


class CsdeReservations(AllReservations):
    Router_Ports = models.OneToOneField(cSDE, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "CsdeReservations"


class DsdeReservations(AllReservations):
    Router_Ports = models.OneToOneField(dSDE, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "DsdeReservations"


class IgwReservations(AllReservations):
    Router_Ports = models.OneToOneField(IGW, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "IgwReservations"


class MxReservations(AllReservations):
    Router_Ports = models.OneToOneField(MX, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "MxReservations"


class SigrReservations(AllReservations):
    Router_Ports = models.OneToOneField(SIGR, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "SigrReservations"


class WasReservations(AllReservations):
    Router_Ports = models.OneToOneField(WAS, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "WasReservations"


class WgrReservations(AllReservations):
    Router_Ports = models.OneToOneField(WGR, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "WgrReservations"


class WprReservations(AllReservations):
    Router_Ports = models.OneToOneField(WPR, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "WprReservations"


class WrsReservations(AllReservations):
    Router_Ports = models.OneToOneField(WRS, on_delete=models.CASCADE, primary_key=True, to_field='Router_Ports',db_column="Router_Ports")

    class Meta:
        verbose_name_plural = "WrsReservations"

