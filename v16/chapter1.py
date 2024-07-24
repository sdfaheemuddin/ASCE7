from enum import Enum
from tools import CreateTable

class Table_1_5__1:
    class RiskCategory(str, Enum):
        I = "I"
        II = "II"
        III = "III"
        IV = "IV"

class Table_1_5__2:
    
    RiskCategory = Table_1_5__1.RiskCategory

    class Load(str, Enum):
        SNOW = "Snow"
        ICE_THICKNESS = "Ice Thickness"
        ICE_WIND = "Wind on Ice"
        SEISMIC = "Seismic"
        WIND = "Wind"
    
    importance_factor = CreateTable(
            row_headers=[
                RiskCategory.I,
                RiskCategory.II,
                RiskCategory.III,
                RiskCategory.IV
            ],
            col_headers=[
                Load.SNOW,
                Load.ICE_THICKNESS,
                Load.ICE_WIND,
                Load.SEISMIC
            ]
        ).add_values([
                [0.80, 0.80, 1.00, 1.00],
                [1.00, 1.00, 1.00, 1.00],
                [1.10, 1.15, 1.00, 1.25],
                [1.20, 1.25, 1.00, 1.50],
            ]
        )

    @staticmethod
    def get_importance_factor(risk: RiskCategory, load: Load):
        return Table_1_5__2.importance_factor[risk][load]
    
    @staticmethod
    def example_importance_factor():
        risk = Table_1_5__1.RiskCategory.II
        load = Table_1_5__2.Load.ICE_WIND

        Is = Table_1_5__2.get_importance_factor(risk, load)

        print("Importance Factor for Risk " + str(risk.value) + " and Load " + str(load.value) + ": " + str(Is))

# Table_1_5__2.example_importance_factor()
