from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from learn.models import Video
from learn.forms import *


def create(request):
    form = VideoUploadForm()
    videos = Video.objects.all()
    return render(request, 'video_upload.html', {'videos': videos, 'form': form})

def all(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})


def video(request, video_id):
    print video_id
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404('Video %s does not exist' % (video_id))
    print video.uploaded_video
    return render(request, 'video_player.html', {'video': video})
            

def submit(request, video_id):
    if request.method == 'POST':
        form = VideoUploadForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse("MOTHER FUCKER IT UPLOADED")
        
def serve(request, video_id):
    video = Video.objects.get(pk=video_id)
    print video.uploaded_video.url
    filename = video.uploaded_video.name.split('/')[-1]
    response = HttpResponse(video.uploaded_video, content_type='video/mp4')
    print video.uploaded_video.file.size
    response['Content-length'] = video.uploaded_video.file.size
    
    return response