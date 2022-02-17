import os

from attribute_register import add_text_attribute
from attribute_register import add_image_attribute
from attribute_register import add_shape_attribute


''' ------------------------- 기본 형태 ------------------------- '''
one_time_attribute = []

# Text 예시
one_time_attribute.append(
    add_text_attribute(
        text = '경동맥 초음파 영상 결과',        # 컨텐츠 내용
        location = (40, 5),   # 위치 (x, y)
        scale = 14,           # 크기
        color = (0,0,0)       # 색상
    )
)


# 그림 예시 (resource 파일)
one_time_attribute.append(
    add_image_attribute(
        path = './resource/logo.png', # 이미지 저장 경로
        location = (45, 99),   # 위치 (x, y)
        height = 20, 
        width = 100
    )
)

# 그리기 예시 (shape:rect, circle)
one_time_attribute.append(
    add_shape_attribute(
        method = 'rect',       # 사각형(rect), 원(circle)
        location = (70, 30),   # 위치 (x, y)
        height = 120, 
        width = 50,
        color = (103, 153, 255),
        fill = True            # True: 채우기, False: 테두리만
    )
)

''' ------------------------- 환자 정보 & 진단 결과 ------------------------- '''
patient_specific_attribute = []
# [0] 이름 (text)
patient_specific_attribute.append(
    add_text_attribute(
        location = (90, 5),   # 위치 (x, y)
        scale = 14,           # 크기
        color = (0,0,0),      # 색상
        register = 'name'     #! target json key, 추후에 파싱 필요 
    )
)

# TODO : [1] 동맥 경화 분포 (image)

# TODO : [1-1] 협착 (text)

# TODO : [1-2] 동맥 경화반 (text)

# TODO : [1-3] 두꺼워진 내막 중막 (text)

# TODO : [2] 동맥경화 정도 (image)


# [3] 나의 혈관 영상 (image)
patient_specific_attribute.append(
    add_image_attribute(
        location = (10, 50),   # 위치 (x, y)
        height = 100, 
        width = 100,
        register = 'src_image' #! target json key, 추후에 파싱 필요 
    )
)
patient_specific_attribute.append(
    add_image_attribute(
        location = (50, 50),   # 위치 (x, y)
        height = 100, 
        width = 100,
        register = 'rst_image' #! target json key, 추후에 파싱 필요 
    )
)

# [4] 동맥경화 위험인자와 나의 상태 (shape)
patient_specific_attribute.append( #* 신호등 배경 
    add_shape_attribute(
        method = 'rect',       # 사각형
        location = (10, 70),     # 위치 (x, y)
        width = 100,
        height = 150,
        color = (0,0,0),
        fill = True,            # True: 채우기, False: 테두리만
    )
)
patient_specific_attribute.append( #* first circle
    add_shape_attribute(
        method = 'circle',       # 사각형
        location = (70, 30),     # 위치 (x, y)
        radius = 40,
        fill = True,            # True: 채우기, False: 테두리만
        register = 'color1' 
    )
)
patient_specific_attribute.append( #* second circle
    add_shape_attribute(
        method = 'circle',       # 사각형
        location = (70, 50),     # 위치 (x, y)
        radius = 40,
        fill = True,            # True: 채우기, False: 테두리만
        register = 'color2' 
    ) 
)
patient_specific_attribute.append( #* third circle
    add_shape_attribute(
        method = 'circle',       # 사각형
        location = (70, 70),     # 위치 (x, y)
        radius = 40,
        fill = True,            # True: 채우기, False: 테두리만
        register = 'color3' 
    ) 
)
patient_specific_attribute.append( #* fourth circle
    add_shape_attribute(
        method = 'circle',       # 사각형
        location = (70, 90),     # 위치 (x, y)
        radius = 40,
        fill = True,            # True: 채우기, False: 테두리만
        register = 'color4' 
    ) 
)


# [4] 동맥경화 위험인자와 나의 상태 (text)
patient_specific_attribute.append( #* first text
    add_text_attribute(
        location = (40, 15),   # 위치 (x, y)
        scale = 14,           # 크기
        color = (0,0,0),       # 색상
        register = 'status1'
    )
)
patient_specific_attribute.append( #* second text
    add_text_attribute(
        location = (40, 20),   # 위치 (x, y)
        scale = 14,           # 크기
        color = (0,0,0),       # 색상
        register = 'status2'
    )
)
patient_specific_attribute.append( #* third text
    add_text_attribute(
        location = (40, 25),   # 위치 (x, y)
        scale = 14,           # 크기
        color = (0,0,0),       # 색상
        register = 'status3'
    )
)
patient_specific_attribute.append( #* fourth text
    add_text_attribute(
        location = (40, 30),   # 위치 (x, y)
        scale = 14,           # 크기
        color = (0,0,0),       # 색상
        register = 'status4'
    )
)


