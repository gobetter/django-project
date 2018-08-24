import requests # pipenv install requests -> http://docs.python-requests.org/en/master/
import pprint


class WorkSheet():
    def __init__(self,sheet_id):
        self.url = 'https://spreadsheets.google.com/feeds/worksheets/'+ sheet_id +'/public/values?alt=json'
        json_string = requests.get(self.url)
        json_dict = json_string.json()

        self.title = json_dict['feed']['title']['$t']
        self.sheet_count = json_dict['feed']['openSearch$totalResults']['$t']

        self.sheet = []

        for item in json_dict['feed']['entry']:
            self.sheet.append(Sheet(item))

    def get_list(self):
        return [self.url, self.title, self.sheet_count]


class Sheet():
    def __init__(self, json_dict):
        self.url = f"{json_dict['link'][0]['href']}?alt=json"

        self.title = json_dict['title']['$t']
        self.col_count = json_dict['gs$colCount']['$t']
        self.row_count = json_dict['gs$rowCount']['$t']

        json_string = requests.get(self.url)
        sheet_json_dict = json_string.json()

        self.questionnaire = []

        for item in sheet_json_dict['feed']['entry']:
            self.questionnaire.append(Questionnaire(item))

    def get_list(self):
        return [self.title, self.col_count, self.row_count, self.url]


class Questionnaire():
    def __init__(self, json_dict):
        self.ans_timestamp               = json_dict['gsx$anstimestamp']['$t']
        self.ans_location                = json_dict['gsx$anslocation']['$t']
        self.ans_assessor                = json_dict['gsx$ansassessor']['$t']
        self.ans_gender                  = json_dict['gsx$ansgender']['$t']
        self.ans_age                     = json_dict['gsx$ansage']['$t']
        self.ans_income                  = json_dict['gsx$ansincome']['$t']
        self.ans_education               = json_dict['gsx$anseducation']['$t']
        self.ans_carreer                 = json_dict['gsx$anscarreer']['$t']
        self.ans_marital_status          = json_dict['gsx$ansmaritalstatus']['$t']
        self.ans_region                  = json_dict['gsx$ansregion']['$t']
        self.ans_best_tourist_attraction = json_dict['gsx$ansbesttouristattraction']['$t']

        self.ans_1_1_1  = self.get_scale_points(json_dict['gsx$ans111' ]['$t'])
        self.ans_1_1_2  = self.get_scale_points(json_dict['gsx$ans112' ]['$t'])
        self.ans_1_1_3  = self.get_scale_points(json_dict['gsx$ans113' ]['$t'])
        self.ans_1_1_4  = self.get_scale_points(json_dict['gsx$ans114' ]['$t'])
        self.ans_1_1_5  = self.get_scale_points(json_dict['gsx$ans115' ]['$t'])
        self.ans_1_1_6  = self.get_scale_points(json_dict['gsx$ans116' ]['$t'])
        self.ans_1_1_7  = self.get_scale_points(json_dict['gsx$ans117' ]['$t'])
        self.ans_1_1_8  = self.get_scale_points(json_dict['gsx$ans118' ]['$t']) 
        self.ans_1_1_9  = self.get_scale_points(json_dict['gsx$ans119' ]['$t'])
        self.ans_1_1_10 = self.get_scale_points(json_dict['gsx$ans1110']['$t'])
        self.ans_1_1_11 = self.get_scale_points(json_dict['gsx$ans1111']['$t'])
        self.ans_1_1_12 = self.get_scale_points(json_dict['gsx$ans1112']['$t'])
        self.ans_1_1_13 = self.get_scale_points(json_dict['gsx$ans1113']['$t'])
        self.ans_1_1_14 = self.get_scale_points(json_dict['gsx$ans1114']['$t'])
        self.ans_1_1_15 = self.get_scale_points(json_dict['gsx$ans1115']['$t'])
        self.ans_1_1_16 = self.get_scale_points(json_dict['gsx$ans1116']['$t'])
        self.ans_1_1_17 = self.get_scale_points(json_dict['gsx$ans1117']['$t'])
        self.ans_1_1_18 = self.get_scale_points(json_dict['gsx$ans1118']['$t'])
        self.ans_1_1_19 = self.get_scale_points(json_dict['gsx$ans1119']['$t'])
        self.ans_1_1_20 = self.get_scale_points(json_dict['gsx$ans1120']['$t'])

        self.ans_1_2_1  = self.get_scale_points(json_dict['gsx$ans121']['$t'])
        self.ans_1_2_2  = self.get_scale_points(json_dict['gsx$ans122']['$t'])
        self.ans_1_2_3  = self.get_scale_points(json_dict['gsx$ans123']['$t'])
        self.ans_1_2_4  = self.get_scale_points(json_dict['gsx$ans124']['$t'])
        self.ans_1_2_5  = self.get_scale_points(json_dict['gsx$ans125']['$t'])
        self.ans_1_2_6  = self.get_scale_points(json_dict['gsx$ans126']['$t'])
        self.ans_1_2_7  = self.get_scale_points(json_dict['gsx$ans127']['$t'])
        self.ans_1_2_8  = self.get_scale_points(json_dict['gsx$ans128']['$t'])
        self.ans_1_2_9  = self.get_scale_points(json_dict['gsx$ans129']['$t'])
        self.ans_1_2_10 = self.get_scale_points(json_dict['gsx$ans1210']['$t'])
        self.ans_1_2_11 = self.get_scale_points(json_dict['gsx$ans1211']['$t'])

        self.ans_1_3_1  = self.get_scale_points(json_dict['gsx$ans131']['$t'])
        self.ans_1_3_2  = self.get_scale_points(json_dict['gsx$ans132']['$t'])
        self.ans_1_3_3  = self.get_scale_points(json_dict['gsx$ans133']['$t'])
        self.ans_1_3_4  = self.get_scale_points(json_dict['gsx$ans134']['$t'])

        self.ans_1_4_1  = self.get_scale_points(json_dict['gsx$ans141']['$t'])
        self.ans_1_4_2  = self.get_scale_points(json_dict['gsx$ans142']['$t'])
        self.ans_1_4_3  = self.get_scale_points(json_dict['gsx$ans143']['$t'])
        self.ans_1_4_4  = self.get_scale_points(json_dict['gsx$ans144']['$t'])

        self.ans_1_5_1  = self.get_scale_points(json_dict['gsx$ans151']['$t'])
        self.ans_1_5_2  = self.get_scale_points(json_dict['gsx$ans152']['$t'])

        self.ans_1_6_1  = self.get_scale_points(json_dict['gsx$ans161']['$t'])
        self.ans_1_6_2  = self.get_scale_points(json_dict['gsx$ans162']['$t'])
        self.ans_1_6_3  = self.get_scale_points(json_dict['gsx$ans163']['$t'])
        self.ans_1_6_4  = self.get_scale_points(json_dict['gsx$ans164']['$t'])

        self.ans_2_1_1  = self.get_scale_points(json_dict['gsx$ans211']['$t'])
        self.ans_2_1_2  = self.get_scale_points(json_dict['gsx$ans212']['$t'])
        self.ans_2_1_3  = self.get_scale_points(json_dict['gsx$ans213']['$t'])
        self.ans_2_1_4  = self.get_scale_points(json_dict['gsx$ans214']['$t'])
        self.ans_2_1_5  = self.get_scale_points(json_dict['gsx$ans215']['$t'])
        self.ans_2_1_6  = self.get_scale_points(json_dict['gsx$ans216']['$t'])

        self.ans_2_2_1  = self.get_scale_points(json_dict['gsx$ans221']['$t'])
        self.ans_2_2_2  = self.get_scale_points(json_dict['gsx$ans222']['$t'])
        self.ans_2_2_3  = self.get_scale_points(json_dict['gsx$ans223']['$t'])
        self.ans_2_2_4  = self.get_scale_points(json_dict['gsx$ans224']['$t'])
        self.ans_2_2_5  = self.get_scale_points(json_dict['gsx$ans225']['$t'])
        self.ans_2_2_6  = self.get_scale_points(json_dict['gsx$ans226']['$t'])
        self.ans_2_2_7  = self.get_scale_points(json_dict['gsx$ans227']['$t'])

        self.ans_3_1_1  = self.get_scale_points(json_dict['gsx$ans311']['$t'])
        self.ans_3_1_2  = self.get_scale_points(json_dict['gsx$ans312']['$t'])
        self.ans_3_1_3  = self.get_scale_points(json_dict['gsx$ans313']['$t'])
        self.ans_3_1_4  = self.get_scale_points(json_dict['gsx$ans314']['$t'])
        self.ans_3_1_5  = self.get_scale_points(json_dict['gsx$ans315']['$t'])

        self.ans_3_2_1  = self.get_scale_points(json_dict['gsx$ans321']['$t'])
        self.ans_3_2_2  = self.get_scale_points(json_dict['gsx$ans322']['$t'])
        self.ans_3_2_3  = self.get_scale_points(json_dict['gsx$ans323']['$t'])

        self.ans_4_1_1  = self.get_scale_points(json_dict['gsx$ans411']['$t'])
        self.ans_4_1_2  = self.get_scale_points(json_dict['gsx$ans412']['$t'])
        self.ans_4_1_3  = self.get_scale_points(json_dict['gsx$ans413']['$t'])
        self.ans_4_1_4  = self.get_scale_points(json_dict['gsx$ans414']['$t'])
        self.ans_4_1_5  = self.get_scale_points(json_dict['gsx$ans415']['$t'])
        self.ans_4_1_6  = self.get_scale_points(json_dict['gsx$ans416']['$t'])
        self.ans_4_1_7  = self.get_scale_points(json_dict['gsx$ans417']['$t'])
        self.ans_4_1_8  = self.get_scale_points(json_dict['gsx$ans418']['$t'])
        self.ans_4_1_9  = self.get_scale_points(json_dict['gsx$ans419']['$t'])
        self.ans_4_1_10 = self.get_scale_points(json_dict['gsx$ans4110']['$t'])
        self.ans_4_1_11 = self.get_scale_points(json_dict['gsx$ans4111']['$t'])
        self.ans_4_1_12 = self.get_scale_points(json_dict['gsx$ans4112']['$t'])
        self.ans_4_1_13 = self.get_scale_points(json_dict['gsx$ans4113']['$t'])
        self.ans_4_1_14 = self.get_scale_points(json_dict['gsx$ans4114']['$t'])
        self.ans_4_1_15 = self.get_scale_points(json_dict['gsx$ans4115']['$t'])
        self.ans_4_1_16 = self.get_scale_points(json_dict['gsx$ans4116']['$t'])
        self.ans_4_1_17 = self.get_scale_points(json_dict['gsx$ans4117']['$t'])

        self.ans_4_2_1  = self.get_scale_points(json_dict['gsx$ans421']['$t'])
        self.ans_4_2_2  = self.get_scale_points(json_dict['gsx$ans422']['$t'])
        self.ans_4_2_3  = self.get_scale_points(json_dict['gsx$ans423']['$t'])
        self.ans_4_2_4  = self.get_scale_points(json_dict['gsx$ans424']['$t'])
        self.ans_4_2_5  = self.get_scale_points(json_dict['gsx$ans425']['$t'])
        self.ans_4_2_6  = self.get_scale_points(json_dict['gsx$ans426']['$t'])
        self.ans_4_2_7  = self.get_scale_points(json_dict['gsx$ans427']['$t'])
        self.ans_4_2_8  = self.get_scale_points(json_dict['gsx$ans428']['$t'])
        self.ans_4_2_9  = self.get_scale_points(json_dict['gsx$ans429']['$t'])
        self.ans_4_2_10 = self.get_scale_points(json_dict['gsx$ans4210']['$t'])
        self.ans_4_2_11 = self.get_scale_points(json_dict['gsx$ans4211']['$t'])

        self.ans_4_3_1  = self.get_scale_points(json_dict['gsx$ans431']['$t'])
        self.ans_4_3_2  = self.get_scale_points(json_dict['gsx$ans432']['$t'])
        self.ans_4_3_3  = self.get_scale_points(json_dict['gsx$ans433']['$t'])
        self.ans_4_3_4  = self.get_scale_points(json_dict['gsx$ans434']['$t'])
        self.ans_4_3_5  = self.get_scale_points(json_dict['gsx$ans435']['$t'])
        self.ans_4_3_6  = self.get_scale_points(json_dict['gsx$ans436']['$t'])
        self.ans_4_3_7  = self.get_scale_points(json_dict['gsx$ans437']['$t'])
        self.ans_4_3_8  = self.get_scale_points(json_dict['gsx$ans438']['$t'])
        self.ans_4_3_9  = self.get_scale_points(json_dict['gsx$ans439']['$t'])
        self.ans_4_3_10 = self.get_scale_points(json_dict['gsx$ans4310']['$t'])

        self.ans_4_4_1  = self.get_scale_points(json_dict['gsx$ans441']['$t'])
        self.ans_4_4_2  = self.get_scale_points(json_dict['gsx$ans442']['$t'])

        self.ans_4_5_1  = self.get_scale_points(json_dict['gsx$ans451']['$t'])
        self.ans_4_5_2  = self.get_scale_points(json_dict['gsx$ans452']['$t'])
        self.ans_4_5_3  = self.get_scale_points(json_dict['gsx$ans453']['$t'])
        self.ans_4_5_4  = self.get_scale_points(json_dict['gsx$ans454']['$t'])
        self.ans_4_5_5  = self.get_scale_points(json_dict['gsx$ans455']['$t'])
        self.ans_4_5_6  = self.get_scale_points(json_dict['gsx$ans456']['$t'])

        self.ans_4_6_1  = self.get_scale_points(json_dict['gsx$ans461']['$t'])
        self.ans_4_6_2  = self.get_scale_points(json_dict['gsx$ans462']['$t'])
        self.ans_4_6_3  = self.get_scale_points(json_dict['gsx$ans463']['$t'])
        self.ans_4_6_4  = self.get_scale_points(json_dict['gsx$ans464']['$t'])
        self.ans_4_6_5  = self.get_scale_points(json_dict['gsx$ans465']['$t'])
        self.ans_4_6_6  = self.get_scale_points(json_dict['gsx$ans466']['$t'])

        self.ans_5_1_1  = self.get_scale_points(json_dict['gsx$ans511']['$t'])
        self.ans_5_1_2  = self.get_scale_points(json_dict['gsx$ans512']['$t'])
        self.ans_5_1_3  = self.get_scale_points(json_dict['gsx$ans513']['$t'])
        self.ans_5_1_4  = self.get_scale_points(json_dict['gsx$ans514']['$t'])

        self.ans_5_2_1  = self.get_scale_points(json_dict['gsx$ans521']['$t'])
        self.ans_5_2_2  = self.get_scale_points(json_dict['gsx$ans522']['$t'])
        self.ans_5_2_3  = self.get_scale_points(json_dict['gsx$ans523']['$t'])
        self.ans_5_2_4  = self.get_scale_points(json_dict['gsx$ans524']['$t'])

        self.ans_5_3_1  = self.get_scale_points(json_dict['gsx$ans531']['$t'])
        self.ans_5_3_2  = self.get_scale_points(json_dict['gsx$ans532']['$t'])
        self.ans_5_3_3  = self.get_scale_points(json_dict['gsx$ans533']['$t'])
        self.ans_5_3_4  = self.get_scale_points(json_dict['gsx$ans534']['$t'])
        self.ans_5_3_5  = self.get_scale_points(json_dict['gsx$ans535']['$t'])
        self.ans_5_3_6  = self.get_scale_points(json_dict['gsx$ans536']['$t'])
        self.ans_5_3_7  = self.get_scale_points(json_dict['gsx$ans537']['$t'])

        self.ans_5_4_1  = self.get_scale_points(json_dict['gsx$ans541']['$t'])
        self.ans_5_4_2  = self.get_scale_points(json_dict['gsx$ans542']['$t'])
        self.ans_5_4_3  = self.get_scale_points(json_dict['gsx$ans543']['$t'])
        self.ans_5_4_4  = self.get_scale_points(json_dict['gsx$ans544']['$t'])

        self.ans_experience   = json_dict['gsx$ansexperience']['$t']
        self.ans_exclusive    = json_dict['gsx$ansexclusive']['$t']
        self.ans_expertise    = json_dict['gsx$ansexpertise']['$t']
        self.ans_exceptional  = json_dict['gsx$ansexceptional']['$t']
        self.ans_excellence   = json_dict['gsx$ansexcellence']['$t']

    def get_experience_summary(self):
        summary = self.ans_1_1_1 + self.ans_1_1_2 + self.ans_1_1_3 + self.ans_1_1_4 + self.ans_1_1_5 + self.ans_1_1_6 + self.ans_1_1_7 + self.ans_1_1_8 + self.ans_1_1_9 + self.ans_1_1_10 + self.ans_1_1_11 + self.ans_1_1_12 + self.ans_1_1_13 +  self.ans_1_1_14 + self.ans_1_1_15 + self.ans_1_1_16 + self.ans_1_1_17 + self.ans_1_1_18 + self.ans_1_1_19 + self.ans_1_1_20
        + self.ans_1_2_1 + self.ans_1_2_2 + self.ans_1_2_3 + self.ans_1_2_4 + self.ans_1_2_5 + self.ans_1_2_6 + self.ans_1_2_7 + self.ans_1_2_8 + self.ans_1_2_9 + self.ans_1_2_10 + self.ans_1_2_11 
        + self.ans_1_3_1 + self.ans_1_3_2 + self.ans_1_3_3 + self.ans_1_3_4 
        + self.ans_1_4_1 + self.ans_1_4_2 + self.ans_1_4_3 + self.ans_1_4_4 
        + self.ans_1_5_1 + self.ans_1_5_2 
        + self.ans_1_6_1 + self.ans_1_6_2 + self.ans_1_6_3 + self.ans_1_6_4
        return (summary)

    def get_exclusive_summary(self):
        summary = self.ans_2_1_1 + self.ans_2_1_2 + self.ans_2_1_3 + self.ans_2_1_4 + self.ans_2_1_5 + self.ans_2_1_6
        + self.ans_2_2_1 + self.ans_2_2_2 + self.ans_2_2_3 + self.ans_2_2_4 + self.ans_2_2_5 + self.ans_2_2_6 + self.ans_2_2_7
        return (summary)

    def get_expertise_summary(self):
        summary = self.ans_3_1_1 + self.ans_3_1_2 + self.ans_3_1_3 + self.ans_3_1_4 + self.ans_3_1_5 
        + self.ans_3_2_1 + self.ans_3_2_2 + self.ans_3_2_3
        return (summary)

    def get_exclusive_summary(self):
        summary = self.ans_4_1_1 + self.ans_4_1_2 + self.ans_4_1_3 + self.ans_4_1_4 + self.ans_4_1_5 + self.ans_4_1_6 + self.ans_4_1_7 + self.ans_4_1_8 + self.ans_4_1_9 + self.ans_4_1_10 + self.ans_4_1_11 + self.ans_4_1_12 + self.ans_4_1_13 + self.ans_4_1_14 + self.ans_4_1_15 + self.ans_4_1_16 + self.ans_4_1_17
        + self.ans_4_2_1 + self.ans_4_2_2 + self.ans_4_2_3 + self.ans_4_2_4 + self.ans_4_2_5 + self.ans_4_2_6 + self.ans_4_2_7 + self.ans_4_2_8 + self.ans_4_2_9 + self.ans_4_2_10 + self.ans_4_2_11 
        + self.ans_4_3_1 + self.ans_4_3_2 + self.ans_4_3_3 + self.ans_4_3_4 + self.ans_4_3_5 + self.ans_4_3_6 + self.ans_4_3_7 + self.ans_4_3_8 + self.ans_4_3_9 + self.ans_4_3_10
        + self.ans_4_4_1 + self.ans_4_4_2
        + self.ans_4_5_1 + self.ans_4_5_2 + self.ans_4_5_3 + self.ans_4_5_4 + self.ans_4_5_5 + self.ans_4_5_6
        + self.ans_4_6_1 + self.ans_4_6_2 + self.ans_4_6_3 + self.ans_4_6_4 + self.ans_4_6_5 + self.ans_4_6_6
        return (summary)

    def get_exceptional_summary(self):
        summary = self.ans_5_1_1 + self.ans_5_1_2 + self.ans_5_1_3 + self.ans_5_1_4
        + self.ans_5_2_1 + self.ans_5_2_2 + self.ans_5_2_3 + self.ans_5_2_4 
        + self.ans_5_3_1 + self.ans_5_3_2 + self.ans_5_3_3 + self.ans_5_3_4 + self.ans_5_3_5 + self.ans_5_3_6 + self.ans_5_3_7
        + self.ans_5_4_1 + self.ans_5_4_2 + self.ans_5_4_3 + self.ans_5_4_4
        return (summary)

    def get_scale_points(self, val):
        switcher = {
                'มากที่สุด'    :5,
                'มาก'       :4,
                'ปานกลาง'   :3,
                'น้อย'       :2,
                'น้อยที่สุด'    :1
                }
        return switcher.get(val, "Invalid scale value")

    def get_list(self):
        return([
            self.ans_timestamp,
            self.ans_location,
            self.ans_assessor,
            self.ans_gender,
            self.ans_age,
            self.ans_income,
            self.ans_education,
            self.ans_carreer,
            self.ans_marital_status,
            self.ans_region,
            self.ans_best_tourist_attraction,

            self.ans_1_1_1,
            self.ans_1_1_2,
            self.ans_1_1_3,
            self.ans_1_1_4,
            self.ans_1_1_5,
            self.ans_1_1_6,
            self.ans_1_1_7,
            self.ans_1_1_8,
            self.ans_1_1_9,
            self.ans_1_1_10,
            self.ans_1_1_11,
            self.ans_1_1_12,
            self.ans_1_1_13,
            self.ans_1_1_14,
            self.ans_1_1_15,
            self.ans_1_1_16,
            self.ans_1_1_17,
            self.ans_1_1_18,
            self.ans_1_1_19,
            self.ans_1_1_20,

            self.ans_1_2_1,
            self.ans_1_2_2,
            self.ans_1_2_3,
            self.ans_1_2_4,
            self.ans_1_2_5,
            self.ans_1_2_6,
            self.ans_1_2_7,
            self.ans_1_2_8,
            self.ans_1_2_9,
            self.ans_1_2_10,
            self.ans_1_2_11,

            self.ans_1_3_1,
            self.ans_1_3_2,
            self.ans_1_3_3,
            self.ans_1_3_4,

            self.ans_1_4_1,
            self.ans_1_4_2,
            self.ans_1_4_3,
            self.ans_1_4_4,

            self.ans_1_5_1,
            self.ans_1_5_2,

            self.ans_1_6_1,
            self.ans_1_6_2,
            self.ans_1_6_3,
            self.ans_1_6_4,

            self.ans_2_1_1,
            self.ans_2_1_2,
            self.ans_2_1_3,
            self.ans_2_1_4,
            self.ans_2_1_5,
            self.ans_2_1_6,

            self.ans_2_2_1,
            self.ans_2_2_2,
            self.ans_2_2_3,
            self.ans_2_2_4,
            self.ans_2_2_5,
            self.ans_2_2_6,
            self.ans_2_2_7,

            self.ans_3_1_1,
            self.ans_3_1_2,
            self.ans_3_1_3,
            self.ans_3_1_4,
            self.ans_3_1_5,

            self.ans_3_2_1,
            self.ans_3_2_2,
            self.ans_3_2_3,

            self.ans_4_1_1,
            self.ans_4_1_2,
            self.ans_4_1_3,
            self.ans_4_1_4,
            self.ans_4_1_5,
            self.ans_4_1_6,
            self.ans_4_1_7,
            self.ans_4_1_8,
            self.ans_4_1_9,
            self.ans_4_1_10,
            self.ans_4_1_11,
            self.ans_4_1_12,
            self.ans_4_1_13,
            self.ans_4_1_14,
            self.ans_4_1_15,
            self.ans_4_1_16,
            self.ans_4_1_17,

            self.ans_4_2_1,
            self.ans_4_2_2,
            self.ans_4_2_3,
            self.ans_4_2_4,
            self.ans_4_2_5,
            self.ans_4_2_6,
            self.ans_4_2_7,
            self.ans_4_2_8,
            self.ans_4_2_9,
            self.ans_4_2_10,
            self.ans_4_2_11,

            self.ans_4_3_1,
            self.ans_4_3_2,
            self.ans_4_3_3,
            self.ans_4_3_4,
            self.ans_4_3_5,
            self.ans_4_3_6,
            self.ans_4_3_7,
            self.ans_4_3_8,
            self.ans_4_3_9,
            self.ans_4_3_10,

            self.ans_4_4_1,
            self.ans_4_4_2,

            self.ans_4_5_1,
            self.ans_4_5_2,
            self.ans_4_5_3,
            self.ans_4_5_4,
            self.ans_4_5_5,
            self.ans_4_5_6,

            self.ans_4_6_1,
            self.ans_4_6_2,
            self.ans_4_6_3,
            self.ans_4_6_4,
            self.ans_4_6_5,
            self.ans_4_6_6,

            self.ans_5_1_1,
            self.ans_5_1_2,
            self.ans_5_1_3,
            self.ans_5_1_4,

            self.ans_5_2_1,
            self.ans_5_2_2,
            self.ans_5_2_3,
            self.ans_5_2_4,

            self.ans_5_3_1,
            self.ans_5_3_2,
            self.ans_5_3_3,
            self.ans_5_3_4,
            self.ans_5_3_5,
            self.ans_5_3_6,
            self.ans_5_3_7,

            self.ans_5_4_1,
            self.ans_5_4_2,
            self.ans_5_4_3,
            self.ans_5_4_4,

            self.ans_experience,
            self.ans_exclusive,
            self.ans_expertise,
            self.ans_exceptional,
            self.ans_excellence,
            ])


def filter_by_location(seq, location):
    for el in seq:
        if el.ans_location==location: yield el


hvd_tourguide = WorkSheet('1fSMVe883ATrG14noEwaDJ7uSDzt6YFOLrMMLPT0ELH0')

# pprint.pprint(hvd_tourguide.sheet[0].get_list())
# pprint.pprint(hvd_tourguide.sheet[1].get_list())

# pprint.pprint(hvd_tourguide.sheets[0].questionnaire.documents[0].get_set())
# print(hvd_tourguide.sheets[0].questionnaire.documents[1].get_set())
# print(len(hvd_tourguide.sheets[0].questionnaire.documents))
# print(hvd_tourguide.sheets[0].questionnaire.document_count)
# pprint.pprint(type(hvd_tourguide.sheet[0].questionnaire.documents()))

# pprint.pprint(hvd_tourguide.sheet[0].questionnaire[0].get_list())

# filtered = list(filter_by_location(hvd_tourguide.sheet[0].questionnaire, 'เกาะรอก'))
# print(len(filtered))
# print(filtered[0].ans_assessor)
# print(filtered[1].ans_assessor)
# print(filtered[2].ans_assessor)

pprint.pprint(hvd_tourguide.sheet[0].questionnaire[1].ans_assessor)
pprint.pprint(hvd_tourguide.sheet[0].questionnaire[1].get_experience_summary())
pprint.pprint(hvd_tourguide.sheet[0].questionnaire[1].get_exclusive_summary())
pprint.pprint(hvd_tourguide.sheet[0].questionnaire[1].get_expertise_summary())
pprint.pprint(hvd_tourguide.sheet[0].questionnaire[1].get_exceptional_summary())
# pprint.pprint(hvd_tourguide.sheet[0].questionnaire[1].get_excellence_summary())
