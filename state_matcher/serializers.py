from numpy import result_type
from rest_framework import serializers

from .models import UserDetails
from .name_match_levenshtein_algo import name_matching_algo

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserDetails
        fields = [
            "pk",
            "name", 
            "state"
        ]

    def validate_state(self, value):

            print("in validate state")
            data = [] 
            result_dict = {}
            max_match  = -1
            with open('state_matcher/state.txt') as f:
                for line in f:
                    line = line.strip()
                    data.append(line)

            best_match_dict = []
            index = 0
            for state in data:
                if(state == value):
                    return value
                else:
                    result = name_matching_algo(state, value)
                    percent = max(result.keys())
                    if percent > max_match:
                        max_match = percent
                    result_dict[percent] = result

            
            raise serializers.ValidationError(
                "Incorrect State Name, Best Matches is " + result_dict[max_match][max_match] 
            )

    

