import maya.cmds as cmds

obj = cmds.ls(sl=True)[0]
vertexCount = cmds.polyEvaluate( v=True )
faceCount = cmds.polyEvaluate( f=True )

indices = [
    [int(a[0]), int(a[1]), int(a[2])] for a in 
        [[x for x in str(( cmds.polyInfo('{}.f[{}]'.format(obj,f), faceToVertex=True) )[0]).split(' ') if x][2:5] 
        for f in range(faceCount)]
    ]
    
normals = [
    cmds.polyNormalPerVertex(f'{obj}.vtx[{i}]', query=True, xyz=True)[:3]
    for i in range(vertexCount)
]

frames = []
for frame in range(220):
    cmds.currentTime(frame)
    vertices = [cmds.xform('{}.vtx[{}]'.format(obj, v), q=True, t=True) for v in range(vertexCount)]
    frames.append(vertices)



print(len(frames))
print(len(normals))
print(len(indices))

import pickle
with open(r'E:\github\python_lab\labs\animation\papers\animated_face.dat', 'wb') as f:
    pickle.dump((indices, normals, frames), f)