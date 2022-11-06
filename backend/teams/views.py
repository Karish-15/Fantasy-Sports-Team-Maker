from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import APIView

from .giveTeams import csv_valid, form_teams, makeDataframe


class Index(APIView):
    def get(self, request):
        return Response({"Team Maker": "Send requests to /formteams to get results"}, status=200)

class makeTeamsAPIView(APIView):
    def get(self, request): 
        return Response({"Error": "GET requests not allowed"}, status=400)

    def post(self, request):
        if request.FILES['file']:
            file_object = request.FILES['file']
            df = makeDataframe(file_object)
            if not csv_valid(file_object, df):
                return Response({"Error": "CSV file not compatible"})
            request_data = {
                'minpositions': {
                    'bat': int(request.data.get('bat', 0)), 
                    'bowl':  int(request.data.get('bowl', 0)), 
                    'all':  int(request.data.get('all', 0)), 
                    'wk':  int(request.data.get('wk', 0))
                    }
                }
            results = form_teams(df, request_data)
            if not len(results['Teams']):
                return Response({"Status": "No teams could be formed with the given data"})
            
            return Response(results)
        else:
            return Response({"Bad file": "Uploaded file not working"}, status=400)
