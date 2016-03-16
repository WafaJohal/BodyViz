import csv

fname="/Users/wafajohal/Dropbox/DATA/STYLEBOT/child4_dance.csv"
all_data = []
map_joints={0:"JointType_SpineBase", 1:"JointType_SpineMid", 2:
"JointType_Neck", 3:"JointType_Head", 4:"JointType_ShoulderLeft", 5:
"JointType_ElbowLeft", 6:"JointType_WristLeft", 7:
"JointType_HandLeft", 8:"JointType_ShoulderRight", 9:
"JointType_ElbowRight", 10:"JointType_WristRight", 11:
"JointType_HandRight", 12:"JointType_HipLeft", 13:
"JointType_KneeLeft", 14:"JointType_AnkleLeft", 15:
"JointType_FootLeft", 16:"JointType_HipRight", 17:
"JointType_KneeRight", 18:"JointType_AnkleRight", 19:
"JointType_FootRight", 20:"JointType_SpineShoulder", 21:
"JointType_HandTipLeft", 22:"JointType_ThumbLeft", 23:
"JointType_HandTipRight", 24:"JointType_ThumbRight"}
count = 0
header = ("", "X.1", "X", "activity", "style", "versatility", "session", "child", "time", "id", "nbbodyke", "JointP_SpineBase_X", "JointP_SpineMid_X", "JointP_Neck_X", "JointP_Head_X", "JointP_ShoulderLeft_X", "JointP_ElbowLeft_X", "JointP_WristLeft_X", "JointP_HandLeft_X", "JointP_ShoulderRight_X", "JointP_ElbowRight_X", "JointP_WristRight_X", "JointP_HandRight_X", "JointP_HipLeft_X", "JointP_KneeLeft_X", "JointP_AnkleLeft_X", "JointP_FootLeft_X", "JointP_HipRight_X", "JointP_KneeRight_X", "JointP_AnkleRight_X", "JointP_FootRight_X", "JointP_SpineShoulder_X", "JointP_HandTipLeft_X", "JointP_ThumbLeft_X", "JointP_HandTipRight_X", "JointP_ThumbRight_X", "JointO_SpineBase_X", "JointO_SpineMid_X", "JointO_Neck_X", "JointO_Head_X", "JointO_ShoulderLeft_X", "JointO_ElbowLeft_X", "JointO_WristLeft_X", "JointO_HandLeft_X", "JointO_ShoulderRight_X", "JointO_ElbowRight_X", "JointO_WristRight_X", "JointO_HandRight_X", "JointO_HipLeft_X", "JointO_KneeLeft_X", "JointO_AnkleLeft_X", "JointO_FootLeft_X", "JointO_HipRight_X", "JointO_KneeRight_X", "JointO_AnkleRight_X", "JointO_FootRight_X", "JointO_SpineShoulder_X", "JointO_HandTipLeft_X", "JointO_ThumbLeft_X", "JointO_HandTipRight_X", "JointO_ThumbRight_X", "JointP_SpineBase_Y", "JointP_SpineMid_Y", "JointP_Neck_Y", "JointP_Head_Y", "JointP_ShoulderLeft_Y", "JointP_ElbowLeft_Y", "JointP_WristLeft_Y", "JointP_HandLeft_Y", "JointP_ShoulderRight_Y", "JointP_ElbowRight_Y", "JointP_WristRight_Y", "JointP_HandRight_Y", "JointP_HipLeft_Y", "JointP_KneeLeft_Y", "JointP_AnkleLeft_Y", "JointP_FootLeft_Y", "JointP_HipRight_Y", "JointP_KneeRight_Y", "JointP_AnkleRight_Y", "JointP_FootRight_Y", "JointP_SpineShoulder_Y", "JointP_HandTipLeft_Y", "JointP_ThumbLeft_Y", "JointP_HandTipRight_Y", "JointP_ThumbRight_Y", "JointO_SpineBase_Y", "JointO_SpineMid_Y", "JointO_Neck_Y", "JointO_Head_Y", "JointO_ShoulderLeft_Y", "JointO_ElbowLeft_Y", "JointO_WristLeft_Y", "JointO_HandLeft_Y", "JointO_ShoulderRight_Y", "JointO_ElbowRight_Y", "JointO_WristRight_Y",
          "JointO_HandRight_Y", "JointO_HipLeft_Y", "JointO_KneeLeft_Y", "JointO_AnkleLeft_Y", "JointO_FootLeft_Y", "JointO_HipRight_Y", "JointO_KneeRight_Y", "JointO_AnkleRight_Y", "JointO_FootRight_Y", "JointO_SpineShoulder_Y", "JointO_HandTipLeft_Y", "JointO_ThumbLeft_Y", "JointO_HandTipRight_Y", "JointO_ThumbRight_Y", "JointP_SpineBase_Z", "JointP_SpineMid_Z", "JointP_Neck_Z", "JointP_Head_Z", "JointP_ShoulderLeft_Z", "JointP_ElbowLeft_Z", "JointP_WristLeft_Z", "JointP_HandLeft_Z", "JointP_ShoulderRight_Z", "JointP_ElbowRight_Z", "JointP_WristRight_Z", "JointP_HandRight_Z", "JointP_HipLeft_Z", "JointP_KneeLeft_Z", "JointP_AnkleLeft_Z", "JointP_FootLeft_Z", "JointP_HipRight_Z", "JointP_KneeRight_Z", "JointP_AnkleRight_Z", "JointP_FootRight_Z", "JointP_SpineShoulder_Z", "JointP_HandTipLeft_Z", "JointP_ThumbLeft_Z", "JointP_HandTipRight_Z", "JointP_ThumbRight_Z", "JointO_SpineBase_Z", "JointO_SpineMid_Z", "JointO_Neck_Z", "JointO_Head_Z", "JointO_ShoulderLeft_Z", "JointO_ElbowLeft_Z", "JointO_WristLeft_Z", "JointO_HandLeft_Z", "JointO_ShoulderRight_Z", "JointO_ElbowRight_Z", "JointO_WristRight_Z", "JointO_HandRight_Z", "JointO_HipLeft_Z", "JointO_KneeLeft_Z", "JointO_AnkleLeft_Z", "JointO_FootLeft_Z", "JointO_HipRight_Z", "JointO_KneeRight_Z", "JointO_AnkleRight_Z", "JointO_FootRight_Z", "JointO_SpineShoulder_Z", "JointO_HandTipLeft_Z", "JointO_ThumbLeft_Z", "JointO_HandTipRight_Z", "JointO_ThumbRight_Z", "JointO_SpineBase_W", "JointO_SpineMid_W", "JointO_Neck_W", "JointO_Head_W", "JointO_ShoulderLeft_W", "JointO_ElbowLeft_W", "JointO_WristLeft_W", "JointO_HandLeft_W", "JointO_ShoulderRight_W", "JointO_ElbowRight_W", "JointO_WristRight_W", "JointO_HandRight_W", "JointO_HipLeft_W", "JointO_KneeLeft_W", "JointO_AnkleLeft_W", "JointO_FootLeft_W", "JointO_HipRight_W", "JointO_KneeRight_W", "JointO_AnkleRight_W", "JointO_FootRight_W", "JointO_SpineShoulder_W", "JointO_HandTipLeft_W", "JointO_ThumbLeft_W", "JointO_HandTipRight_W", "JointO_ThumbRight_W", "time_rel", "armopenness", "style2")

loading = False
def setup():
        size(640, 480)
        background(0)
        smooth()
        all_data = loadCSVtoVar()
        count = 0
        print('done loading')
        # todo read file
        # body = row of the data
        
def draw():
    if(not loading):
        frameRate(5)
        body = all_data[count]
        drawSkeleton(body)
        count += 1


def drawSkeleton(body):
    # Body
    DrawBone(body,
             3,
             2)
    DrawBone(body,
             2,
             4)
    DrawBone(body,
             2,
             8)
    DrawBone(body,
             2,
             1)
    DrawBone(body,
             4,
             1)
    DrawBone(body,
             8,
             1)
    DrawBone(body,
             1,
             0)
    DrawBone(body,
             0,
             12)
    DrawBone(body,
             0,
             16)
    DrawBone(body,
             12,
             16)

    # Left Arm
    DrawBone(body,
             4,
             5)
    DrawBone(body,
             5,
             6)
    DrawBone(body,
             6,
             7)

    # Right Arm
    DrawBone(body,
             8,
             9)
    DrawBone(body,
             9,
             10)
    DrawBone(body,
             10,
             11)

    # Left Leg
    DrawBone(body,
             12,
             13)
    DrawBone(body,
             13,
             14)
    DrawBone(body,
             14,
             15)

    # Right Leg
    DrawBone(body,
             16,
             17)
    DrawBone(body,
             17,
             18)
    DrawBone(body,
             18,
             19)


def DrawBone(body, j1,  j2):
    noFill()
    stroke(255, 255, 0)
    line(body[j1].x * width / 2,
         body[j1].y * height / 2,
         body[j2].x * width / 2,
         body[j2].y * height / 2)
    

def cleanRow(row):
    for key, value in row.items():
        if(value == '' or value == 'NA'):
            row[key] = '0'

def loadCSVtoVar():
    loading = True
    print('file opened')
    csvfile = open(fname, 'r')
    print('file opened')
    bodyfreader = csv.DictReader(csvfile, header)
    bodyfreader.next()
    print('file opened')
    for row in bodyfreader:
        print(row['session'])
        jointsP = []
        jointsO = []
        cleanRow(row)
        for j in map_joints:
            nx = map_joints[j].replace('JointType_', 'JointP_') + '_X'
            ny = map_joints[j].replace('JointType_', 'JointP_') + '_Y'
            nz = map_joints[j].replace('JointType_', 'JointP_') + '_Z'
            nox = map_joints[j].replace('JointType_', 'JointO_') + '_X'
            noy = map_joints[j].replace('JointType_', 'JointO_') + '_Y'
            noz = map_joints[j].replace('JointType_', 'JointO_') + '_Z'
            now = map_joints[j].replace('JointType_', 'JointO_') + '_W'
      
                
            x = float(row[nx])
            y = float(row[ny])
            z = float(row[nz])
            jointsP.append(PVector(x, y, z))
            # if(row[nox]!='' and row[noy]!='' and row[noz]!='' and
            # row[nx]!='NA' and row[ny]!='NA' and row[nz]!='NA' ):
            ox = float(row[nox])
            oy = float(row[noy])
            oz = float(row[noz])
            ow = float(row[now])
            jointsO.append((ox, oy, oz, ow))
        print((row['style'], row['child'], row['session'],
            row['activity'], row['versatility']))
        # all_data.append(((row['style'], row['child'], row['session'],
        # row['activity'], row[
        #'versatility']), float(row['time']), float(row['time_rel']), jointsP, jointsO))
        all_data.append( jointsP)
    idx = 0
    csvfile.close()
    loading = False
    return all_data
