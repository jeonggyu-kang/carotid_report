import os
import json

def parse_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    return data



class RuleBasedDiagnosis:
    @staticmethod
    def update_status(patient_dict): # 신호등
        signal_light = []

        bp = patient_dict['bp']
        dm = patient_dict['dm']
        tc = patient_dict['tc']
        ls = 0  # life style
        for k, v in patient_dict['ls'].items():
            if v:
                ls += 1

        signal_light.append( (bp, str(bp) + '. 혈압'))
        signal_light.append( (dm, str(dm) + '. 당뇨병'))
        signal_light.append( (tc, str(tc) + '. 이상지질혈증'))
        signal_light.append( (ls, str(ls) + '. 생활습관 (흡연, 운동, 비만'))

        signal_light.sort(reverse=True)

        for i, item in enumerate(signal_light):
            color_key = 'color{}'.format(i+1)
            status_key = 'status{}'.format(i+1)

            if item[0] > 2: # red
                color_value = (255,0,0)
            elif item[0] == 2: # yellow
                color_value = (255,255,0)
            else:
                color_value = (0,255,0)

            status_value = item[1]

            patient_dict[color_key] = color_value
            patient_dict[status_key] = status_value

        return patient_dict
