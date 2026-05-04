from django.http import JsonResponse
from apps.models.campus_map import University, Pathway, DeliveryPoint
import json



def full_map(request):
    universities = []
    for u in University.objects.all():
        universities.append({
            "id": u.id,
            "name": u.name,
            "geometry": json.loads(u.geometry.geojson),  # GeoJSON → dict
        })

    pathways = []
    for p in Pathway.objects.all():
        pathways.append({
            "id": p.id,
            "path": json.loads(p.geometry.geojson),
            
        })

    delivery_points = []
    for d in DeliveryPoint.objects.all():
        delivery_points.append({
            "id": d.id,
            "name": d.name,
            "lat": d.location.y,
            "lng": d.location.x,
        })

    return JsonResponse({
        "universities": universities,
        "pathways": pathways,
        "delivery_points": delivery_points,
    })