import os
import argparse

from utils import parse_json, RuleBasedDiagnosis
from pdf import PDF
from config import one_time_attribute, patient_specific_attribute

from attribute_register import CommonAttribute, PatientSpecificAttribute
        

class CarotidReport:
    def __init__(self, **kwargs):
        self._build(**kwargs)
                
    def _build(self, **kwargs):
        self.pdf_root = kwargs.get('pdf_root')
        os.makedirs(self.pdf_root, exist_ok=True)

        self.method = kwargs.get('pdf_method')

        self._build_meta(**kwargs)

    def _build_meta(self, **kwargs):
        self.cover_page = kwargs.get('meta')['cover_page']
        self.cover_pdf  = kwargs.get('meta')['cover']
        
        self.one_time_attribute = kwargs.get('meta')['one_time_attribute']
        self.patient_specific_attribute = kwargs.get('meta')['patient_specific_attribute']
    
    def _make_pdf(self, p_name):
        pdf_path = os.path.join(self.pdf_root, str(p_name))
        pdf_path += '.pdf'
        pdf = self.method.makePDF(pdf_path)
        return pdf, pdf_path

    '''
    def write_json(self):
        with open(self.json_path, 'w') as f:
            json.dump(self.patient_master_dict, f, indent='\t', ensure_ascii = False)

    def _convert_to_pdf(self, pdf, repeatables, write_common_attribute=False):
        # add one time attributes
        if write_common_attribute:
            self.common_attribute(pdf, self.method)
        
        # add repeatables attributes
        is_first_row = write_common_attribute
        repeatables(pdf, self.method, is_first_row)
    '''

    def run(self, json_path, p_name=None):
        # set patient name
        patient_dict = parse_json(json_path)

        # make pdf
        if p_name is None:
            p_name = patient_dict['name']
        pdf, pdf_path = self._make_pdf(p_name)
                
        # total pages
        total_pages = 1 + self.cover_page


        # rule based diagnosis
        patient_dict = RuleBasedDiagnosis.update_status(patient_dict)


        writer_common = CommonAttribute(
            method = self.method,
            total_pages = total_pages,
            attribute_list = self.one_time_attribute
        )
        writer_common(pdf)

        writer_patient_specific = PatientSpecificAttribute(
            method = self.method,
            attribute_list = self.patient_specific_attribute,
            patient_dict = patient_dict
        )
        writer_patient_specific(pdf)

        pdf.save()
        return

        ''' 
        for i, key in enumerate(json_keys):
   
            self._convert_to_pdf(
                pdf = pdf,
                repeatables = PatientSpecificAttribute(
                    recorded_time = self._get_patient_attribute(key, 'recorded_time'),
                    ecg_images = self._get_patient_attribute(key, 'img_name'),
                    jargon = self._get_patient_attribute(key, 'annotation_info'),
                    render_dir = self.render_dir
                ),
                write_common_attribute = (i%2 == 0)
            )

            if i%2 != 0:
                pdf.showPage()
            # mark flag
            self.patient_master_dict[key]['is_printed'] = True
        '''

        pdf.save()
        self._merge_pdf(pdf_path)

        #! update json 
        #self.write_json()
        return 


    def _merge_pdf(self, contents_pdf_path):
        merger = PdfFileMerger()
        merger.append(PdfFileReader(open(self.cover_pdf, 'rb')))
        merger.append(PdfFileReader(open(contents_pdf_path, 'rb')))
        
        try:
            merger.write('(final)'+contents_pdf_path)
        except:
            print('Can not merge pdf files.')
            exit(1)



        
        

        

def opt():
    parser = argparse.ArgumentParser()
    
    ''' ------------------------------ input 파일 경로 ------------------------------ '''
    parser.add_argument('--patient_json', type=str, default='./dummy_carotid.json')       # patient json 파일
    ''' ------------------------------ 리소스 ------------------------------ '''
    parser.add_argument('--cover', type=str, default='./resource/cover.pdf')
    ''' ------------------------------ output 경로 ------------------------------ '''
    parser.add_argument('--pdf_dir', type=str, default='./pdf_results')             # 결과 PDF 파일이 저장될 경로
    
    return parser.parse_args()

def main():
    args = opt()
    
    app = CarotidReport(
        pdf_method = PDF,                     # PDF 생성 방법 (library)
        pdf_root = args.pdf_dir,              # PDF 저장 디렉터리
        meta = dict(
            cover=args.cover,   # 커버 PDF
            cover_page= 1,      # 커버 PDF 페이지 수 TODO : parse from given pdf
            one_time_attribute = one_time_attribute,
            patient_specific_attribute = patient_specific_attribute
        )   
    )
    app.run(args.patient_json) # 환자 이름은 json에서 parsing
    #app.run(args.patient_json , p_name='강정규') # 환자 json 입력 

if __name__ == '__main__':
    main()