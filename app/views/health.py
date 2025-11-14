from django.http import JsonResponse


def health(request):
    """Simple health check endpoint for Nagios/monitoring.

    Returns 200 OK with a small JSON payload when the app is reachable.
    """
    return JsonResponse({"status": "ok"}, status=200)
