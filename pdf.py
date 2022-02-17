from abc import ABC, abstractmethod
import argparse
import os

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("NanumGothicLight", "NanumGothicLight.ttf"))

class BasePDF(ABC):
    @abstractmethod
    def drawText():
        pass

    @abstractmethod
    def drawImage():
        pass

    @abstractmethod
    def rect():
        pass

    @abstractmethod
    def makePDF():
        pass


class PDF(BasePDF): # reportlab 의존성 
    A4_width  = A4[0]
    A4_height = A4[1]
    SUPPORTED_SHAPE_METHOD = ['rect', 'circle']
    
    @staticmethod
    def drawShape(pdf, method, location, height, width, color=None, fill=None):
        if not method in PDF.SUPPORTED_SHAPE_METHOD:
            print('Supported shape method: {}, but got {}'.format(''.join(SUPPORTED_SHAPE_METHOD), method))
            exit(1)
            
        if True: # TODO : make it optional
            location = PDF.get_coords_by_ratio(location)

        if color is None:
            color = (0,0,0)
        
        pdf.setFillColor(color)
        if method == 'rect':
            pdf.rect(location[0], location[1], width=width, height=height, stroke=True, fill=fill)
        elif method == 'circle':
            pdf.circle(location[0], location[1], width, fill=fill)
        else:
            raise NotImplementedError

    @staticmethod    
    def drawText(pdf, text, location, scale=None, color=None, font=None):
    #def drawText(pdf, **kwargs):
        
        if scale is None:
            scale = 16
        if color is None:
            color = (0,0,0)

        if font is None:
            pdf.setFont('NanumGothicLight', scale)
        else:
            pdf.setFont(font, scale)

        if True: # TODO : make it optional
            location = PDF.get_coords_by_ratio(location)

        # set color
        pdf.setFillColor(color)

        report = pdf.beginText(location[0], location[1])
        
        if isinstance(text, list):
            for line in text:
                report.textLine(line)
        elif isinstance(text, str):
            report.textLine(text)

        pdf.drawText(report)

    @staticmethod  
    def drawImage(pdf, path, location, height, width):
        if True: # TODO : make it optional
            location = PDF.get_coords_by_ratio(location)
        pdf.drawImage(path, location[0], location[1], width=width, height=height)

    @staticmethod
    def makePDF(pdf_path):
        return Canvas(pdf_path)

    @staticmethod
    def get_coords_by_ratio(location):
        '''
            args:
                location (tuple or list) : percetange ratio in common CS coords system.        
        '''
        target_x = (location[0] / 100.0) * PDF.A4_width
        target_y = PDF.A4_height * (1.0 - (location[1]/100.0))
        return (target_x, target_y)