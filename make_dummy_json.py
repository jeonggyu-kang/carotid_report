import json
import os


# (환자 1명당 json 파일 하나)

def make_carotid_json():
    ret = {}
    # 동백경화 분포   
    #  None,      : 정상 (텍스트 작성 필요 없음)
    #  1.05 ~ 1.49: 증가된 내막 중막 (관찰되지 않음)
    #  1.50 ~ 9.9 : 동맥경화반 (관찰되지 않음)
    #  50 이상     : 협착 (관찰되지 않음)

    # blue box 출력 순서 : 숫자가 

    #! register 필요한 keys
    ret['name'] = '홍길동'
    ret['src_image'] = './demo/I8VAMPO2_1.bmp'
    ret['rst_image'] = './demo/11.png'

    '''
    ret['color1'] = (255,0,0)
    ret['color2'] = (255,255,0)
    ret['color3'] = (0,255,0)
    ret['color4'] = (0,255,0)

    ret['status1'] = '2. 혈압'
    ret['status2'] = '2. 당뇨병'
    ret['status3'] = '2. 이상지질혈증'
    ret['status4'] = '2. 생활습관 (흡연, 운동, 비만)'
    '''

    
    ret['lt.DCC'] = 1.6 #or 53 float or None,
    ret['lt.PCC'] = 1.6 #or 53 float or None,
    ret['lt.BULB'] = 1.6 #or 53 float or None,
    ret['lt.ICA'] = 1.6 #or 53 float or None,
    ret['lt.ECA'] = 1.6 #or 53 float or None,

    ret['rt.DCC'] = 1.6 #or 53 float or None,
    ret['rt.PCC'] = 1.6 #or 53 float or None,
    ret['rt.BULB'] = 1.6# or 53 float or None,
    ret['rt.ICA'] = 1.6 #or 53 float or None,
    ret['rt.ECA'] = 1.6 #or 53 float or None,
  
    # e.g. thresolding 
    ret['bp'] = 4 #3random.randn(5)  # int
    ret['dm'] = 2 #random.randn(5)  # int
    ret['tc'] = 1 #random.randn(5)  # int
    ret['ls'] = {
        'S' : True,
        'P' : True,
        'O' : True
    }
    # color 3가지 
    # 혈압
    #   0: 진단 X, 치료X, 정상 O               : green
    #   1: 진단 O, 치료O, 정상 O               : green
    #   2: 진단 O, 치료X, 정상 O               : yellow
    #   3: 진단 O, 치료X, 정상 X (혈압 높은 상태)  : red 
    #   4: 진단 X, 치료X, 정상 X (혈압 높은 상태)  : red

    # 당뇨
    #   0: 진단 X, 치료X, 정상 O  
    #   1: 진단 O, 치료O, 정상 O 
    #   2: 진단 O, 치료X, 정상 O 
    #   3: 진단 O, 치료X, 정상 X (혈압 높은 상태)
    #   4: 진단 X, 치료X, 정상 X (혈압 높은 상태)    

    # 고지혈증
    #   0: 진단 X, 치료X, 정상 O  
    #   1: 진단 O, 치료O, 정상 O 
    #   2: 진단 O, 치료X, 정상 O 
    #   3: 진단 O, 치료X, 정상 X (혈압 높은 상태)
    #   4: 진단 X, 치료X, 정상 X (혈압 높은 상태)    

    # 생활습관 risk factor (점수 수기로 기입 txt)
    # 점수 : cnt : 0-green, 1,2:yellow  3:Red
    # 흡연 :   S  (str)
    # 운동 부족 P
    # 비만     O

    # [2] 동맥경화 정도 (ABCDE) 미국 심장학회 발표 가이드 라인 확인 후 제공 

    

    return ret


data = make_carotid_json()

with open('dummy_carotid.json', 'w') as f:
    json.dump(data, f, indent='\t', ensure_ascii = False)
