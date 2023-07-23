from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import APIView

from .giveTeams import csv_valid, form_teams, makeDataframe, makeDataframe_list, give_sample_data
# from .redis_sample import give_sample_data

class Index(APIView):
    def get(self, request):
        return Response({"Team Maker": "Send requests to /formteams to get results"}, status=200)

class makeTeamsAPIView(APIView):
    def get(self, request): 
        return Response({"Error": "GET requests not allowed"}, status=400)

    def post(self, request):
        
        if request.FILES:
            
            file_object = request.FILES['file']
            if(file_object):
                df = makeDataframe(file_object)
                print(df.to_dict())
            
            if not csv_valid(file_object, df):
                return Response({"Error": "CSV file not compatible"})
                
        else:
            df = give_sample_data()
            
            print(df)

        request_data = {
                'minpositions': {
                    'bat': int(request.data.get('bat', 0)), 
                    'bowl':  int(request.data.get('bowl', 0)), 
                    'all':  int(request.data.get('all', 0)), 
                    'wk':  int(request.data.get('wk', 0))
                    }
                }
        results = form_teams(df, request_data)
        print('teams formed')
        if not len(results['Teams']):
            return Response({"Status": "No teams could be formed with the given data"})
            
        return Response(results)
