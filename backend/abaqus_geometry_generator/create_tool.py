# -*- coding: utf-8 -*-
from imports import *

class ToolModel():
    def __init__(self, data):
        self.dataInput(data)
        self.createPart()
        self.createPartition()
        self.createSetsandSections()
        self.createMesh()


    def dataInput(self, data):
        # Calling Model
        self.ModelName = str(data['generalInformation']['modelName'])
        self.m = mdb.models[self.ModelName]
        # Defining Variables
        self.Name = str(data['toolData']['createPartInformation']['Name'])
        self.ReliefAngle = data['toolData']['createPartInformation']['clearanceAngle']
        self.RakeAngle = float(data['toolData']['createPartInformation']['rakeAngle'])
        self.RakeAngle = -6
        self.clearanceFaceDimension = data['toolData']['createPartInformation']['clearanceFaceDimension']
        self.rakeFaceDimension = data['toolData']['createPartInformation']['rakeFaceDimension']
        self.Radius = data['toolData']['createPartInformation']['Radius']
        self.Trickness = data['toolData']['createPartInformation']['Trickness']

        self.SectionName = "ToolSection"

        self.sizePartitionRadius = data['toolData']['createPartitionInformation']['partition01']
        self.sizePartitionVerticalEdge = data['toolData']['createPartitionInformation']['partition02']
        self.GlobalSize = data['toolData']['createMeshInformation']['globalSize']
        self.DeviationFactor = data['toolData']['createMeshInformation']['deviationFactor']
        self.MinSizeFactor = data['toolData']['createMeshInformation']['minSizeFactor']
        self.RadiusMesh = data['toolData']['createMeshInformation']['radiusMeshSize']
        self.PartitionMesh = data['toolData']['createMeshInformation']['partition02MeshSize']
        self.BiasMinSize = data['toolData']['createMeshInformation']['noseBiasMinMeshSize']
        self.BiasMaxSize = data['toolData']['createMeshInformation']['noseBiasMaxMeshSize']

    def createPart(self):
        # Creating Sketch
        s = self.m.ConstrainedSketch(name='SketchTool', sheetSize=200.0)
        # Creating "References lines"
        s.Line(point1=(0.0, 0.0), point2=(10.6401720046997, 0.0))
        s.HorizontalConstraint(addUndoState=False, entity=s.geometry[2])
        s.Line(point1=(0.0, 10.0), point2=(0.0, 1.25))
        s.VerticalConstraint(addUndoState=False, entity=s.geometry[3])
        s.CoincidentConstraint(entity1=s.vertices[3], entity2=s.vertices[0])
        s.setAsConstruction(objectList=(s.geometry[3], s.geometry[2]))
        s.FixedConstraint(entity=s.geometry[3])
        # Creating Geometry Lines
        s.Line(point1=(3.31129169464111, 1.25408506393433), point2=(11.7126932144165, 5.62865686416626))
        s.Line(point1=(11.98082447052, 7.72666597366333), point2=(11.98082447052, 13.75))
        s.Line(point1=(9.38889980316162, 13.6635837554932), point2=(3.17722415924072, 13.6635837554932))
        s.Line(point1=(3.75, 12.5), point2=(2.99847316741943, 3.93239545822144))
        s.HorizontalConstraint(addUndoState=False, entity=s.geometry[6])
        s.VerticalConstraint(addUndoState=False, entity=s.geometry[5])
        s.CoincidentConstraint(entity1=s.vertices[4], entity2=s.vertices[0])
        s.CoincidentConstraint(entity1=s.vertices[6], entity2=s.vertices[5])
        s.CoincidentConstraint(entity1=s.vertices[8], entity2=s.vertices[7])
        s.CoincidentConstraint(entity1=s.vertices[10], entity2=s.vertices[9])
        s.CoincidentConstraint(entity1=s.vertices[11], entity2=s.vertices[0])
        # Defining Dimension and Angle of the Clearance Face
        s.AngularDimension(line1=s.geometry[4], line2=s.geometry[2], textPoint=(18.2371864318848, 2.41468572616577), value=self.ReliefAngle)
        s.ObliqueDimension(textPoint=(10.5507974624634, -1.29030799865723), value=self.clearanceFaceDimension, vertex1=s.vertices[0], vertex2=s.vertices[5])
        # Defining Dimension and Angle of the Rake Face
        s.AngularDimension(line1=s.geometry[7], line2=s.geometry[3], textPoint=(0.31717586517334, 7.36955785751343), value=self.RakeAngle)
        s.ObliqueDimension(textPoint=(0.0, 8.75), value=self.rakeFaceDimension, vertex1=s.vertices[9], vertex2=s.vertices[0])
        # Defining tool radius
        self.Radius = 0.0001 if self.Radius == 0 else self.Radius
        s.FilletByRadius(curve1=s.geometry[4], curve2=s.geometry[7], nearPoint1=(3.86042213439941, 1.10268461704254), nearPoint2=(4.32205963134766, 0.249606490135193), radius=self.Radius)
        # Align Tool with the coordinate system
        s.CoincidentConstraint(entity1=s.vertices[4], entity2=s.geometry[2])
        s.CoincidentConstraint(entity1=s.vertices[11], entity2=s.geometry[3])
        # Creating Tool Body
        self.p = self.m.Part(dimensionality=THREE_D, name=self.Name, type=DEFORMABLE_BODY)
        self.p.BaseSolidExtrude(depth=self.Trickness, sketch=s)

    def createPartition(self):
        # Creating Sketch Tool Particion
        s = self.m.ConstrainedSketch(gridSpacing=0.3, name='sketchTool', sheetSize=12.33, transform=self.p.MakeSketchTransform(sketchPlane=self.p.faces[5], 
            sketchPlaneSide=SIDE1, sketchUpEdge=self.p.edges[7], sketchOrientation=RIGHT, origin=(1.923927, 2.470625, 0.02)))
        self.p.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=s)
        # Creating Partition Line 01
        s.Line(point1=(-1.33219867034149, -2.36441900014877), point2=(-0.154028704597473, -2.28348900556564))
        s.ObliqueDimension(textPoint=(-0.0696328191299438, -2.04407115459442), value=self.sizePartitionRadius, vertex1=s.vertices[6], vertex2=s.vertices[7])
        s.ParallelConstraint(entity1=s.geometry[5], entity2=s.geometry[7])
        s.CoincidentConstraint(entity1=s.vertices[6], entity2=s.vertices[5])
        # Creating Partition Line 02
        s.Line(point1=(-1.65, -2.25), point2=(-1.275, -1.65))
        s.ObliqueDimension(textPoint=(-1.53137355132294, -1.76418836593628), value=self.sizePartitionRadius, vertex1=s.vertices[8], vertex2=s.vertices[9])
        s.ParallelConstraint(entity1=s.geometry[8], entity2=s.geometry[2])
        s.CoincidentConstraint(entity1=s.vertices[6], entity2=s.vertices[8])
        # Creating Auxiliary Point 01
        s.Spot(point=(-0.45, -2.25))
        s.CoincidentConstraint(entity1=s.geometry[5], entity2=s.vertices[10])
        s.ObliqueDimension(textPoint=(-0.381290843917847, -2.48147197246552), value=self.sizePartitionRadius, vertex1=s.vertices[4], vertex2=s.vertices[10])
        # Creating Auxiliary Point 02
        s.Spot(point=(-1.425, -1.275))
        s.CoincidentConstraint(entity1=s.vertices[11], entity2=s.geometry[2])
        s.ObliqueDimension(textPoint=(-1.98067395968628, -1.20997364997864), value=self.sizePartitionRadius, vertex1=s.vertices[11], vertex2=s.vertices[0])
        # Creating Partition Line 03 and 04
        s.Line(point1=(-1.4025, -1.155), point2=(-1.0725, -1.4025))
        s.Line(point1=(-0.165, -2.145), point2=(-0.2475, -1.815))
        s.CoincidentConstraint(entity1=s.vertices[12], entity2=s.vertices[11])
        s.CoincidentConstraint(entity1=s.geometry[9], entity2=s.vertices[9])
        s.CoincidentConstraint(entity1=s.vertices[14], entity2=s.vertices[10])
        s.CoincidentConstraint(entity1=s.vertices[7], entity2=s.geometry[10])
        s.CoincidentConstraint(entity1=s.vertices[15], entity2=s.vertices[13])
        # Creating Auxiliary Point 03
        s.Spot(point=(1.35, -1.35))
        s.CoincidentConstraint(entity1=s.vertices[16], entity2=s.geometry[4])
        s.VerticalDimension(textPoint=(1.66873724179077, -2.03905059576035), value=self.sizePartitionVerticalEdge, vertex1=s.vertices[16], vertex2=s.vertices[3])
        # Creating Partition Line 05
        s.Line(point1=(0.255, -1.36), point2=(0.85, -1.19))
        s.CoincidentConstraint(entity1=s.vertices[18], entity2=s.vertices[16])
        s.CoincidentConstraint(entity1=s.vertices[17], entity2=s.vertices[13])
        # Creating Partition Line 06
        s.Line(point1=(0.299743451380973, 2.71355728388917), point2=(-0.17, 1.445))
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[19], entity2=s.geometry[3])
        s.ParallelConstraint(entity1=s.geometry[12], entity2=s.geometry[2])
        s.CoincidentConstraint(entity1=s.vertices[20], entity2=s.vertices[13])
        # Creating Partition Line 07 and 08
        s.Line(point1=(-1.90824233575058, -2.50458845674992), point2=(-1.92693637891006, -2.53446565747261))
        s.Line(point1=(-1.99049629850578, -2.48404787659645), point2=(-1.97086750550461, -2.50645578086376))
        s.CoincidentConstraint(entity1=s.vertices[24], entity2=s.vertices[6])
        s.CoincidentConstraint(entity1=s.vertices[23], entity2=s.vertices[0])
        s.CoincidentConstraint(entity1=s.vertices[21], entity2=s.vertices[6])
        s.CoincidentConstraint(entity1=s.vertices[22], entity2=s.vertices[4])
        # Creating Partition
        self.p.PartitionFaceBySketch(faces=self.p.faces.getSequenceFromMask(('[#20 ]', ), ), sketch=s, sketchUpEdge=self.p.edges[7])
        self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#1 ]', ), ), edges=(self.p.edges[9], self.p.edges[10], self.p.edges[11], self.p.edges[12]), line=self.p.edges[26], sense=REVERSE)
        self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#2 ]', ), ), edges=(self.p.edges[21], self.p.edges[23]), line=self.p.edges[33], sense=REVERSE)
        self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#4 ]', ), ), edges=(self.p.edges[32], self.p.edges[34]), line=self.p.edges[5], sense=REVERSE)
        self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#8 ]', ), ), edges=(self.p.edges[35], ), line=self.p.edges[20], sense=REVERSE)
        self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#1 ]', ), ), edges=(self.p.edges[42], ), line=self.p.edges[30], sense=REVERSE)
                
    def createSetsandSections(self):
        # Defining the Reference Point
        self.p.ReferencePoint(point=self.p.InterestingPoint(self.p.edges[5], MIDDLE))
        # Creating RF Set
        self.p.Set(name='ToolRP', referencePoints=(self.p.referencePoints[8], ))
        # Creating Domain Set - Without RF
        self.p.Set(cells=self.p.cells.getSequenceFromMask(('[#7f ]', ), ), name='ToolDomain')
        # Creating Sections
        self.m.HomogeneousSolidSection(material='WG-300', name=self.SectionName, thickness=None)
        self.p.SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=self.m.parts['Tool'].sets['ToolDomain'], sectionName=self.SectionName, thicknessAssignment=FROM_SECTION)
        # Creating Temperature Set
        self.p.Set(name='ToolTemperatureOutputSet', vertices=self.p.vertices.getSequenceFromMask(('[#4000 ]', ), ))
        # Creating Surfaces
        self.p.Surface(name='ToolSurface', side1Faces=self.p.faces.getSequenceFromMask(('[#640a0000 ]', ), ))

    def createMesh(self):
        # Creating Mesh
        self.p.setMeshControls(algorithm=ADVANCING_FRONT, regions=self.p.cells.getSequenceFromMask(('[#7f ]', ), ), technique=SWEEP)
        self.p.seedPart(deviationFactor=self.DeviationFactor, minSizeFactor=self.MinSizeFactor, size=self.GlobalSize)
        self.p.setElementType(elemTypes=(ElemType(elemCode=C3D8T, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, distortionControl=DEFAULT), ElemType(elemCode=C3D6T, elemLibrary=EXPLICIT), ElemType(elemCode=C3D4T, elemLibrary=EXPLICIT)), regions=(self.p.cells.getSequenceFromMask(('[#7f ]', ), ), ))
        self.p.setElementType(elemTypes=(ElemType(elemCode=C3D8T, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, distortionControl=DEFAULT), ElemType(elemCode=C3D6T, elemLibrary=EXPLICIT), ElemType(elemCode=C3D4T, elemLibrary=EXPLICIT)), regions=(self.p.cells.getSequenceFromMask(('[#7f ]', ), ), ))
        # Defining Seed Edges
        self.p.seedEdgeBySize(constraint=FINER, deviationFactor=0.1, edges=self.p.edges.getSequenceFromMask(('[#2800 ]', ), ), minSizeFactor=0.1, size=self.PartitionMesh)
        self.p.seedEdgeByBias(biasMethod=SINGLE, constraint=FINER, end1Edges=self.p.edges.getSequenceFromMask(('[#10500000 #40201 ]', ), ), end2Edges=self.p.edges.getSequenceFromMask(('[#81040080 #20002 ]', ), ), maxSize=self.BiasMaxSize, minSize=self.BiasMinSize)
        self.p.seedEdgeBySize(constraint=FINER, deviationFactor=0.1, edges=self.p.edges.getSequenceFromMask(('[#6c000100 #80e4 ]', ), ), minSizeFactor=0.1, size=self.RadiusMesh)
        self.p.generateMesh()
