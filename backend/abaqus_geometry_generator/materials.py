# -*- coding: utf-8 -*-
from imports import *

class Materials():
    def __init__(self, model):
        self.materialsPart(model)

    def materialsPart(self, model):      
        m = mdb.models[model]

        m.Material(name='DA718')
        m.materials['DA718'].SpecificHeat(dependencies=0, law=
            CONSTANTVOLUME, table=((440600000.0, 20.0), (459700000.0, 100.0), (
            486700000.0, 300.0), (520900000.0, 500.0), (559900000.0, 600.0), (
            606000000.0, 650.0), (610900000.0, 700.0), (662000000.0, 800.0), (
            651000000.0, 900.0), (673000000.0, 1000.0), (710100000.0, 1100.0), (
            710100000.0, 1200.0)), temperatureDependency=ON)
        m.materials['DA718'].setValues(materialIdentifier='')
        m.materials['DA718'].setValues(description=
            '[PENG20] (S.72)')
        m.materials['DA718'].Elastic(dependencies=0, moduli=
            LONG_TERM, noCompression=OFF, noTension=OFF, table=((217000.0, 0.3, 20.0), 
            (155000.0, 0.3, 900.0)), temperatureDependency=ON, type=ISOTROPIC)
        m.materials['DA718'].Density(dependencies=0, 
            distributionType=UNIFORM, fieldName='', table=((8.22e-09, ), ), 
            temperatureDependency=OFF)
        m.materials['DA718'].InelasticHeatFraction(fraction=0.9)
        m.materials['DA718'].Conductivity(dependencies=0, table=((
            10.31, 20.0), (11.9, 100.0), (15.2, 300.0), (18.5, 500.0), (20.3, 600.0), (
            24.15, 700.0), (26.09, 800.0), (25.7, 900.0), (26.3, 1000.0), (30.95, 
            1100.0), (30.95, 1200.0)), temperatureDependency=ON, type=ISOTROPIC)
        m.materials['DA718'].JohnsonCookDamageInitiation(alpha=0.0, 
            definition=MSFLD, dependencies=0, direction=NMORI, feq=10.0, fnn=10.0, fnt=
            10.0, frequency=1, ks=0.0, numberImperfections=4, omega=1.0, position=
            CENTROID, table=((0.40583, 0.75, -1.45, 0.04, 0.89, 1340.0, 25.0, 0.001), )
            , temperatureDependency=OFF, tolerance=0.05)
        m.materials['DA718'].johnsonCookDamageInitiation.DamageEvolution(
            degradation=MAXIMUM, dependencies=0, mixedModeBehavior=MODE_INDEPENDENT, 
            modeMixRatio=ENERGY, power=None, softening=TABULAR, table=((0.0, 0.0), (
            0.030888524, 0.0003298), (0.059978241, 0.0006596), (0.087373904, 
            0.0009894), (0.113174168, 0.0013192), (0.137471942, 0.001649), (
            0.160354723, 0.0019788), (0.181904915, 0.0023086), (0.202200122, 
            0.0026384), (0.221313428, 0.0029682), (0.239313661, 0.003298), (
            0.256265642, 0.0036278), (0.272230417, 0.0039576), (0.287265476, 
            0.0042874), (0.301424961, 0.0046172), (0.314759862, 0.004947), (
            0.327318199, 0.0052768), (0.339145195, 0.0056066), (0.350283441, 
            0.0059364), (0.360773045, 0.0062662), (0.370651783, 0.006596), (
            0.379955228, 0.0069258), (0.388716882, 0.0072556), (0.396968297, 
            0.0075854), (0.404739187, 0.0079152), (0.412057536, 0.008245), (
            0.418949697, 0.0085748), (0.42544049, 0.0089046), (0.431553289, 0.0092344), 
            (0.437310106, 0.0095642), (0.442731672, 0.009894), (0.447837511, 
            0.0102238), (0.452646009, 0.0105536), (0.457174482, 0.0108834), (
            0.461439237, 0.0112132), (0.465455632, 0.011543), (0.46923813, 0.0118728), 
            (0.472800353, 0.0122026), (0.476155128, 0.0125324), (0.479314536, 
            0.0128622), (0.482289954, 0.013192), (0.485092098, 0.0135218), (
            0.487731058, 0.0138516), (0.490216336, 0.0141814), (0.492556883, 
            0.0145112), (0.494761128, 0.014841), (0.496837007, 0.0151708), (
            0.498791996, 0.0155006), (0.500633136, 0.0158304), (0.502367056, 
            0.0161602), (0.504, 0.01649)), temperatureDependency=OFF, type=
            DISPLACEMENT)
        m.materials['DA718'].Plastic(dataType=HALF_CYCLE, 
            dependencies=0, hardening=JOHNSON_COOK, numBackstresses=1, rate=OFF, 
            strainRangeDependency=OFF, table=((1262.0, 1354.0, 0.5, 1.08, 1340.0, 
            20.0), ), temperatureDependency=OFF)
        m.materials['DA718'].plastic.RateDependent(dependencies=0, 
            table=((0.006, 0.001), ), temperatureDependency=OFF, type=JOHNSON_COOK)
        m.Material(name='WG-300')
        m.materials['WG-300'].Elastic(dependencies=0, moduli=
            LONG_TERM, noCompression=OFF, noTension=OFF, table=((393000.0, 0.23), ), 
            temperatureDependency=OFF, type=ISOTROPIC)
        m.materials['WG-300'].Density(dependencies=0, 
            distributionType=UNIFORM, fieldName='', table=((4e-09, ), ), 
            temperatureDependency=OFF)
        m.materials['WG-300'].setValues(description=
            'WG-300 Greenleaf\n')
        m.materials['WG-300'].SpecificHeat(dependencies=0, law=
            CONSTANTVOLUME, table=((715000000.0, 25.0), (875000000.0, 100.0), (
            990000000.0, 200.0), (1060000000.0, 300.0), (1110000000.0, 400.0), (
            1150000000.0, 500.0), (1175000000.0, 600.0), (1205000000.0, 700.0), (
            1225000000.0, 800.0), (1245000000.0, 900.0), (1265000000.0, 1000.0)), 
            temperatureDependency=ON)
        m.materials['WG-300'].setValues(materialIdentifier='')
        m.materials['WG-300'].Conductivity(dependencies=0, table=((
            35.0, 25.0), (28.344, 50.0), (22.532, 200.0), (18.869, 300.0), (16.322, 
            400.0), (14.252, 500.0), (12.978, 600.0), (11.783, 700.0), (10.748, 800.0), 
            (10.032, 900.0), (9.315, 1000.0)), temperatureDependency=ON, type=
            ISOTROPIC)

# model = Materials()
