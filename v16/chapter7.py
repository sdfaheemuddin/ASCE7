from enum import Enum
import numpy as np
from tools import CreateTable
from chapter1 import *

class Table_7_3__1:
    
    class SurfaceRoughness(str, Enum):
        B = "B"
        C = "C"
        D = "D"
        ABOVE_TREE_LINE = "Above the tree line in windswept mountainous areas"
        ALASKA = "In Alaska, in areas where trees do not exist within a 2-mi (3-km) radius of the site"

    class RoofExposure(str, Enum):
        FULLY_EXPOSED = "Fully Exposed"
        PARTIALLY_EXPOSED = "Partially Exposed"
        SHELTERED = "Sheltered"

    exposure_factor = CreateTable(
        row_headers=[
            SurfaceRoughness.B,
            SurfaceRoughness.C,
            SurfaceRoughness.D,
            SurfaceRoughness.ABOVE_TREE_LINE,
            SurfaceRoughness.ALASKA
        ],
        col_headers=[
            RoofExposure.FULLY_EXPOSED,
            RoofExposure.PARTIALLY_EXPOSED,
            RoofExposure.SHELTERED
        ]
    ).add_values([
            [0.9, 1.0, 1.2],
            [0.9, 1.0, 1.1],
            [0.8, 0.9, 1.0],
            [0.7, 0.8, None],
            [0.7, 0.8, None],
        ]
    )
    
    @staticmethod
    def get_exposure_factor(surface_roughness: SurfaceRoughness, roof_exposure: RoofExposure):
        return Table_7_3__1.exposure_factor[surface_roughness][roof_exposure]
    
class Table_7_3__2:
    
    class ThermalFactor(str, Enum):
        ALL_OTHER_STRUCTURES = 1.0
        ABOVE_FREEZING = 1.1
        UNHEATED_OPEN_AIR = 1.2
        FREEZER_BUILDING = 1.3
        HEATED_GREENHOUSES = 0.85

class Figure_7_4__1:

    class RoofSurface(str, Enum):
        SLIPPERY = "Slippery"
        OTHER = "Other"

    roof_slope_factor = {
        1: {
            RoofSurface.SLIPPERY : np.array([5,70]),
            RoofSurface.OTHER : np.array([30,70]),
        },
        1.1: {
            RoofSurface.SLIPPERY : np.array([10,70]),
            RoofSurface.OTHER : np.array([37.5,70]),
        },
        1.2: {
            RoofSurface.SLIPPERY : np.array([15,70]),
            RoofSurface.OTHER : np.array([45,70]),
        }
    }
    
    def get_roof_slope_factor(tilt_angle, Ct, roof_surface: RoofSurface):
        Ct = min(1.2,max(1,Ct))

        # Perform interpolation for each Ct value
        Cs = np.interp(tilt_angle, Figure_7_4__1.roof_slope_factor[Ct][roof_surface], np.array([1, 0]),left=1,right=0)
        
        return Cs

class Eq_7_3__1:
    def get_flat_roof_snow_load(Ce, Ct, Is, Pg):
        return 0.7 * Ce * Ct * Is * Pg

class Sec_7_3_4:
    def get_minimum_snow_load(Pg, Is, tilt_angle, is_roof_curved: bool):
        min_angle = 10 if is_roof_curved else 15
        if tilt_angle < min_angle:
            return Is * min(20, Pg)
        else:
            return 0

class Eq_7_4__1:
    def get_sloped_roof_snow_load(Cs, Pf):
        return Cs * Pf

class SnowLoad:
    def __init__(self, tilt_angle, risk: Table_1_5__1.RiskCategory, ground_snow,
                 surface_roughness: Table_7_3__1.SurfaceRoughness, roof_exposure: Table_7_3__1.RoofExposure,
                 thermal_factor: Table_7_3__2.ThermalFactor, roof_surface: Figure_7_4__1.RoofSurface, is_roof_curved: bool = False):
        self.tilt_angle = tilt_angle
        self.risk = risk
        self.Pg = ground_snow
        self.Is = Table_1_5__2.get_importance_factor(risk, Table_1_5__2.Load.SNOW)
        
        self.Ce = Table_7_3__1.get_exposure_factor(surface_roughness, roof_exposure)
        self.Ct = thermal_factor
        self.Cs = Figure_7_4__1.get_roof_slope_factor(self.tilt_angle, self.Ct, roof_surface)
        
        self.Pf = Eq_7_3__1.get_flat_roof_snow_load(self.Ce, self.Ct, self.Is, self.Pg)
        self.Pm = Sec_7_3_4.get_minimum_snow_load(self.Pg, self.Is, self.tilt_angle, is_roof_curved)
        self.Ps = Eq_7_4__1.get_sloped_roof_snow_load(self.Cs, self.Pf)
        
        self.Snow = max(self.Ps, self.Pm)