# -*- coding: utf-8 -*-
from imports import *

class EulerianModel():
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
        self.KssDomain = "KssDomain"
        self.ElementType = "EC3D8RT"
        self.ElementLibrary = "EXPLICIT"
        self.EulerDomain = "EulerDomain"
        self.SectionName = "EulerSection"
        self.WorkpieceDomain = "WorkpieceDomain"
        self.WorkpieceBottom = "WorkpieceBottom"
        self.PartName = str(data['eulerianData']['createPartInformation']['Name'])
        self.Width = data['eulerianData']['createPartInformation']['Width']
        self.Height = data['eulerianData']['createPartInformation']['Height']
        self.Trickness = data['eulerianData']['createPartInformation']['Trickness']
        self.x_points = data['eulerianData']['createParticionInformation']['x_points']
        self.y_points = data['eulerianData']['createParticionInformation']['y_points']
        self.GlobalSize = data['eulerianData']['createMeshInformation']['globalSize']
        self.DeviationFactor = data['eulerianData']['createMeshInformation']['deviationFactor']
        self.MinSizeFactor = data['eulerianData']['createMeshInformation']['minSizeFactor']

    def createPart(self):
        # Creating Sketch
        s = self.m.ConstrainedSketch(name='sketchEulerian', sheetSize=20.0)
        s.rectangle(point1=(0.0, 0.0), point2=(self.Width, self.Height))
        # Creating Body
        self.p = self.m.Part(dimensionality=THREE_D, name=self.PartName, type=EULERIAN)
        self.p.BaseSolidExtrude(depth=self.Trickness, sketch=s)

    def createPartition(self):
        # Creating Sketch Tool Particion
        s = self.m.ConstrainedSketch(gridSpacing=0.31, name='sketchEulerinPartition', sheetSize=12.76, transform=self.p.MakeSketchTransform(sketchPlane=self.p.faces[4], 
                sketchPlaneSide=SIDE1, sketchUpEdge=self.p.edges[7], sketchOrientation=RIGHT, origin=(0, 0, 0)))
        self.p.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=s)
        # Draw the first vertical line and add constraints
        s.Line(point1=(self.x_points[0], 0.0), point2=(self.x_points[0], self.Height))
        s.VerticalConstraint(addUndoState=False, entity=s.geometry[6])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[3], entity2=s.geometry[6])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[4], entity2=s.geometry[3])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[5], entity2=s.geometry[5])
        # Draw the second vertical line and add constraints
        s.Line(point1=(self.x_points[1], 0.0), point2=(self.x_points[1], self.Height))
        s.VerticalConstraint(addUndoState=False, entity=s.geometry[7])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[3], entity2=s.geometry[7])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[6], entity2=s.geometry[3])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[7], entity2=s.geometry[5])
        # Draw the third vertical line and add constraints
        s.Line(point1=(self.x_points[2], 0.0), point2=(self.x_points[2], self.Height))
        s.VerticalConstraint(addUndoState=False, entity=s.geometry[8])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[3], entity2=s.geometry[8])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[8], entity2=s.geometry[3])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[9], entity2=s.geometry[5])
        # Draw the fourth vertical line and add constraints
        s.Line(point1=(self.x_points[3], 0.0), point2=(self.x_points[3], self.Height))
        s.VerticalConstraint(addUndoState=False, entity=s.geometry[9])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[3], entity2=s.geometry[9])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[10], entity2=s.geometry[3])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[11], entity2=s.geometry[5])
        # Draw the first horizontal line and add constraints
        s.Line(point1=(0.0, self.y_points[0]), point2=(self.Width, self.y_points[0]))
        s.HorizontalConstraint(addUndoState=False, entity=s.geometry[10])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[2], entity2=s.geometry[10])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[12], entity2=s.geometry[2])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[13], entity2=s.geometry[4])
        # Draw the second horizontal line and add constraints
        s.Line(point1=(0.0, self.y_points[1]), point2=(self.Width, self.y_points[1]))
        s.HorizontalConstraint(addUndoState=False, entity=s.geometry[11])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[2], entity2=s.geometry[11])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[14], entity2=s.geometry[2])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[15], entity2=s.geometry[4])
        # Draw the third horizontal line and add constraints
        s.Line(point1=(0.0, self.y_points[2]), point2=(self.Width, self.y_points[2]))
        s.HorizontalConstraint(addUndoState=False, entity=s.geometry[12])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[2], entity2=s.geometry[12])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[16], entity2=s.geometry[2])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[17], entity2=s.geometry[4])
        # Draw the fourth horizontal line and add constraints
        s.Line(point1=(0.0, self.y_points[3]), point2=(self.Width, self.y_points[3]))
        s.HorizontalConstraint(addUndoState=False, entity=s.geometry[13])
        s.PerpendicularConstraint(addUndoState=False, entity1=s.geometry[2], entity2=s.geometry[13])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[18], entity2=s.geometry[2])
        s.CoincidentConstraint(addUndoState=False, entity1=s.vertices[19], entity2=s.geometry[4])
        # Partition the face by the sketch
        self.p.PartitionFaceBySketch(faces=self.p.faces.getSequenceFromMask(('[#10 ]', ), ), sketch=s, sketchUpEdge=self.p.edges[7])
        self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#1 ]', ), ), edges=(self.p.edges[3], self.p.edges[5], self.p.edges[7], self.p.edges[11], 
            self.p.edges[14], self.p.edges[18], self.p.edges[19], self.p.edges[22], self.p.edges[28], self.p.edges[31], self.p.edges[34], self.p.edges[35], self.p.edges[38], 
            self.p.edges[42], self.p.edges[45], self.p.edges[46], self.p.edges[47], self.p.edges[52], self.p.edges[55], self.p.edges[57]), line=self.p.edges[62], sense=REVERSE)
        
        # This code creates partitions for cells by extruding edges using different parameter values.
        # The partitions list contains tuples of (mask, edge, line) for each partition operation.
        # The loop iterates over these tuples and performs the PartitionCellByExtrudeEdge operation.
        # Line exemple --> self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#8 ]', ), ), edges=(self.p.edges[51], ), line=self.p.edges[85], sense=REVERSE)
        partitions = [(8, 51, 85), (16, 62, 5), (32, 73, 13), (64, 82, 21), (256, 82, 29), (512, 89, 37), (1024, 99, 42), 
                      (2048, 103, 47), (1024, 100, 55), (2048, 109, 62), (4096, 116, 67), (8192, 122, 45), (8192, 120, 50), 
                      (16384, 126, 57), (1, 133, 62), (1, 137, 67), (65536, 138, 50), (1, 142, 58), (1, 145, 63), (1, 145, 68)]
        for mask, edge, line in partitions:
            self.p.PartitionCellByExtrudeEdge(cells=self.p.cells.getSequenceFromMask(('[#%x ]' % mask, ), ), edges=(self.p.edges[edge], ), line=self.p.edges[line], sense=REVERSE)

    def createSetsandSections(self):
        # Creating WorkpieceBottom Set 
        self.p.Set(faces=self.p.faces.getSequenceFromMask(('[#0:2 #f0 #800 ]', ), ), name=self.WorkpieceBottom)
        # Creating EulerDomain Set 
        self.p.Set(cells=self.p.cells.getSequenceFromMask(('[#1ffffff ]', ), ), name=self.EulerDomain)
        # Creating WorkpieceDomain Set 
        self.p.Set(cells=self.p.cells.getSequenceFromMask(('[#eee00 ]', ), ), name=self.WorkpieceDomain)
        # Creating KssDomain Set 
        self.p.Set(cells=self.p.cells.getSequenceFromMask(('[#400020 ]', ), ), name=self.KssDomain)

        # Creating Sections
        self.m.EulerianSection(data={'da718-1': 'DA718'}, name=self.SectionName)
        self.p.Set(cells=self.p.cells.getSequenceFromMask(('[#1ffffff ]', ), ), name=self.EulerDomain)
        self.p.SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=self.p.sets[self.EulerDomain], sectionName=self.SectionName, thicknessAssignment=FROM_SECTION)

    def createMesh(self):
        # Set the element types for the part
        self.p.setElementType(elemTypes=(ElemType(elemCode=EC3D8RT, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, hourglassControl=DEFAULT), ElemType(elemCode=UNKNOWN_WEDGE, elemLibrary=EXPLICIT), ElemType(elemCode=UNKNOWN_TET, elemLibrary=EXPLICIT)), regions=(self.p.cells.getSequenceFromMask(('[#1ffffff ]', ), ), ))
        # Seed the part with a global element size
        self.p.seedPart(deviationFactor=self.DeviationFactor, minSizeFactor=self.MinSizeFactor, size=self.GlobalSize)
        # Seed edges with a bias toward one end (end1Edges) using a single bias method
        self.p.seedEdgeByBias(biasMethod=SINGLE, constraint=FINER, end1Edges=self.p.edges.getSequenceFromMask(('[#0:3 #2082082 #200000 ]', ), ), end2Edges=self.p.edges.getSequenceFromMask(('[#0:3 #208208 #8800000 ]', ), ), maxSize=0.2, minSize=0.06)
        self.p.seedEdgeByBias(biasMethod=SINGLE, constraint=FINER, end1Edges=self.p.edges.getSequenceFromMask(('[#0:2 #21084800 #0 #1000 ]', ), ), end2Edges=self.p.edges.getSequenceFromMask(('[#0:2 #10842000 #0 #110000 ]', ), ), maxSize=0.06, minSize=0.006)
        self.p.seedEdgeByBias(biasMethod=SINGLE, constraint=FINER, end1Edges=self.p.edges.getSequenceFromMask(('[#0 #150000 #40000500 #8000001 #402000 ]', ), ), end2Edges=self.p.edges.getSequenceFromMask(('[#0:3 #1400000 ]', ), ), maxSize=0.2, minSize=0.006)
        self.p.seedEdgeByBias(biasMethod=SINGLE, constraint=FINER, end1Edges=self.p.edges.getSequenceFromMask(('[#21020404 #0:3 #20000 ]', ), ), end2Edges=self.p.edges.getSequenceFromMask(('[#408101 #0:3 #280 ]', ), ), maxSize=0.03, minSize=0.006)
        self.p.seedEdgeByBias(biasMethod=SINGLE, constraint=FINER, end1Edges=self.p.edges.getSequenceFromMask(('[#0:4 #5000000 ]', ), ), end2Edges=self.p.edges.getSequenceFromMask(('[#1a000000 #0:2 #d0000000 #5a ]', ), ), maxSize=0.2, minSize=0.03)
        # Seed edges with a specified size
        self.p.seedEdgeBySize(constraint=FINER, deviationFactor=0.1, edges=self.p.edges.getSequenceFromMask(('[#40000000 #31a28c63 #c6 #0 #ccc00 ]', ), ), minSizeFactor=0.1, size=0.006)
        self.p.seedEdgeBySize(constraint=FINER, deviationFactor=0.1, edges=self.p.edges.getSequenceFromMask(('[#340000 #600000c #18000 #150 ]', ), ), minSizeFactor=0.1, size=0.006)
        self.p.seedEdgeBySize(constraint=FINER, deviationFactor=0.1, edges=self.p.edges.getSequenceFromMask(('[#68d0 #c0003180 #6300018 #155400 ]', ), ), minSizeFactor=0.1, size=0.006)
        # Generate the mesh for the part
        self.p.generateMesh()

