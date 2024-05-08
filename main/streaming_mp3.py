from django.http import HttpResponse, StreamingHttpResponse
from django.conf import settings
import os


def stream_audio(request):
    BASE_DIR = settings.BASE_DIR
    audio_file_path = os.path.join(BASE_DIR, 'swum.mp3')  # Путь к вашему аудиофайлу
    chunk_size = 8192  # Размер чанка для потоковой передачи данных

    range_header = request.headers.get('Range', None)
    total_size = os.path.getsize(audio_file_path)

    if range_header:
        content_range = range_header.split('=')[1]
        start, end = content_range.split('-')
        start = int(start)
        end = int(end) if end else total_size - 1
    else:
        start = 0
        end = total_size - 1

    def file_iterator(file_path, start, end, chunk_size):
        with open(file_path, 'rb') as audio_file:
            audio_file.seek(start)
            while start <= end:
                chunk = audio_file.read(min(chunk_size, end - start + 1))
                if not chunk:
                    break
                start += len(chunk)
                yield chunk

    response = StreamingHttpResponse(file_iterator(audio_file_path, start, end, chunk_size), content_type='audio/mpeg')
    response['Content-Length'] = end - start + 1
    response['Content-Range'] = f'bytes {start}-{end}/{total_size}'
    return response