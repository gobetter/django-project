import pprint
import json
import requests
import itertools

from statistics import mean
from collections import OrderedDict

class Questionnaire:
    def __init__(self, questionnaire_dict):
        self.q_dict = questionnaire_dict

        self.timestamp               = self.q_dict['gsx$timestamp']['$t']
        self.location                = self.q_dict['gsx$location']['$t']
        self.assessor                = self.q_dict['gsx$assessor']['$t']
        self.gender                  = self.q_dict['gsx$gender']['$t']
        self.age                     = self.q_dict['gsx$age']['$t']
        self.income                  = self.q_dict['gsx$income']['$t']
        self.education               = self.q_dict['gsx$education']['$t']
        self.carreer                 = self.q_dict['gsx$carreer']['$t']
        self.marital_status          = self.q_dict['gsx$maritalstatus']['$t']
        self.region                  = self.q_dict['gsx$region']['$t']
        self.best_tourist_attraction = self.q_dict['gsx$besttouristattraction']['$t']

        self.experience              = self.q_dict['gsx$experience']['$t']
        self.exclusive               = self.q_dict['gsx$exclusive']['$t']
        self.expertise               = self.q_dict['gsx$expertise']['$t']
        self.exceptional             = self.q_dict['gsx$exceptional']['$t']
        self.excellence              = self.q_dict['gsx$excellence']['$t']

    def __str__(self):
        return f"Timestamp: {self.timestamp} -> Location: {self.location}"

    def get_scale_points(self, val):
        switcher = {
                'มากที่สุด'    :5,
                'มาก'       :4,
                'ปานกลาง'   :3,
                'น้อย'       :2,
                'น้อยที่สุด'    :1
                }
        return switcher.get(val, "ไม่ได้ตอบ")


class TourGuide(Questionnaire):
    def __init__(self, questionnaire_dict):
        Questionnaire.__init__(self, questionnaire_dict)

        self.ans_1_1_1  = self.get_scale_points(self.q_dict['gsx$ans111' ]['$t'])
        self.ans_1_1_2  = self.get_scale_points(self.q_dict['gsx$ans112' ]['$t'])
        self.ans_1_1_3  = self.get_scale_points(self.q_dict['gsx$ans113' ]['$t'])
        self.ans_1_1_4  = self.get_scale_points(self.q_dict['gsx$ans114' ]['$t'])
        self.ans_1_1_5  = self.get_scale_points(self.q_dict['gsx$ans115' ]['$t'])
        self.ans_1_1_6  = self.get_scale_points(self.q_dict['gsx$ans116' ]['$t'])
        self.ans_1_1_7  = self.get_scale_points(self.q_dict['gsx$ans117' ]['$t'])
        self.ans_1_1_8  = self.get_scale_points(self.q_dict['gsx$ans118' ]['$t']) 
        self.ans_1_1_9  = self.get_scale_points(self.q_dict['gsx$ans119' ]['$t'])
        self.ans_1_1_10 = self.get_scale_points(self.q_dict['gsx$ans1110']['$t'])
        self.ans_1_1_11 = self.get_scale_points(self.q_dict['gsx$ans1111']['$t'])
        self.ans_1_1_12 = self.get_scale_points(self.q_dict['gsx$ans1112']['$t'])
        self.ans_1_1_13 = self.get_scale_points(self.q_dict['gsx$ans1113']['$t'])
        self.ans_1_1_14 = self.get_scale_points(self.q_dict['gsx$ans1114']['$t'])
        self.ans_1_1_15 = self.get_scale_points(self.q_dict['gsx$ans1115']['$t'])
        self.ans_1_1_16 = self.get_scale_points(self.q_dict['gsx$ans1116']['$t'])
        self.ans_1_1_17 = self.get_scale_points(self.q_dict['gsx$ans1117']['$t'])
        self.ans_1_1_18 = self.get_scale_points(self.q_dict['gsx$ans1118']['$t'])
        self.ans_1_1_19 = self.get_scale_points(self.q_dict['gsx$ans1119']['$t'])
        self.ans_1_1_20 = self.get_scale_points(self.q_dict['gsx$ans1120']['$t'])

        self.ans_1_2_1  = self.get_scale_points(self.q_dict['gsx$ans121']['$t'])
        self.ans_1_2_2  = self.get_scale_points(self.q_dict['gsx$ans122']['$t'])
        self.ans_1_2_3  = self.get_scale_points(self.q_dict['gsx$ans123']['$t'])
        self.ans_1_2_4  = self.get_scale_points(self.q_dict['gsx$ans124']['$t'])
        self.ans_1_2_5  = self.get_scale_points(self.q_dict['gsx$ans125']['$t'])
        self.ans_1_2_6  = self.get_scale_points(self.q_dict['gsx$ans126']['$t'])
        self.ans_1_2_7  = self.get_scale_points(self.q_dict['gsx$ans127']['$t'])
        self.ans_1_2_8  = self.get_scale_points(self.q_dict['gsx$ans128']['$t'])
        self.ans_1_2_9  = self.get_scale_points(self.q_dict['gsx$ans129']['$t'])
        self.ans_1_2_10 = self.get_scale_points(self.q_dict['gsx$ans1210']['$t'])
        self.ans_1_2_11 = self.get_scale_points(self.q_dict['gsx$ans1211']['$t'])

        self.ans_1_3_1  = self.get_scale_points(self.q_dict['gsx$ans131']['$t'])
        self.ans_1_3_2  = self.get_scale_points(self.q_dict['gsx$ans132']['$t'])
        self.ans_1_3_3  = self.get_scale_points(self.q_dict['gsx$ans133']['$t'])
        self.ans_1_3_4  = self.get_scale_points(self.q_dict['gsx$ans134']['$t'])

        self.ans_1_4_1  = self.get_scale_points(self.q_dict['gsx$ans141']['$t'])
        self.ans_1_4_2  = self.get_scale_points(self.q_dict['gsx$ans142']['$t'])
        self.ans_1_4_3  = self.get_scale_points(self.q_dict['gsx$ans143']['$t'])
        self.ans_1_4_4  = self.get_scale_points(self.q_dict['gsx$ans144']['$t'])

        self.ans_1_5_1  = self.get_scale_points(self.q_dict['gsx$ans151']['$t'])
        self.ans_1_5_2  = self.get_scale_points(self.q_dict['gsx$ans152']['$t'])

        self.ans_1_6_1  = self.get_scale_points(self.q_dict['gsx$ans161']['$t'])
        self.ans_1_6_2  = self.get_scale_points(self.q_dict['gsx$ans162']['$t'])
        self.ans_1_6_3  = self.get_scale_points(self.q_dict['gsx$ans163']['$t'])
        self.ans_1_6_4  = self.get_scale_points(self.q_dict['gsx$ans164']['$t'])

        self.ans_2_1_1  = self.get_scale_points(self.q_dict['gsx$ans211']['$t'])
        self.ans_2_1_2  = self.get_scale_points(self.q_dict['gsx$ans212']['$t'])
        self.ans_2_1_3  = self.get_scale_points(self.q_dict['gsx$ans213']['$t'])
        self.ans_2_1_4  = self.get_scale_points(self.q_dict['gsx$ans214']['$t'])
        self.ans_2_1_5  = self.get_scale_points(self.q_dict['gsx$ans215']['$t'])
        self.ans_2_1_6  = self.get_scale_points(self.q_dict['gsx$ans216']['$t'])

        self.ans_2_2_1  = self.get_scale_points(self.q_dict['gsx$ans221']['$t'])
        self.ans_2_2_2  = self.get_scale_points(self.q_dict['gsx$ans222']['$t'])
        self.ans_2_2_3  = self.get_scale_points(self.q_dict['gsx$ans223']['$t'])
        self.ans_2_2_4  = self.get_scale_points(self.q_dict['gsx$ans224']['$t'])
        self.ans_2_2_5  = self.get_scale_points(self.q_dict['gsx$ans225']['$t'])
        self.ans_2_2_6  = self.get_scale_points(self.q_dict['gsx$ans226']['$t'])
        self.ans_2_2_7  = self.get_scale_points(self.q_dict['gsx$ans227']['$t'])

        self.ans_3_1_1  = self.get_scale_points(self.q_dict['gsx$ans311']['$t'])
        self.ans_3_1_2  = self.get_scale_points(self.q_dict['gsx$ans312']['$t'])
        self.ans_3_1_3  = self.get_scale_points(self.q_dict['gsx$ans313']['$t'])
        self.ans_3_1_4  = self.get_scale_points(self.q_dict['gsx$ans314']['$t'])
        self.ans_3_1_5  = self.get_scale_points(self.q_dict['gsx$ans315']['$t'])

        self.ans_3_2_1  = self.get_scale_points(self.q_dict['gsx$ans321']['$t'])
        self.ans_3_2_2  = self.get_scale_points(self.q_dict['gsx$ans322']['$t'])
        self.ans_3_2_3  = self.get_scale_points(self.q_dict['gsx$ans323']['$t'])

        self.ans_4_1_1  = self.get_scale_points(self.q_dict['gsx$ans411']['$t'])
        self.ans_4_1_2  = self.get_scale_points(self.q_dict['gsx$ans412']['$t'])
        self.ans_4_1_3  = self.get_scale_points(self.q_dict['gsx$ans413']['$t'])
        self.ans_4_1_4  = self.get_scale_points(self.q_dict['gsx$ans414']['$t'])
        self.ans_4_1_5  = self.get_scale_points(self.q_dict['gsx$ans415']['$t'])
        self.ans_4_1_6  = self.get_scale_points(self.q_dict['gsx$ans416']['$t'])
        self.ans_4_1_7  = self.get_scale_points(self.q_dict['gsx$ans417']['$t'])
        self.ans_4_1_8  = self.get_scale_points(self.q_dict['gsx$ans418']['$t'])
        self.ans_4_1_9  = self.get_scale_points(self.q_dict['gsx$ans419']['$t'])
        self.ans_4_1_10 = self.get_scale_points(self.q_dict['gsx$ans4110']['$t'])
        self.ans_4_1_11 = self.get_scale_points(self.q_dict['gsx$ans4111']['$t'])
        self.ans_4_1_12 = self.get_scale_points(self.q_dict['gsx$ans4112']['$t'])
        self.ans_4_1_13 = self.get_scale_points(self.q_dict['gsx$ans4113']['$t'])
        self.ans_4_1_14 = self.get_scale_points(self.q_dict['gsx$ans4114']['$t'])
        self.ans_4_1_15 = self.get_scale_points(self.q_dict['gsx$ans4115']['$t'])
        self.ans_4_1_16 = self.get_scale_points(self.q_dict['gsx$ans4116']['$t'])
        self.ans_4_1_17 = self.get_scale_points(self.q_dict['gsx$ans4117']['$t'])

        self.ans_4_2_1  = self.get_scale_points(self.q_dict['gsx$ans421']['$t'])
        self.ans_4_2_2  = self.get_scale_points(self.q_dict['gsx$ans422']['$t'])
        self.ans_4_2_3  = self.get_scale_points(self.q_dict['gsx$ans423']['$t'])
        self.ans_4_2_4  = self.get_scale_points(self.q_dict['gsx$ans424']['$t'])
        self.ans_4_2_5  = self.get_scale_points(self.q_dict['gsx$ans425']['$t'])
        self.ans_4_2_6  = self.get_scale_points(self.q_dict['gsx$ans426']['$t'])
        self.ans_4_2_7  = self.get_scale_points(self.q_dict['gsx$ans427']['$t'])
        self.ans_4_2_8  = self.get_scale_points(self.q_dict['gsx$ans428']['$t'])
        self.ans_4_2_9  = self.get_scale_points(self.q_dict['gsx$ans429']['$t'])
        self.ans_4_2_10 = self.get_scale_points(self.q_dict['gsx$ans4210']['$t'])
        self.ans_4_2_11 = self.get_scale_points(self.q_dict['gsx$ans4211']['$t'])

        self.ans_4_3_1  = self.get_scale_points(self.q_dict['gsx$ans431']['$t'])
        self.ans_4_3_2  = self.get_scale_points(self.q_dict['gsx$ans432']['$t'])
        self.ans_4_3_3  = self.get_scale_points(self.q_dict['gsx$ans433']['$t'])
        self.ans_4_3_4  = self.get_scale_points(self.q_dict['gsx$ans434']['$t'])
        self.ans_4_3_5  = self.get_scale_points(self.q_dict['gsx$ans435']['$t'])
        self.ans_4_3_6  = self.get_scale_points(self.q_dict['gsx$ans436']['$t'])
        self.ans_4_3_7  = self.get_scale_points(self.q_dict['gsx$ans437']['$t'])
        self.ans_4_3_8  = self.get_scale_points(self.q_dict['gsx$ans438']['$t'])
        self.ans_4_3_9  = self.get_scale_points(self.q_dict['gsx$ans439']['$t'])
        self.ans_4_3_10 = self.get_scale_points(self.q_dict['gsx$ans4310']['$t'])

        self.ans_4_4_1  = self.get_scale_points(self.q_dict['gsx$ans441']['$t'])
        self.ans_4_4_2  = self.get_scale_points(self.q_dict['gsx$ans442']['$t'])

        self.ans_4_5_1  = self.get_scale_points(self.q_dict['gsx$ans451']['$t'])
        self.ans_4_5_2  = self.get_scale_points(self.q_dict['gsx$ans452']['$t'])
        self.ans_4_5_3  = self.get_scale_points(self.q_dict['gsx$ans453']['$t'])
        self.ans_4_5_4  = self.get_scale_points(self.q_dict['gsx$ans454']['$t'])
        self.ans_4_5_5  = self.get_scale_points(self.q_dict['gsx$ans455']['$t'])
        self.ans_4_5_6  = self.get_scale_points(self.q_dict['gsx$ans456']['$t'])

        self.ans_4_6_1  = self.get_scale_points(self.q_dict['gsx$ans461']['$t'])
        self.ans_4_6_2  = self.get_scale_points(self.q_dict['gsx$ans462']['$t'])
        self.ans_4_6_3  = self.get_scale_points(self.q_dict['gsx$ans463']['$t'])
        self.ans_4_6_4  = self.get_scale_points(self.q_dict['gsx$ans464']['$t'])
        self.ans_4_6_5  = self.get_scale_points(self.q_dict['gsx$ans465']['$t'])
        self.ans_4_6_6  = self.get_scale_points(self.q_dict['gsx$ans466']['$t'])

        self.ans_5_1_1  = self.get_scale_points(self.q_dict['gsx$ans511']['$t'])
        self.ans_5_1_2  = self.get_scale_points(self.q_dict['gsx$ans512']['$t'])
        self.ans_5_1_3  = self.get_scale_points(self.q_dict['gsx$ans513']['$t'])
        self.ans_5_1_4  = self.get_scale_points(self.q_dict['gsx$ans514']['$t'])

        self.ans_5_2_1  = self.get_scale_points(self.q_dict['gsx$ans521']['$t'])
        self.ans_5_2_2  = self.get_scale_points(self.q_dict['gsx$ans522']['$t'])
        self.ans_5_2_3  = self.get_scale_points(self.q_dict['gsx$ans523']['$t'])
        self.ans_5_2_4  = self.get_scale_points(self.q_dict['gsx$ans524']['$t'])

        self.ans_5_3_1  = self.get_scale_points(self.q_dict['gsx$ans531']['$t'])
        self.ans_5_3_2  = self.get_scale_points(self.q_dict['gsx$ans532']['$t'])
        self.ans_5_3_3  = self.get_scale_points(self.q_dict['gsx$ans533']['$t'])
        self.ans_5_3_4  = self.get_scale_points(self.q_dict['gsx$ans534']['$t'])
        self.ans_5_3_5  = self.get_scale_points(self.q_dict['gsx$ans535']['$t'])
        self.ans_5_3_6  = self.get_scale_points(self.q_dict['gsx$ans536']['$t'])
        self.ans_5_3_7  = self.get_scale_points(self.q_dict['gsx$ans537']['$t'])

        self.ans_5_4_1  = self.get_scale_points(self.q_dict['gsx$ans541']['$t'])
        self.ans_5_4_2  = self.get_scale_points(self.q_dict['gsx$ans542']['$t'])
        self.ans_5_4_3  = self.get_scale_points(self.q_dict['gsx$ans543']['$t'])
        self.ans_5_4_4  = self.get_scale_points(self.q_dict['gsx$ans544']['$t'])

    def __str__(self):
        return f"----------------------\nLocation: {self.location}\nAssessor: {self.assessor}"

    def get_all_list(self):
        return([
            self.timestamp,
            self.location,
            self.assessor,
            self.gender,
            self.age,
            self.income,
            self.education,
            self.carreer,
            self.marital_status,
            self.region,
            self.best_tourist_attraction,

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

            self.experience,
            self.exclusive,
            self.expertise,
            self.exceptional,
            self.excellence,
            ])

    def get_experience_list(self):
        return ([self.ans_1_1_1 , self.ans_1_1_2 , self.ans_1_1_3 , self.ans_1_1_4 , self.ans_1_1_5 , self.ans_1_1_6 , self.ans_1_1_7 , self.ans_1_1_8 , self.ans_1_1_9 , self.ans_1_1_10 , self.ans_1_1_11 , self.ans_1_1_12 , self.ans_1_1_13 , self.ans_1_1_14 , self.ans_1_1_15 , self.ans_1_1_16 , self.ans_1_1_17 , self.ans_1_1_18 , self.ans_1_1_19 , self.ans_1_1_20
        , self.ans_1_2_1 , self.ans_1_2_2 , self.ans_1_2_3 , self.ans_1_2_4 , self.ans_1_2_5 , self.ans_1_2_6 , self.ans_1_2_7 , self.ans_1_2_8 , self.ans_1_2_9 , self.ans_1_2_10 , self.ans_1_2_11 
        , self.ans_1_3_1 , self.ans_1_3_2 , self.ans_1_3_3 , self.ans_1_3_4 
        , self.ans_1_4_1 , self.ans_1_4_2 , self.ans_1_4_3 , self.ans_1_4_4 
        , self.ans_1_5_1 , self.ans_1_5_2 
        , self.ans_1_6_1 , self.ans_1_6_2 , self.ans_1_6_3 , self.ans_1_6_4])

    def get_exclusive_list(self):
        return([self.ans_2_1_1 , self.ans_2_1_2 , self.ans_2_1_3 , self.ans_2_1_4 , self.ans_2_1_5 , self.ans_2_1_6
            , self.ans_2_2_1 , self.ans_2_2_2 , self.ans_2_2_3 , self.ans_2_2_4 , self.ans_2_2_5 , self.ans_2_2_6 , self.ans_2_2_7])

    def get_expertise_list(self):
        return ([self.ans_3_1_1 , self.ans_3_1_2 , self.ans_3_1_3 , self.ans_3_1_4 , self.ans_3_1_5 
        , self.ans_3_2_1 , self.ans_3_2_2 , self.ans_3_2_3])

    def get_exceptional_list(self):
        return ([self.ans_4_1_1 , self.ans_4_1_2 , self.ans_4_1_3 , self.ans_4_1_4 , self.ans_4_1_5 , self.ans_4_1_6 , self.ans_4_1_7 , self.ans_4_1_8 , self.ans_4_1_9 , self.ans_4_1_10 , self.ans_4_1_11 , self.ans_4_1_12 , self.ans_4_1_13 , self.ans_4_1_14 , self.ans_4_1_15 , self.ans_4_1_16 , self.ans_4_1_17
        , self.ans_4_2_1 , self.ans_4_2_2 , self.ans_4_2_3 , self.ans_4_2_4 , self.ans_4_2_5 , self.ans_4_2_6 , self.ans_4_2_7 , self.ans_4_2_8 , self.ans_4_2_9 , self.ans_4_2_10 , self.ans_4_2_11 
        , self.ans_4_3_1 , self.ans_4_3_2 , self.ans_4_3_3 , self.ans_4_3_4 , self.ans_4_3_5 , self.ans_4_3_6 , self.ans_4_3_7 , self.ans_4_3_8 , self.ans_4_3_9 , self.ans_4_3_10
        , self.ans_4_4_1 , self.ans_4_4_2
        , self.ans_4_5_1 , self.ans_4_5_2 , self.ans_4_5_3 , self.ans_4_5_4 , self.ans_4_5_5 , self.ans_4_5_6
        , self.ans_4_6_1 , self.ans_4_6_2 , self.ans_4_6_3 , self.ans_4_6_4 , self.ans_4_6_5 , self.ans_4_6_6])

    def get_excellence_list(self):
        return ([self.ans_5_1_1 , self.ans_5_1_2 , self.ans_5_1_3 , self.ans_5_1_4
        , self.ans_5_2_1 , self.ans_5_2_2 , self.ans_5_2_3 , self.ans_5_2_4 
        , self.ans_5_3_1 , self.ans_5_3_2 , self.ans_5_3_3 , self.ans_5_3_4 , self.ans_5_3_5 , self.ans_5_3_6 , self.ans_5_3_7
        , self.ans_5_4_1 , self.ans_5_4_2 , self.ans_5_4_3 , self.ans_5_4_4])


class Cultural(Questionnaire):
    def __init__(self, questionnaire_dict):
        Questionnaire.__init__(self, questionnaire_dict)

        self.ans_1_1_1  = self.get_scale_points(self.q_dict['gsx$ans111' ]['$t'])
        self.ans_1_1_2  = self.get_scale_points(self.q_dict['gsx$ans112' ]['$t'])
        self.ans_1_1_3  = self.get_scale_points(self.q_dict['gsx$ans113' ]['$t'])
        self.ans_1_1_4  = self.get_scale_points(self.q_dict['gsx$ans114' ]['$t'])
        self.ans_1_1_5  = self.get_scale_points(self.q_dict['gsx$ans115' ]['$t'])
        self.ans_1_1_6  = self.get_scale_points(self.q_dict['gsx$ans116' ]['$t'])
        self.ans_1_1_7  = self.get_scale_points(self.q_dict['gsx$ans117' ]['$t'])
        self.ans_1_1_8  = self.get_scale_points(self.q_dict['gsx$ans118' ]['$t']) 
        self.ans_1_1_9  = self.get_scale_points(self.q_dict['gsx$ans119' ]['$t'])
        self.ans_1_1_10 = self.get_scale_points(self.q_dict['gsx$ans1110']['$t'])
        self.ans_1_1_11 = self.get_scale_points(self.q_dict['gsx$ans1111']['$t'])
        self.ans_1_1_12 = self.get_scale_points(self.q_dict['gsx$ans1112']['$t'])

        self.ans_1_2_1  = self.get_scale_points(self.q_dict['gsx$ans121']['$t'])
        self.ans_1_2_2  = self.get_scale_points(self.q_dict['gsx$ans122']['$t'])
        self.ans_1_2_3  = self.get_scale_points(self.q_dict['gsx$ans123']['$t'])
        self.ans_1_2_4  = self.get_scale_points(self.q_dict['gsx$ans124']['$t'])

        self.ans_1_3_1  = self.get_scale_points(self.q_dict['gsx$ans131']['$t'])
        self.ans_1_3_2  = self.get_scale_points(self.q_dict['gsx$ans132']['$t'])
        self.ans_1_3_3  = self.get_scale_points(self.q_dict['gsx$ans133']['$t'])
        self.ans_1_3_4  = self.get_scale_points(self.q_dict['gsx$ans134']['$t'])

        self.ans_1_4_1  = self.get_scale_points(self.q_dict['gsx$ans141']['$t'])
        self.ans_1_4_2  = self.get_scale_points(self.q_dict['gsx$ans142']['$t'])
        self.ans_1_4_3  = self.get_scale_points(self.q_dict['gsx$ans143']['$t'])

        self.ans_1_5_1  = self.get_scale_points(self.q_dict['gsx$ans151']['$t'])
        self.ans_1_5_2  = self.get_scale_points(self.q_dict['gsx$ans152']['$t'])

        self.ans_1_6_1  = self.get_scale_points(self.q_dict['gsx$ans161']['$t'])
        self.ans_1_6_2  = self.get_scale_points(self.q_dict['gsx$ans162']['$t'])
        self.ans_1_6_3  = self.get_scale_points(self.q_dict['gsx$ans163']['$t'])
        self.ans_1_6_4  = self.get_scale_points(self.q_dict['gsx$ans164']['$t'])

        self.ans_2_1_1  = self.get_scale_points(self.q_dict['gsx$ans211']['$t'])
        self.ans_2_1_2  = self.get_scale_points(self.q_dict['gsx$ans212']['$t'])
        self.ans_2_1_3  = self.get_scale_points(self.q_dict['gsx$ans213']['$t'])
        self.ans_2_1_4  = self.get_scale_points(self.q_dict['gsx$ans214']['$t'])
        self.ans_2_1_5  = self.get_scale_points(self.q_dict['gsx$ans215']['$t'])
        self.ans_2_1_6  = self.get_scale_points(self.q_dict['gsx$ans216']['$t'])

        self.ans_2_2_1  = self.get_scale_points(self.q_dict['gsx$ans221']['$t'])
        self.ans_2_2_2  = self.get_scale_points(self.q_dict['gsx$ans222']['$t'])
        self.ans_2_2_3  = self.get_scale_points(self.q_dict['gsx$ans223']['$t'])

        self.ans_3_1_1  = self.get_scale_points(self.q_dict['gsx$ans311']['$t'])
        self.ans_3_1_2  = self.get_scale_points(self.q_dict['gsx$ans312']['$t'])
        self.ans_3_1_3  = self.get_scale_points(self.q_dict['gsx$ans313']['$t'])
        self.ans_3_1_4  = self.get_scale_points(self.q_dict['gsx$ans314']['$t'])
        self.ans_3_1_5  = self.get_scale_points(self.q_dict['gsx$ans315']['$t'])

        self.ans_3_2_1  = self.get_scale_points(self.q_dict['gsx$ans321']['$t'])
        self.ans_3_2_2  = self.get_scale_points(self.q_dict['gsx$ans322']['$t'])
        self.ans_3_2_3  = self.get_scale_points(self.q_dict['gsx$ans323']['$t'])

        self.ans_4_1_1  = self.get_scale_points(self.q_dict['gsx$ans411']['$t'])
        self.ans_4_1_2  = self.get_scale_points(self.q_dict['gsx$ans412']['$t'])
        self.ans_4_1_3  = self.get_scale_points(self.q_dict['gsx$ans413']['$t'])
        self.ans_4_1_4  = self.get_scale_points(self.q_dict['gsx$ans414']['$t'])
        self.ans_4_1_5  = self.get_scale_points(self.q_dict['gsx$ans415']['$t'])
        self.ans_4_1_6  = self.get_scale_points(self.q_dict['gsx$ans416']['$t'])

        self.ans_4_2_1  = self.get_scale_points(self.q_dict['gsx$ans421']['$t'])
        self.ans_4_2_2  = self.get_scale_points(self.q_dict['gsx$ans422']['$t'])
        self.ans_4_2_3  = self.get_scale_points(self.q_dict['gsx$ans423']['$t'])
        self.ans_4_2_4  = self.get_scale_points(self.q_dict['gsx$ans424']['$t'])
        self.ans_4_2_5  = self.get_scale_points(self.q_dict['gsx$ans425']['$t'])
        self.ans_4_2_6  = self.get_scale_points(self.q_dict['gsx$ans426']['$t'])

        self.ans_4_3_1  = self.get_scale_points(self.q_dict['gsx$ans431']['$t'])
        self.ans_4_3_2  = self.get_scale_points(self.q_dict['gsx$ans432']['$t'])
        self.ans_4_3_3  = self.get_scale_points(self.q_dict['gsx$ans433']['$t'])
        self.ans_4_3_4  = self.get_scale_points(self.q_dict['gsx$ans434']['$t'])
        self.ans_4_3_5  = self.get_scale_points(self.q_dict['gsx$ans435']['$t'])
        self.ans_4_3_6  = self.get_scale_points(self.q_dict['gsx$ans436']['$t'])

        self.ans_4_4_1  = self.get_scale_points(self.q_dict['gsx$ans441']['$t'])
        self.ans_4_4_2  = self.get_scale_points(self.q_dict['gsx$ans442']['$t'])
        self.ans_4_4_3  = self.get_scale_points(self.q_dict['gsx$ans443']['$t'])
        self.ans_4_4_4  = self.get_scale_points(self.q_dict['gsx$ans444']['$t'])
        self.ans_4_4_5  = self.get_scale_points(self.q_dict['gsx$ans445']['$t'])

        self.ans_4_5_1  = self.get_scale_points(self.q_dict['gsx$ans451']['$t'])
        self.ans_4_5_2  = self.get_scale_points(self.q_dict['gsx$ans452']['$t'])
        self.ans_4_5_3  = self.get_scale_points(self.q_dict['gsx$ans453']['$t'])
        self.ans_4_5_4  = self.get_scale_points(self.q_dict['gsx$ans454']['$t'])
        self.ans_4_5_5  = self.get_scale_points(self.q_dict['gsx$ans455']['$t'])
        self.ans_4_5_6  = self.get_scale_points(self.q_dict['gsx$ans456']['$t'])

        self.ans_5_1_1  = self.get_scale_points(self.q_dict['gsx$ans511']['$t'])
        self.ans_5_1_2  = self.get_scale_points(self.q_dict['gsx$ans512']['$t'])
        self.ans_5_1_3  = self.get_scale_points(self.q_dict['gsx$ans513']['$t'])
        self.ans_5_1_4  = self.get_scale_points(self.q_dict['gsx$ans514']['$t'])

        self.ans_5_2_1  = self.get_scale_points(self.q_dict['gsx$ans521']['$t'])
        self.ans_5_2_2  = self.get_scale_points(self.q_dict['gsx$ans522']['$t'])
        self.ans_5_2_3  = self.get_scale_points(self.q_dict['gsx$ans523']['$t'])

        self.ans_5_3_1  = self.get_scale_points(self.q_dict['gsx$ans531']['$t'])
        self.ans_5_3_2  = self.get_scale_points(self.q_dict['gsx$ans532']['$t'])
        self.ans_5_3_3  = self.get_scale_points(self.q_dict['gsx$ans533']['$t'])
        self.ans_5_3_4  = self.get_scale_points(self.q_dict['gsx$ans534']['$t'])
        self.ans_5_3_5  = self.get_scale_points(self.q_dict['gsx$ans535']['$t'])
        self.ans_5_3_6  = self.get_scale_points(self.q_dict['gsx$ans536']['$t'])
        self.ans_5_3_7  = self.get_scale_points(self.q_dict['gsx$ans537']['$t'])
        self.ans_5_3_8  = self.get_scale_points(self.q_dict['gsx$ans538']['$t'])

        self.ans_5_4_1  = self.get_scale_points(self.q_dict['gsx$ans541']['$t'])
        self.ans_5_4_2  = self.get_scale_points(self.q_dict['gsx$ans542']['$t'])
        self.ans_5_4_3  = self.get_scale_points(self.q_dict['gsx$ans543']['$t'])
        self.ans_5_4_4  = self.get_scale_points(self.q_dict['gsx$ans544']['$t'])

    def __str__(self):
        return f"----------------------\nLocation: {self.location}\nAssessor: {self.assessor}"

    def get_all_list(self):
        return([
            self.timestamp,
            self.location,
            self.assessor,
            self.gender,
            self.age,
            self.income,
            self.education,
            self.carreer,
            self.marital_status,
            self.region,
            self.best_tourist_attraction,

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

            self.ans_1_2_1,
            self.ans_1_2_2,
            self.ans_1_2_3,
            self.ans_1_2_4,

            self.ans_1_3_1,
            self.ans_1_3_2,
            self.ans_1_3_3,
            self.ans_1_3_4,

            self.ans_1_4_1,
            self.ans_1_4_2,
            self.ans_1_4_3,

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

            self.ans_4_2_1,
            self.ans_4_2_2,
            self.ans_4_2_3,
            self.ans_4_2_4,
            self.ans_4_2_5,
            self.ans_4_2_6,

            self.ans_4_3_1,
            self.ans_4_3_2,
            self.ans_4_3_3,
            self.ans_4_3_4,
            self.ans_4_3_5,
            self.ans_4_3_6,

            self.ans_4_4_1,
            self.ans_4_4_2,
            self.ans_4_4_3,
            self.ans_4_4_4,
            self.ans_4_4_5,

            self.ans_4_5_1,
            self.ans_4_5_2,
            self.ans_4_5_3,
            self.ans_4_5_4,
            self.ans_4_5_5,
            self.ans_4_5_6,

            self.ans_5_1_1,
            self.ans_5_1_2,
            self.ans_5_1_3,
            self.ans_5_1_4,

            self.ans_5_2_1,
            self.ans_5_2_2,
            self.ans_5_2_3,

            self.ans_5_3_1,
            self.ans_5_3_2,
            self.ans_5_3_3,
            self.ans_5_3_4,
            self.ans_5_3_5,
            self.ans_5_3_6,
            self.ans_5_3_7,
            self.ans_5_3_8,

            self.ans_5_4_1,
            self.ans_5_4_2,
            self.ans_5_4_3,
            self.ans_5_4_4,

            self.experience,
            self.exclusive,
            self.expertise,
            self.exceptional,
            self.excellence,
            ])

    def get_experience_list(self):
        return ([self.ans_1_1_1 , self.ans_1_1_2 , self.ans_1_1_3 , self.ans_1_1_4 , self.ans_1_1_5 , self.ans_1_1_6 , self.ans_1_1_7 , self.ans_1_1_8 , self.ans_1_1_9 , self.ans_1_1_10 , self.ans_1_1_11 , self.ans_1_1_12
        , self.ans_1_2_1 , self.ans_1_2_2 , self.ans_1_2_3 , self.ans_1_2_4
        , self.ans_1_3_1 , self.ans_1_3_2 , self.ans_1_3_3 , self.ans_1_3_4 
        , self.ans_1_4_1 , self.ans_1_4_2 , self.ans_1_4_3 
        , self.ans_1_5_1 , self.ans_1_5_2 
        , self.ans_1_6_1 , self.ans_1_6_2 , self.ans_1_6_3 , self.ans_1_6_4])

    def get_exclusive_list(self):
        return([self.ans_2_1_1 , self.ans_2_1_2 , self.ans_2_1_3 , self.ans_2_1_4 , self.ans_2_1_5 , self.ans_2_1_6
        , self.ans_2_2_1 , self.ans_2_2_2 , self.ans_2_2_3])

    def get_expertise_list(self):
        return ([self.ans_3_1_1 , self.ans_3_1_2 , self.ans_3_1_3 , self.ans_3_1_4 , self.ans_3_1_5 
        , self.ans_3_2_1 , self.ans_3_2_2 , self.ans_3_2_3])

    def get_exceptional_list(self):
        return ([self.ans_4_1_1 , self.ans_4_1_2 , self.ans_4_1_3 , self.ans_4_1_4 , self.ans_4_1_5 , self.ans_4_1_6
        , self.ans_4_2_1 , self.ans_4_2_2 , self.ans_4_2_3 , self.ans_4_2_4 , self.ans_4_2_5 , self.ans_4_2_6
        , self.ans_4_3_1 , self.ans_4_3_2 , self.ans_4_3_3 , self.ans_4_3_4 , self.ans_4_3_5 , self.ans_4_3_6
        , self.ans_4_4_1 , self.ans_4_4_2 , self.ans_4_4_3 , self.ans_4_4_4 , self.ans_4_4_5
        , self.ans_4_5_1 , self.ans_4_5_2 , self.ans_4_5_3 , self.ans_4_5_4 , self.ans_4_5_5 , self.ans_4_5_6])

    def get_excellence_list(self):
        return ([self.ans_5_1_1 , self.ans_5_1_2 , self.ans_5_1_3 , self.ans_5_1_4
        , self.ans_5_2_1 , self.ans_5_2_2 , self.ans_5_2_3
        , self.ans_5_3_1 , self.ans_5_3_2 , self.ans_5_3_3 , self.ans_5_3_4 , self.ans_5_3_5 , self.ans_5_3_6 , self.ans_5_3_7 , self.ans_5_3_8
        , self.ans_5_4_1 , self.ans_5_4_2 , self.ans_5_4_3 , self.ans_5_4_4])


class Accommudation(Questionnaire):
    def __init__(self, questionnaire_dict):
        Questionnaire.__init__(self, questionnaire_dict)

        self.ans_1_1_1  = self.get_scale_points(self.q_dict['gsx$ans111' ]['$t'])
        self.ans_1_1_2  = self.get_scale_points(self.q_dict['gsx$ans112' ]['$t'])
        self.ans_1_1_3  = self.get_scale_points(self.q_dict['gsx$ans113' ]['$t'])
        self.ans_1_1_4  = self.get_scale_points(self.q_dict['gsx$ans114' ]['$t'])
        self.ans_1_1_5  = self.get_scale_points(self.q_dict['gsx$ans115' ]['$t'])
        self.ans_1_1_6  = self.get_scale_points(self.q_dict['gsx$ans116' ]['$t'])
        self.ans_1_1_7  = self.get_scale_points(self.q_dict['gsx$ans117' ]['$t'])
        self.ans_1_1_8  = self.get_scale_points(self.q_dict['gsx$ans118' ]['$t']) 
        self.ans_1_1_9  = self.get_scale_points(self.q_dict['gsx$ans119' ]['$t'])
        self.ans_1_1_10 = self.get_scale_points(self.q_dict['gsx$ans1110']['$t'])
        self.ans_1_1_11 = self.get_scale_points(self.q_dict['gsx$ans1111']['$t'])
        self.ans_1_1_12 = self.get_scale_points(self.q_dict['gsx$ans1112']['$t'])
        self.ans_1_1_13 = self.get_scale_points(self.q_dict['gsx$ans1113']['$t'])
        self.ans_1_1_14 = self.get_scale_points(self.q_dict['gsx$ans1114']['$t'])
        self.ans_1_1_15 = self.get_scale_points(self.q_dict['gsx$ans1115']['$t'])
        self.ans_1_1_16 = self.get_scale_points(self.q_dict['gsx$ans1116']['$t'])
        self.ans_1_1_17 = self.get_scale_points(self.q_dict['gsx$ans1117']['$t'])
        self.ans_1_1_18 = self.get_scale_points(self.q_dict['gsx$ans1118']['$t'])

        self.ans_1_2_1  = self.get_scale_points(self.q_dict['gsx$ans121']['$t'])
        self.ans_1_2_2  = self.get_scale_points(self.q_dict['gsx$ans122']['$t'])
        self.ans_1_2_3  = self.get_scale_points(self.q_dict['gsx$ans123']['$t'])
        self.ans_1_2_4  = self.get_scale_points(self.q_dict['gsx$ans124']['$t'])
        self.ans_1_2_5  = self.get_scale_points(self.q_dict['gsx$ans125']['$t'])
        self.ans_1_2_6  = self.get_scale_points(self.q_dict['gsx$ans126']['$t'])
        self.ans_1_2_7  = self.get_scale_points(self.q_dict['gsx$ans127']['$t'])
        self.ans_1_2_8  = self.get_scale_points(self.q_dict['gsx$ans128']['$t'])
        self.ans_1_2_9  = self.get_scale_points(self.q_dict['gsx$ans129']['$t'])
        self.ans_1_2_10 = self.get_scale_points(self.q_dict['gsx$ans1210']['$t'])
        self.ans_1_2_11 = self.get_scale_points(self.q_dict['gsx$ans1211']['$t'])

        self.ans_1_3_1  = self.get_scale_points(self.q_dict['gsx$ans131']['$t'])
        self.ans_1_3_2  = self.get_scale_points(self.q_dict['gsx$ans132']['$t'])
        self.ans_1_3_3  = self.get_scale_points(self.q_dict['gsx$ans133']['$t'])
        self.ans_1_3_4  = self.get_scale_points(self.q_dict['gsx$ans134']['$t'])

        self.ans_1_4_1  = self.get_scale_points(self.q_dict['gsx$ans141']['$t'])
        self.ans_1_4_2  = self.get_scale_points(self.q_dict['gsx$ans142']['$t'])
        self.ans_1_4_3  = self.get_scale_points(self.q_dict['gsx$ans143']['$t'])
        self.ans_1_4_4  = self.get_scale_points(self.q_dict['gsx$ans144']['$t'])

        self.ans_1_5_1  = self.get_scale_points(self.q_dict['gsx$ans151']['$t'])
        self.ans_1_5_2  = self.get_scale_points(self.q_dict['gsx$ans152']['$t'])
        self.ans_1_5_3  = self.get_scale_points(self.q_dict['gsx$ans153']['$t'])

        self.ans_1_6_1  = self.get_scale_points(self.q_dict['gsx$ans161']['$t'])
        self.ans_1_6_2  = self.get_scale_points(self.q_dict['gsx$ans162']['$t'])
        self.ans_1_6_3  = self.get_scale_points(self.q_dict['gsx$ans163']['$t'])
        self.ans_1_6_4  = self.get_scale_points(self.q_dict['gsx$ans164']['$t'])

        self.ans_2_1_1  = self.get_scale_points(self.q_dict['gsx$ans211']['$t'])
        self.ans_2_1_2  = self.get_scale_points(self.q_dict['gsx$ans212']['$t'])
        self.ans_2_1_3  = self.get_scale_points(self.q_dict['gsx$ans213']['$t'])

        self.ans_2_2_1  = self.get_scale_points(self.q_dict['gsx$ans221']['$t'])
        self.ans_2_2_2  = self.get_scale_points(self.q_dict['gsx$ans222']['$t'])
        self.ans_2_2_3  = self.get_scale_points(self.q_dict['gsx$ans223']['$t'])
        self.ans_2_2_4  = self.get_scale_points(self.q_dict['gsx$ans224']['$t'])
        self.ans_2_2_5  = self.get_scale_points(self.q_dict['gsx$ans225']['$t'])

        self.ans_3_1_1  = self.get_scale_points(self.q_dict['gsx$ans311']['$t'])
        self.ans_3_1_2  = self.get_scale_points(self.q_dict['gsx$ans312']['$t'])
        self.ans_3_1_3  = self.get_scale_points(self.q_dict['gsx$ans313']['$t'])
        self.ans_3_1_4  = self.get_scale_points(self.q_dict['gsx$ans314']['$t'])

        self.ans_3_2_1  = self.get_scale_points(self.q_dict['gsx$ans321']['$t'])
        self.ans_3_2_2  = self.get_scale_points(self.q_dict['gsx$ans322']['$t'])

        self.ans_4_1_1  = self.get_scale_points(self.q_dict['gsx$ans411']['$t'])
        self.ans_4_1_2  = self.get_scale_points(self.q_dict['gsx$ans412']['$t'])
        self.ans_4_1_3  = self.get_scale_points(self.q_dict['gsx$ans413']['$t'])
        self.ans_4_1_4  = self.get_scale_points(self.q_dict['gsx$ans414']['$t'])
        self.ans_4_1_5  = self.get_scale_points(self.q_dict['gsx$ans415']['$t'])
        self.ans_4_1_6  = self.get_scale_points(self.q_dict['gsx$ans416']['$t'])
        self.ans_4_1_7  = self.get_scale_points(self.q_dict['gsx$ans417']['$t'])

        self.ans_4_2_1  = self.get_scale_points(self.q_dict['gsx$ans421']['$t'])
        self.ans_4_2_2  = self.get_scale_points(self.q_dict['gsx$ans422']['$t'])
        self.ans_4_2_3  = self.get_scale_points(self.q_dict['gsx$ans423']['$t'])
        self.ans_4_2_4  = self.get_scale_points(self.q_dict['gsx$ans424']['$t'])
        self.ans_4_2_5  = self.get_scale_points(self.q_dict['gsx$ans425']['$t'])
        self.ans_4_2_6  = self.get_scale_points(self.q_dict['gsx$ans426']['$t'])
        self.ans_4_2_7  = self.get_scale_points(self.q_dict['gsx$ans427']['$t'])
        self.ans_4_2_8  = self.get_scale_points(self.q_dict['gsx$ans428']['$t'])

        self.ans_4_3_1  = self.get_scale_points(self.q_dict['gsx$ans431']['$t'])
        self.ans_4_3_2  = self.get_scale_points(self.q_dict['gsx$ans432']['$t'])
        self.ans_4_3_3  = self.get_scale_points(self.q_dict['gsx$ans433']['$t'])
        self.ans_4_3_4  = self.get_scale_points(self.q_dict['gsx$ans434']['$t'])
        self.ans_4_3_5  = self.get_scale_points(self.q_dict['gsx$ans435']['$t'])
        self.ans_4_3_6  = self.get_scale_points(self.q_dict['gsx$ans436']['$t'])
        self.ans_4_3_7  = self.get_scale_points(self.q_dict['gsx$ans437']['$t'])
        self.ans_4_3_8  = self.get_scale_points(self.q_dict['gsx$ans438']['$t'])
        self.ans_4_3_9  = self.get_scale_points(self.q_dict['gsx$ans439']['$t'])
        self.ans_4_3_10 = self.get_scale_points(self.q_dict['gsx$ans4310']['$t'])

        self.ans_4_4_1  = self.get_scale_points(self.q_dict['gsx$ans441']['$t'])
        self.ans_4_4_2  = self.get_scale_points(self.q_dict['gsx$ans442']['$t'])

        self.ans_4_5_1  = self.get_scale_points(self.q_dict['gsx$ans451']['$t'])
        self.ans_4_5_2  = self.get_scale_points(self.q_dict['gsx$ans452']['$t'])
        self.ans_4_5_3  = self.get_scale_points(self.q_dict['gsx$ans453']['$t'])
        self.ans_4_5_4  = self.get_scale_points(self.q_dict['gsx$ans454']['$t'])
        self.ans_4_5_5  = self.get_scale_points(self.q_dict['gsx$ans455']['$t'])

        self.ans_4_6_1  = self.get_scale_points(self.q_dict['gsx$ans461']['$t'])
        self.ans_4_6_2  = self.get_scale_points(self.q_dict['gsx$ans462']['$t'])
        self.ans_4_6_3  = self.get_scale_points(self.q_dict['gsx$ans463']['$t'])
        self.ans_4_6_4  = self.get_scale_points(self.q_dict['gsx$ans464']['$t'])
        self.ans_4_6_5  = self.get_scale_points(self.q_dict['gsx$ans465']['$t'])
        self.ans_4_6_6  = self.get_scale_points(self.q_dict['gsx$ans466']['$t'])

        self.ans_4_7_1  = self.get_scale_points(self.q_dict['gsx$ans471']['$t'])
        self.ans_4_7_2  = self.get_scale_points(self.q_dict['gsx$ans472']['$t'])
        self.ans_4_7_3  = self.get_scale_points(self.q_dict['gsx$ans473']['$t'])
        self.ans_4_7_4  = self.get_scale_points(self.q_dict['gsx$ans474']['$t'])

        self.ans_4_8_1  = self.get_scale_points(self.q_dict['gsx$ans481']['$t'])
        self.ans_4_8_2  = self.get_scale_points(self.q_dict['gsx$ans482']['$t'])
        self.ans_4_8_3  = self.get_scale_points(self.q_dict['gsx$ans483']['$t'])
        self.ans_4_8_4  = self.get_scale_points(self.q_dict['gsx$ans484']['$t'])
        self.ans_4_8_5  = self.get_scale_points(self.q_dict['gsx$ans485']['$t'])
        self.ans_4_8_6  = self.get_scale_points(self.q_dict['gsx$ans486']['$t'])
        self.ans_4_8_7  = self.get_scale_points(self.q_dict['gsx$ans487']['$t'])
        self.ans_4_8_8  = self.get_scale_points(self.q_dict['gsx$ans488']['$t'])
        self.ans_4_8_9  = self.get_scale_points(self.q_dict['gsx$ans489']['$t'])
        self.ans_4_8_10 = self.get_scale_points(self.q_dict['gsx$ans4810']['$t'])

        self.ans_5_1_1  = self.get_scale_points(self.q_dict['gsx$ans511']['$t'])
        self.ans_5_1_2  = self.get_scale_points(self.q_dict['gsx$ans512']['$t'])
        self.ans_5_1_3  = self.get_scale_points(self.q_dict['gsx$ans513']['$t'])
        self.ans_5_1_4  = self.get_scale_points(self.q_dict['gsx$ans514']['$t'])

        self.ans_5_2_1  = self.get_scale_points(self.q_dict['gsx$ans521']['$t'])
        self.ans_5_2_2  = self.get_scale_points(self.q_dict['gsx$ans522']['$t'])
        self.ans_5_2_3  = self.get_scale_points(self.q_dict['gsx$ans523']['$t'])
        self.ans_5_2_4  = self.get_scale_points(self.q_dict['gsx$ans524']['$t'])

        self.ans_5_3_1  = self.get_scale_points(self.q_dict['gsx$ans531']['$t'])
        self.ans_5_3_2  = self.get_scale_points(self.q_dict['gsx$ans532']['$t'])
        self.ans_5_3_3  = self.get_scale_points(self.q_dict['gsx$ans533']['$t'])
        self.ans_5_3_4  = self.get_scale_points(self.q_dict['gsx$ans534']['$t'])
        self.ans_5_3_5  = self.get_scale_points(self.q_dict['gsx$ans535']['$t'])
        self.ans_5_3_6  = self.get_scale_points(self.q_dict['gsx$ans536']['$t'])
        self.ans_5_3_7  = self.get_scale_points(self.q_dict['gsx$ans537']['$t'])

        self.ans_5_4_1  = self.get_scale_points(self.q_dict['gsx$ans541']['$t'])
        self.ans_5_4_2  = self.get_scale_points(self.q_dict['gsx$ans542']['$t'])
        self.ans_5_4_3  = self.get_scale_points(self.q_dict['gsx$ans543']['$t'])
        self.ans_5_4_4  = self.get_scale_points(self.q_dict['gsx$ans544']['$t'])

    def __str__(self):
        return f"----------------------\nLocation: {self.location}\nAssessor: {self.assessor}"

    def get_all_list(self):
        return([
            self.timestamp,
            self.location,
            self.assessor,
            self.gender,
            self.age,
            self.income,
            self.education,
            self.carreer,
            self.marital_status,
            self.region,
            self.best_tourist_attraction,

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
            self.ans_1_5_3,

            self.ans_1_6_1,
            self.ans_1_6_2,
            self.ans_1_6_3,
            self.ans_1_6_4,

            self.ans_2_1_1,
            self.ans_2_1_2,
            self.ans_2_1_3,

            self.ans_2_2_1,
            self.ans_2_2_2,
            self.ans_2_2_3,
            self.ans_2_2_4,
            self.ans_2_2_5,

            self.ans_3_1_1,
            self.ans_3_1_2,
            self.ans_3_1_3,
            self.ans_3_1_4,

            self.ans_3_2_1,
            self.ans_3_2_2,

            self.ans_4_1_1,
            self.ans_4_1_2,
            self.ans_4_1_3,
            self.ans_4_1_4,
            self.ans_4_1_5,
            self.ans_4_1_6,
            self.ans_4_1_7,

            self.ans_4_2_1,
            self.ans_4_2_2,
            self.ans_4_2_3,
            self.ans_4_2_4,
            self.ans_4_2_5,
            self.ans_4_2_6,
            self.ans_4_2_7,
            self.ans_4_2_8,

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

            self.ans_4_6_1,
            self.ans_4_6_2,
            self.ans_4_6_3,
            self.ans_4_6_4,
            self.ans_4_6_5,
            self.ans_4_6_6,

            self.ans_4_7_1,
            self.ans_4_7_2,
            self.ans_4_7_3,
            self.ans_4_7_4,

            self.ans_4_8_1,
            self.ans_4_8_2,
            self.ans_4_8_3,
            self.ans_4_8_4,
            self.ans_4_8_5,
            self.ans_4_8_6,
            self.ans_4_8_7,
            self.ans_4_8_8,
            self.ans_4_8_9,
            self.ans_4_8_10,

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

            self.experience,
            self.exclusive,
            self.expertise,
            self.exceptional,
            self.excellence,
            ])

    def get_experience_list(self):
        return ([self.ans_1_1_1 , self.ans_1_1_2 , self.ans_1_1_3 , self.ans_1_1_4 , self.ans_1_1_5 , self.ans_1_1_6 , self.ans_1_1_7 , self.ans_1_1_8 , self.ans_1_1_9 , self.ans_1_1_10 , self.ans_1_1_11 , self.ans_1_1_12 , self.ans_1_1_13 , self.ans_1_1_14 , self.ans_1_1_15 , self.ans_1_1_16 , self.ans_1_1_17
        , self.ans_1_2_1 , self.ans_1_2_2 , self.ans_1_2_3 , self.ans_1_2_4 , self.ans_1_2_5 , self.ans_1_2_6 , self.ans_1_2_7 , self.ans_1_2_8 , self.ans_1_2_9 , self.ans_1_2_10 , self.ans_1_2_11
        , self.ans_1_3_1 , self.ans_1_3_2 , self.ans_1_3_3 , self.ans_1_3_4
        , self.ans_1_4_1 , self.ans_1_4_2 , self.ans_1_4_3 , self.ans_1_4_4
        , self.ans_1_5_1 , self.ans_1_5_2 , self.ans_1_5_3
        , self.ans_1_6_1 , self.ans_1_6_2 , self.ans_1_6_3 , self.ans_1_6_4])

    def get_exclusive_list(self):
        return([self.ans_2_1_1 , self.ans_2_1_2 , self.ans_2_1_3
            , self.ans_2_2_1 , self.ans_2_2_2 , self.ans_2_2_3 , self.ans_2_2_4 , self.ans_2_2_5])

    def get_expertise_list(self):
        return ([self.ans_3_1_1 , self.ans_3_1_2 , self.ans_3_1_3 , self.ans_3_1_4
        , self.ans_3_2_1 , self.ans_3_2_2])

    def get_exceptional_list(self):
        return ([self.ans_4_1_1 , self.ans_4_1_2 , self.ans_4_1_3 , self.ans_4_1_4 , self.ans_4_1_5 , self.ans_4_1_6 , self.ans_4_1_7
        , self.ans_4_2_1 , self.ans_4_2_2 , self.ans_4_2_3 , self.ans_4_2_4 , self.ans_4_2_5 , self.ans_4_2_6 , self.ans_4_2_7 , self.ans_4_2_8
        , self.ans_4_3_1 , self.ans_4_3_2 , self.ans_4_3_3 , self.ans_4_3_4 , self.ans_4_3_5 , self.ans_4_3_6 , self.ans_4_3_7 , self.ans_4_3_8 , self.ans_4_3_9 , self.ans_4_3_10
        , self.ans_4_4_1 , self.ans_4_4_2
        , self.ans_4_5_1 , self.ans_4_5_2 , self.ans_4_5_3 , self.ans_4_5_4 , self.ans_4_5_5
        , self.ans_4_6_1 , self.ans_4_6_2 , self.ans_4_6_3 , self.ans_4_6_4 , self.ans_4_6_5 , self.ans_4_6_6
        , self.ans_4_7_1 , self.ans_4_7_2 , self.ans_4_7_3 , self.ans_4_7_4 , self.ans_4_5_5
        , self.ans_4_8_1 , self.ans_4_8_2 , self.ans_4_8_3 , self.ans_4_8_4 , self.ans_4_8_5 , self.ans_4_8_6 , self.ans_4_8_7 , self.ans_4_8_8 , self.ans_4_8_9 , self.ans_4_8_10])

    def get_excellence_list(self):
        return ([self.ans_5_1_1 , self.ans_5_1_2 , self.ans_5_1_3 , self.ans_5_1_4
        , self.ans_5_2_1 , self.ans_5_2_2 , self.ans_5_2_3 , self.ans_5_2_4 
        , self.ans_5_3_1 , self.ans_5_3_2 , self.ans_5_3_3 , self.ans_5_3_4 , self.ans_5_3_5 , self.ans_5_3_6 , self.ans_5_3_7
        , self.ans_5_4_1 , self.ans_5_4_2 , self.ans_5_4_3 , self.ans_5_4_4])

class Questionnaires:
    def __init__(self, questionnaire_type, q_url):
        self.questionnaire_type = questionnaire_type
        self.url                = q_url
        self.questionnaires     = self.get_questionnaires()

    def get_questionnaires(self):
        url_json    = self.url + '?alt=json'
        json_string = requests.get(url_json)
        json_dict   = json_string.json()
        questionnaires = []

        for q in json_dict['feed']['entry']:
            questionnaires.append(self.questionnaire_type(q))

        return questionnaires

    def filter_by_location_list(self, location):
        # filtered_list = [q for q in self.questionnaires if q.location == location]
        filtered_list = filter(lambda q: q.location==location, self.questionnaires)

        return filtered_list

    # def filter_by_location_generator(self, location):
    #     for el in self.questionnaire:
    #         if el.ans_location==location: yield el


sheet_url_tourguide     = 'https://spreadsheets.google.com/feeds/list/1fSMVe883ATrG14noEwaDJ7uSDzt6YFOLrMMLPT0ELH0/oummhpi/public/values'
sheet_url_cultural       = 'https://spreadsheets.google.com/feeds/list/1x3PxQsyTnosVGDoirbTLy529_go0gZ4anjGrXGjEOWs/of7djn6/public/values'
# sheet_url_accommudation = 'https://spreadsheets.google.com/feeds/list/1Mp_8iK4sm8ROh50_reBJSA7vXeb57xJAI-k9EbhBc_E/ohlbicy/public/values'
sheet_url_accommudation = 'https://spreadsheets.google.com/feeds/list/1Av30Ms3Nu5NCCo-UtMbw1QSqAvlk_XEPSMAbgwX5YmQ/odfz5k7/public/values'

# rq = Questionnaires(Questionnaire, sheet_url_tourguide)
q_type = Questionnaires(TourGuide, sheet_url_tourguide)
# rq = Questionnaires(Cultural, sheet_url_cultural)
# rq = Questionnaires(Accommudation, sheet_url_accommudation)

# for q in rq.questionnaires:
#     # print(q)
#     # print(q.get_experience_list())

#     f"------- {print(q.location)} -------"
#     print(mean(q.get_experience_list()))
#     print(mean(q.get_exclusive_list()))
#     print(mean(q.get_expertise_list()))
#     print(mean(q.get_exceptional_list()))
#     print(mean(q.get_excellence_list()))


# for q in rq.filter_by_location_list("เกาะรอก"):
#     print(q.location)
#     print(q.get_experience_list())

# print("*********************************************************")
# for q in rq.filter_by_location_list("ว้ดถ้ำเสือ"):
#     f"------- {print(q.location)} -------"
#     print(mean(q.get_experience_list()))
#     print(mean(q.get_exclusive_list()))
#     print(mean(q.get_expertise_list()))
#     print(mean(q.get_exceptional_list()))
#     print(mean(q.get_excellence_list()))


# for q in rq.questionnaires:
#     print(q.location)

# print("*********************************************************")

location_names =[q.location for q in q_type.questionnaires]
location_names_ordered = list(OrderedDict.fromkeys(location_names))
data = []

for location in location_names_ordered:
    # print(f"---- {location} ----")
    experience_list     = list(itertools.chain(*[filtered_q.get_experience_list() for filtered_q in q_type.filter_by_location_list(location)]))
    exclusive_list      = list(itertools.chain(*[filtered_q.get_exclusive_list() for filtered_q in q_type.filter_by_location_list(location)]))
    expertise_list      = list(itertools.chain(*[filtered_q.get_expertise_list() for filtered_q in q_type.filter_by_location_list(location)]))
    exceptional_list    = list(itertools.chain(*[filtered_q.get_exceptional_list() for filtered_q in q_type.filter_by_location_list(location)]))
    excellence_list     = list(itertools.chain(*[filtered_q.get_excellence_list() for filtered_q in q_type.filter_by_location_list(location)]))

    data.append([location, [
        mean(experience_list),
        mean(exclusive_list),
        mean(expertise_list),
        mean(exceptional_list),
        mean(excellence_list)
        ]])
