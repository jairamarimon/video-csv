from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import read_videos, write_videos
from .serializers import VideoSerializer


class VideoListView(APIView):
    def get(self, request):
        videos = read_videos()
        sort_by = request.GET.get('sort_by')
        order = request.GET.get('order', 'asc')
        valid_sort_fields = ['name', 'post_date', 'views_count']

        if sort_by:
            if sort_by not in valid_sort_fields:
                return Response({
                    'error': f'Invalid sort_by value.'
                             f'Choose from {valid_sort_fields}.'
                }, status=400)

            reverse = order == 'desc'

            try:
                videos = sorted(
                    videos, key=lambda x: x[sort_by], reverse=reverse)
            except Exception:
                return Response({
                    'error': f'Failed to sort by `{sort_by}`.'
                }, status=400)

        return Response(videos)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        videos = read_videos()
        new_video = serializer.validated_data

        if any(video['id'] == new_video['id'] for video in videos):
            return Response({
                'error': 'Video ID must be unique.'
            }, status=400)

        videos.append(new_video)
        write_videos(videos)

        return Response(new_video, status=201)


class VideoDetailView(APIView):
    def put(self, request, id):
        videos = read_videos()
        serializer = VideoSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        for i, video in enumerate(videos):
            if video['id'] == id:

                videos[i] = serializer.validated_data
                write_videos(videos)
                return Response(serializer.validated_data)

        return Response({
            'error': 'Video not found.'
        }, status=404)

    def delete(self, request, id):
        videos = read_videos()
        new_videos = [v for v in videos if v['id'] != id]

        if len(videos) == len(new_videos):
            return Response({
                'error': 'Video not found.'
                }, status=404)

        write_videos(new_videos)
        return Response({
            'message': 'Video deleted successfully.'
        }, status=204)

    def get(self, request, id):
        videos = read_videos()
        video = [v for v in videos if v['id'] == id]
        video = video[0] if video else None

        if video:
            return Response(video)

        return Response({
            'error': 'Video not found.'
        }, status=404)
