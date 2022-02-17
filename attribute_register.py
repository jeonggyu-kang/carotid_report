from abc import ABC, abstractmethod
import os


def add_text_attribute(**kwargs):
    text = kwargs.get('text')
    location = kwargs.get('location')
    scale = kwargs.get('scale')
    color = kwargs.get('color')
    font = kwargs.get('font')

    register = kwargs.get('register')

    if register is None:
        assert text is not None

    assert location is not None

    if color is None:
        color = (0,0,0) # default (black)
    if scale is None:
        scale = 12 # default size

    ret = {
        'type' : 'text',
        'text' : text,
        'location' : location,
        'scale' : scale,
        'color' : color,
        'font' : font,
    }
    if register is not None:
        ret.update({'register':register})
    return ret

def add_image_attribute(**kwargs):
    path = kwargs.get('path')
    location = kwargs.get('location')
    height = kwargs.get('height')
    width = kwargs.get('width')
    
    register = kwargs.get('register')

    if register is None:
        assert path is not None

    assert location is not None
    assert height is not None
    assert width is not None

    ret = {
        'type' : 'image',
        'path' : path,
        'location' : location,
        'height' : height,
        'width' : width,
    }
    if register is not None:
        ret.update({'register':register})
    return ret

def add_shape_attribute(**kwargs):
    '''
        supported shape types: rect
    '''
    method = kwargs.get('method')
    location = kwargs.get('location')
    height = kwargs.get('height')
    width = kwargs.get('width')
    color = kwargs.get('color')
    fill = kwargs.get('fill')

    register = kwargs.get('register')
    radius = kwargs.get('radius')
    if radius is not None:
        height = radius // 2
        width = radius // 2

    assert method is not None
    assert location is not None
    assert height is not None
    assert width is not None

    if fill is None:
        fill = False 
    if color is None:
        color = (0,0,0)



    ret = {
        'type' : 'shape',
        'method' : method,
        'location' : location,
        'height' : height,
        'width' : width,
        'color' : color,
        'fill' : fill
    }
    if register is not None:
        ret.update({'register':register})
    return ret




class BaseAttribute(ABC):
    @abstractmethod
    def __call__(self):
        pass
    @abstractmethod
    def _build_attribute(self):
        pass


class CommonAttribute(BaseAttribute):
    def __init__(self, method=None, attribute_list=None, total_pages=None):
        self.total_page = total_pages
        #'page' : str(1 + kwargs.get('cover_page')),
        self._build_attribute(attribute_list, method)
        
    def _build_attribute(self, attribute_list, method):
        self.attribute_lst = []

        for attribute in attribute_list:
            if 'text' == attribute['type']:
                self.attribute_lst.append({
                    'method' : method.drawText,
                    'keys' : self._parse_keys(attribute)
                })
            elif 'image' == attribute['type']:
                self.attribute_lst.append({
                    'method' : method.drawImage,
                    'keys' : self._parse_keys(attribute)
                })
            elif 'shape' == attribute['type']:
                self.attribute_lst.append({
                    'method' : method.drawShape,
                    'keys' : self._parse_keys(attribute)
                })
            else:
                raise ValueError

    def _parse_keys(self, attribute):
        attribute.pop('type')
        return attribute

    def __call__(self, pdf):
        for attribute_dict in self.attribute_lst:
            attribute_dict['method'](
                pdf=pdf,
                **attribute_dict['keys']
            )
     



class PatientSpecificAttribute(BaseAttribute):
    def __init__(self, method=None, attribute_list=None, patient_dict=None):
        self._build_attribute(attribute_list, method, patient_dict)


    def _build_attribute(self, attribute_list, method, patient_dict):
        #print(patient_dict)
        self.attribute_lst = []

        for attribute in attribute_list:
            



            if attribute['type'] == 'text':
                if 'register' in attribute.keys():
                    attribute['text'] = patient_dict[ attribute['register'] ]  # name
                
                self.attribute_lst.append({
                    'method' : method.drawText,
                    'keys' : self._parse_keys(attribute)
                })

            elif attribute['type'] == 'image':
                if 'register' in attribute.keys():
                    attribute['path'] = patient_dict[ attribute['register'] ] # src & rst image
                self.attribute_lst.append({
                    'method' : method.drawImage,
                    'keys' : self._parse_keys(attribute)
                })

            elif attribute['type'] == 'shape':
                if 'register' in attribute.keys():
                    attribute['color'] = patient_dict[ attribute['register'] ] # circle1~4
                self.attribute_lst.append({
                    'method' : method.drawShape,
                    'keys' : self._parse_keys(attribute)
                })

            else:
                raise TypeError

    def _parse_keys(self, attribute):
        attribute.pop('type')
        attribute.pop('register', None)
        return attribute


    def __call__(self, pdf):
        for attribute_dict in self.attribute_lst:
            attribute_dict['method'](
                pdf=pdf,
                **attribute_dict['keys']
            )



    
    
    
