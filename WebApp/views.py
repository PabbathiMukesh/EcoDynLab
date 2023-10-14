import json
import csv
from pathlib import Path
from sqlite3 import IntegrityError
import traceback

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from django.contrib.auth import authenticate, login

from WebApp.forms import AgencyForm, ContactForm, ImageFolderForm, MeasurementForm, ProjectForm
from WebApp.forms import LoginForm
from WebApp.forms import ImageUploadForm
from WebApp.models import Agency, Contact, Measurement, People
from WebApp.models import Image
from WebApp.models import ImageFolder
from WebApp.models import Project
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from WebApp.utils import get_stations
from papers.models import Paper
from WebApp.serializer import PaperSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()

BASE_DIR = Path(__file__).resolve().parent.parent
f = open(str(BASE_DIR) + '/data.json', )
data = json.load(f)


def home(request):
    images = Image.objects.all()
    context = {
        "app_cards": [
            {"name": "Display WMS data (fixed-size view)", "background_image_url": static("/images/cards/fixed.PNG"),
             'url': reverse('map_fixed_size')},
            {"name": "Display GEE data (fixed-size view)", "background_image_url": static("/images/cards/gee.PNG"),
             'url': reverse('map_from_gee')},
            {"name": "Display WMS data (full-screen view)", "background_image_url": static("/images/cards/full.PNG"),
             'url': reverse('map_full_screen')},
            {"name": "Chart from NetCDF file", "background_image_url": static("/images/cards/netCDF.jpg"),
             'url': reverse('chart_from_netcdf')},
            {"name": "Chart from ClimateSERV API", "background_image_url": static("/images/cards/ClimateSERV.jpg"),
             'url': reverse('chart_climateserv')},
            {"name": "Chart from SQL Database", "background_image_url": static("/images/cards/SQLite.jpg"),
             'url': reverse('chart_sqlite')},
            {"name": "Use forms to enter data", "background_image_url": static("/images/cards/EnterData.jpg"),
             'url': reverse('updates')},
            {"name": "Select AOI on a map", "background_image_url": static("/images/cards/aoi.PNG"),
             'url': reverse('select_aoi')},
            {"name": "Map & Chart", "background_image_url": static("/images/cards/fixed.PNG"),
             'url': reverse('map_chart')},
        ],
        "images": images,
    }

    return render(request, 'WebApp/home.html', context)


@csrf_exempt
def select_aoi(request):
    return render(request, 'WebApp/select_aoi.html', {})


@csrf_exempt
def map_chart(request):
    context = {}
    return render(request, 'WebApp/map_chart.html', context)


def map_fixed_size(request):
    return render(request, 'WebApp/map_fixedsize.html', {})


def user_login(request):
    show_signup_form = False
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # signup_form = SignupForm(request.POST)
        #print("inside")
        if 'login' in request.POST:
            #print("inside login")
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                print(username)
                print(password)
                user = authenticate(request, username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('about')
                else:
                    messages.error(request, 'Login failed. Please check your credentials.')
                    pass

        elif 'signup' in request.POST:
            #print("inside signup")

            # if signup_form.is_valid():
            #     new_user = signup_form.save(commit=False)  # Don't save to the database yet
            #     new_user.save()

            #     login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            #     return redirect('about') 
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            password=request.POST['password']
            # password2=request.POST['password2']
            # email=request.POST['email']
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                show_signup_form = True
                pass
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,'email already used')
            #     return redirect('/acc/signup')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('about')
    else:
        #print("inside else")
        login_form = LoginForm()
        #signup_form = SignupForm()

    context = {
        'show_signup_form': show_signup_form,
        }
    print("outside")
    return render(request, 'WebApp/login.html', context)


def map_from_gee(request):
    return render(request, 'WebApp/map_from_GEE.html', {})


def map_full_screen(request):
    return render(request, 'WebApp/map_fullscreen.html', {})


def chart_from_netcdf(request):
    # url = 'https://thredds.servirglobal.net/thredds/wms/mk_aqx/geos/20191123.nc?service=WMS&version=1.3.0&request
    # =GetCapabilities' document = requests.get(url) soup = BeautifulSoup(document.content, "lxml-xml")
    # bounds=soup.find("EX_GeographicBoundingBox") children = bounds.findChildren() bounds_nc=[float(children[
    # 0].get_text()),float(children[1].get_text()),float(children[2].get_text()),float(children[3].get_text())]

    context = {
        "netcdf_path": data["sample_netCDF"],
        # "netcdf_bounds":bounds_nc
    }
    return render(request, 'WebApp/chart_from_netCDF.html', context)


def chart_climateserv(request):
    return render(request, 'WebApp/chart_from_ClimateSERV.html', {})


def chart_sqlite(request):
    print(get_stations())
    return render(request, 'WebApp/chart_from_SQLite.html', get_stations())


def about(request):
    images = Image.objects.filter(foldername__name='Carousel')
    agencies = Agency.objects.all()
    context = {
        "agencies": agencies,
        "images": images
    }
    return render(request, 'WebApp/about.html', context)

def people(request):
    team_members = People.objects.all().order_by('title__titleorder')
    return render(request, 'WebApp/people.html', {'team_members': team_members})

def person_detail(request, member_id):
    person = get_object_or_404(People, pk=member_id)  # Assuming your People model has a primary key 'id'
    return render(request, 'WebApp/person_detail.html', {'person': person})


def projects(request):
    projects = Project.objects.all()

    # Sort the projects by the first year in the "period" field
    sorted_projects = sorted(projects, key=lambda project: int(project.period.split('-')[0]), reverse=True)

    return render(request, 'WebApp/projects.html', {'projects': sorted_projects})

def products(request):
    return render(request, 'WebApp/products.html', {})

def pictures(request):
    return render(request, 'WebApp/pictures.html', {})

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact object and save it to the database
            contact = Contact(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                institution=form.cleaned_data['institution'],
                query=form.cleaned_data['query']
            )
            contact.save()
            
            # Redirect to a success page or show a success message
            success_message = "Thank you for your submission! We will get back to you soon."
            return render(request, 'WebApp/contactus.html', {'form': form, 'success_message': success_message})
        else:
            # Form is not valid; re-render the form with error messages
            return render(request, 'WebApp/contactus.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'WebApp/contactus.html', {'form': form})

def legal(request):
    return render(request, 'WebApp/legal.html', {})



@xframe_options_exempt
def feedback(request):
    return render(request, 'WebApp/feedback.html', {})


def setup(request):
    return render(request, 'WebApp/setup.html', {})



@csrf_exempt
def updates(request):
    if request.method == "POST":
        context = {}
        form = MeasurementForm(request.POST)
        context["form"] = form
        if form.is_valid():
            member = Measurement(station_id=request.POST["stations"], measurement_date=request.POST["measurement_date"],
                                 measurement_temp=request.POST["measurement_temp"],
                                 measurement_precip=request.POST["measurement_precip"])
            member.save()
            url = reverse('admin:%s_%s_change' % (member._meta.app_label, member._meta.model_name), args=[member.id])
            if request.user.is_active and request.user.is_superuser:
                messages.success(request, mark_safe(
                    'Data submitted! <a href="' + url + '">Go to this record in admin pages</a>'), extra_tags='form1')
            else:
                messages.success(request,
                                 mark_safe('Data submitted!'), extra_tags='form1')
            form = MeasurementForm()
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = MeasurementForm()
    return render(request, 'WebApp/update_datamodel.html', {"form": form})

    ### Papers Requests
def paper_test(request):
    # allPapers = Paper.objects.all()
    # context = {'allPapers':allPapers}
    return HttpResponse('Hello, world. You’re at the polls index.')

def paper_index(request):
    # allPapers = Paper.objects.all()
    # context = {'allPapers':allPapers}
    return render(request, 'papers/index.html')

@api_view(['GET'])
def paper_list_view(request, *args, **kwargs):
	queryset = Paper.objects.all().order_by('-year')
	serializer = PaperSerializer(queryset, many=True)
	print(len(queryset))
	return Response(serializer.data, status=200)

@api_view(['GET'])
def paper_detail_view(request, paper_id, *args, **kwargs):
	try:
		paper_obj = Paper.objects.get(id=paper_id)
	except:
		return Response({"message" : "Not Found"}, status=404)
	serializer = PaperSerializer(paper_obj)
	return Response(serializer.data, status=200)

@api_view(['POST'])
def paper_create_view(request, *args, **kwargs):
	serializer = PaperSerializer(data=request.data)
	print(serializer)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response(serializer.data, status=201)
	return Response({}, status=400)


def remove_bom(string):
    if string.startswith('\ufeff'):
        return string[1:]
    return string
    

def picture_gallery(request):
    images = Image.objects.all()
    folder = ImageFolder.objects.all()
    return render(request, 'WebApp/pictures.html', {'images': images,'folder': folder})


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        folder_form = ImageFolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pictures')
        if folder_form.is_valid():
            folder_form.save()
            return redirect('upload_image')
        else:
            folder_form = ImageFolderForm()
    else:
        form = ImageUploadForm()
        folder_form = ImageFolderForm()

    return render(request, 'WebApp/upload_image.html', {'form': form, 'folder_form': folder_form})

def upload_agency(request):
    if request.method == 'POST':
        form = AgencyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_agency')
    else:
        form = AgencyForm()
    return render(request, 'WebApp/upload_agency.html', {'form': form})

def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_project')
    else:
        form = ProjectForm()
    return render(request, 'WebApp/upload_project.html', {'form': form})

def import_csv(request):
    
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
        else:
            try:
                
                decoded_file = csv_file.read().decode('utf-8')
                csv_data = csv.DictReader(decoded_file.splitlines())
                for row in csv_data:
                    row = {remove_bom(key): value for key, value in row.items()}
                    for field_name in ['Year', 'Number', 'Volume']:
                        if row.get(field_name) == '':
                            row[field_name] = None
                    try:
                        Paper.objects.create(
                            authors=row['Authors'],
                            year=row['Year'],
                            title=row['Title'],
                            #abstract=row['abstract'],
                            journal=row['Publication'],
                            issue=row.get('Number'),
                            volume=row.get('Volume'),
                            pages=row['Pages'],
                            DOI=row.get('Publisher')
                        )
                    except Exception as inner_e:
                        print(f"Error creating Paper object: {inner_e}")
                        traceback.print_exc()
                        messages.error(request, f'An error occurred: {str(inner_e)}')
                messages.success(request, 'CSV file imported successfully.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        return redirect('import_csv')  # Redirect to the import page after import

    return render(request, 'WebApp/import_csv.html')  # Replace with your template name


def create_folder(request):
    if request.method == 'POST':
        folder_form = ImageFolderForm(request.POST)
        if folder_form.is_valid():
            try:
                print("success saved")
                folder_form.save()
                return JsonResponse({'success': True})
            except Exception as e:
                # Handle unique constraint violation
                print("IntegrityError:", e) 
                messages.info(request,'username already exists')
                messages.error(request, 'Login failed. Please check your credentials.')
                return JsonResponse({'success': False, 'error_message': 'Folder with this name already exists.'})
        else:
            print("Oh! no")
            return JsonResponse({'success': False, 'error_message': 'Folder with this name already exists.'})
    else:
        folder_form = ImageFolderForm()
    
    return render(request, 'create_folder.html', {'folder_form': folder_form})