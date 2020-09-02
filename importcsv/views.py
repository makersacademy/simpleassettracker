from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AssetForm
import logging
# Create your views here.
@login_required(login_url='/login')
def importView(response):
  return render(response, "importcsv/importcsv.html", {})

def upload_csv(request):
  asset_count = 0
  data = {}
  if "GET" == request.method:
    return render(request, "importcsv/importcsv.html", data)
  # if not GET, then proceed
  try:
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
      messages.error(request, "File is not CSV type")
      return HttpResponseRedirect(reverse("upload_csv"))
      #if file is too large, return
    if csv_file.multiple_chunks():
      messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
      return HttpResponseRedirect(reverse("upload_csv"))

    file_data = csv_file.read().decode("utf-8")

    lines = file_data.split("\n")
    # removes headers from csv
    del lines[0]
  	# loop over the lines and save them in db. If error, store as string and then display
    for line in lines:
      fields = line.split(",")
      data_dict = {}
      data_dict["AssetTag"] = fields[0]
      data_dict["DeviceType"] = fields[1]
      data_dict["CreatedBy"] = request.user.id

      try:
        form = AssetForm(data_dict)
        if form.is_valid():
          form.save()
          asset_count += 1
        else:
          logging.getLogger("error_logger").error(form.errors.as_json())
          messages.error(request, "Field required - unable to upload. "+form.errors.as_json())
      except Exception as e:
        logging.getLogger("error_logger").error(repr(e))
        pass

  except Exception as e:
    logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
    messages.error(request, "Unable to upload file. "+repr(e))

  messages.success(request, f'You have successfully uploaded {asset_count} assets!')
  return HttpResponseRedirect(reverse("upload_csv"))
