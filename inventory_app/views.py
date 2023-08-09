from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.views.generic import TemplateView

import user.models
import pandas as pd

from inventory_app import snapshot, cisco_snapshot
from inventory_app.forms import *
from inventory_app.models import *
from user.models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def index(request):
    return render(request, 'inventory_app/index.html')


@login_required()
def users(request):
    user_items = User.objects.all()
    users_count = user_items.count()
    profile_items = Profile.objects.all()
    context = {
        'user_items': user_items,
        'profile_items': profile_items,
        'users_count': users_count,
    }
    return render(request, 'inventory_app/users.html', context)


@login_required()
def available_ports(request):
    return render(request, 'inventory_app/available_ports.html')


@login_required()
def reservation(request):
    cgwitems = CgwReservations.objects.all()
    dgwitems = DgwReservations.objects.all()
    csdeitems = CsdeReservations.objects.all()
    dsdeitems = DsdeReservations.objects.all()
    igwitems = IgwReservations.objects.all()
    mxitems = MxReservations.objects.all()
    sigritems = SigrReservations.objects.all()
    wasitems = WasReservations.objects.all()
    wgritems = WgrReservations.objects.all()
    wpritems = WprReservations.objects.all()
    wrsitems = WrsReservations.objects.all()
    reservations_count = cgwitems.count() + dgwitems.count() + csdeitems.count() + dsdeitems.count() + igwitems.count() + mxitems.count() + sigritems.count() + wasitems.count() + wgritems.count() + wpritems.count() + wrsitems.count()
    context = {
        'cgwitems': cgwitems,
        'dgwitems': dgwitems,
        'csdeitems': csdeitems,
        'dsdeitems': dsdeitems,
        'igwitems': igwitems,
        'mxitems': mxitems,
        'sigritems': sigritems,
        'wasitems': wasitems,
        'wgritems': wgritems,
        'wpritems': wpritems,
        'wrsitems': wrsitems,
        'reservations_count': reservations_count
    }
    return render(request, 'inventory_app/reservation.html', context, )


@login_required()
def cgw(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'CGW',
    }
    return render(request, 'inventory_app/cgw.html', context)


@login_required()
def cgw_json(request):
    cgw_items = CGW.objects.all()
    data = [cgw_item.get_data() for cgw_item in cgw_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def cgw_form(request):
    if request.POST:
        form = CgwReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = CGW.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-cgw_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = CgwReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/cgw_reservation.html', context)


def cgw_details(request):
    queryset=CGW.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = cisco_snapshot.process_dataframe(df)

    context = {
        'header': 'CGW',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/cgw_details.html', context)


@login_required()
def csde(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'cSDE',
    }
    return render(request, 'inventory_app/csde.html', context)


@login_required()
def csde_json(request):
    csde_items = cSDE.objects.all()
    data = [csde_item.get_data() for csde_item in csde_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def csde_form(request):
    if request.POST:
        form = CsdeReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = cSDE.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-csde_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = CsdeReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/csde_reservation.html', context)


def csde_details(request):
    queryset=cSDE.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'CSDE',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/csde_details.html', context)


@login_required()
def dgw(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'DGW',
    }
    return render(request, 'inventory_app/dgw.html', context)


@login_required()
def dgw_json(request):
    dgw_items = DGW.objects.all()
    data = [dgw_item.get_data() for dgw_item in dgw_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def dgw_form(request):
    if request.POST:
        form = DgwReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = DGW.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-dgw_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = DgwReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/dgw_reservation.html', context)


def dgw_details(request):
    queryset=DGW.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = cisco_snapshot.process_dataframe(df)

    context = {
        'header': 'DGW',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/dgw_details.html', context)


def dsde(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'dSDE',
    }
    return render(request, 'inventory_app/dsde.html', context)


@login_required()
def dsde_json(request):
    dsde_items = dSDE.objects.all()
    data = [dsde_item.get_data() for dsde_item in dsde_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def dsde_form(request):
    if request.POST:
        form = DsdeReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = dSDE.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-dsde_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = DsdeReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/dsde_reservation.html', context)


def dsde_details(request):
    queryset=dSDE.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'DSDE',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/dsde_details.html', context)


def igw(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'IGW',
    }
    return render(request, 'inventory_app/igw.html', context)


@login_required()
def igw_json(request):
    igw_items = IGW.objects.all()
    data = [igw_item.get_data() for igw_item in igw_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def igw_form(request):
    if request.POST:
        form = IgwReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = IGW.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-igw_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = IgwReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/igw_reservation.html', context)


def igw_details(request):
    queryset=IGW.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'IGW',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/igw_details.html', context)


def mx(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'MX',
    }
    return render(request, 'inventory_app/mx.html', context)


@login_required()
def mx_json(request):
    mx_items = MX.objects.all()
    data = [mx_item.get_data() for mx_item in mx_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def mx_form(request):
    if request.POST:
        form = MxReservationForm(request.POST)
        if form.is_valid():
            form.save()
            selected_id = form.cleaned_data['Router_Ports']
            change_status = MX.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
        # return redirect('inventory_app-mx_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = MxReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/mx_reservation.html', context)


def mx_details(request):
    queryset=MX.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'MX',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/mx_details.html', context)


def sigr(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'SIGR',
    }
    return render(request, 'inventory_app/sigr.html', context)


@login_required()
def sigr_json(request):
    sigr_items = SIGR.objects.all()
    data = [sigr_item.get_data() for sigr_item in sigr_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def sigr_form(request):
    if request.POST:
        form = SigrReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = SIGR.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-sigr_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = SigrReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/sigr_reservation.html', context)


def sigr_details(request):
    queryset=SIGR.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'SIGR',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/sigr_details.html', context)


def was(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'WAS',
    }
    return render(request, 'inventory_app/was.html', context)


@login_required()
def was_json(request):
    was_items = WAS.objects.all()
    data = [was_item.get_data() for was_item in was_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def was_form(request):
    if request.POST:
        form = WasReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = WAS.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-was_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = WasReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/was_reservation.html', context)


def was_details(request):
    queryset=WAS.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'WAS',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/was_details.html', context)


def wgr(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'WGR',
    }
    return render(request, 'inventory_app/wgr.html', context)


@login_required()
def wgr_json(request):
    wgr_items = WGR.objects.all()
    data = [wgr_item.get_data() for wgr_item in wgr_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def wgr_form(request):
    if request.POST:
        form = WgrReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = WGR.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-wgr_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = WgrReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/wgr_reservation.html', context)


def wgr_details(request):
    queryset=WGR.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'WGR',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/wgr_details.html', context)


def wpr(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'WPR',
    }
    return render(request, 'inventory_app/wpr.html', context)


@login_required()
def wpr_json(request):
    wpr_items = WPR.objects.all()
    data = [wpr_item.get_data() for wpr_item in wpr_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def wpr_form(request):
    if request.POST:
        form = WprReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = WPR.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-wpr_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = WprReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/wpr_reservation.html', context)


# def wpr_details(request):
#     slots = WPR.objects.order_by().values('Slot','Module_Description').distinct()
#     context = {
#         'slots': slots,
#         'header': 'WPR',
#     }
#     return render(request, 'inventory_app/wpr_details.html', context)


def wpr_details(request):
    queryset=WPR.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'WPR',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/wpr_details.html', context)


def wrs(request):
    # items=CGW.objects.all()
    context = {
        # 'items': items,
        'header': 'WRS',
    }
    return render(request, 'inventory_app/wrs.html', context)


@login_required()
def wrs_json(request):
    wrs_items = WRS.objects.all()
    data = [wrs_item.get_data() for wrs_item in wrs_items]
    response = {'data': data}
    return JsonResponse(response)


@login_required()
def wrs_form(request):
    if request.POST:
        form = WrsReservationForm(request.POST)
        if form.is_valid():
            selected_id = form.cleaned_data['Router_Ports']
            change_status = WRS.objects.filter(Router_Ports=selected_id).update(Port_Status="Reserved")
            form.save()
        # return redirect('inventory_app-wrs_form')
        messages.success(request, "Port reserved successfully")
        messages.info(request,
                      "If you wish to reserve another port make necessary changes to the below form, otherwise exit...")
    else:
        form = WrsReservationForm()
        change_status = False
    context = {
        'form': form,
        'change_status': change_status,
    }
    return render(request, 'inventory_app/wrs_reservation.html', context)


def wrs_details(request):
    queryset=WRS.objects.all()
    data = list(queryset.values())
    df=pd.DataFrame(data)
    df_html = snapshot.process_dataframe(df)

    context = {
        'header': 'WRS',
        'df_html': df_html,
    }
    return render(request, 'inventory_app/wrs_details.html', context)


def error_500(request):
    return render(request, '500.html')
