from enum import Enum
from numpy import log10 as log

def limit(value, a, b):
    return max(min(value, max(a, b)), min(a, b))

class Figure:
    def __init__(self, theta, A, without_overhang: bool = True):
        self.A = A
        self.theta = theta
        self.fig = self.__class__.__name__
        
        negative = "negative_without_overhang" if without_overhang else "negative_with_overhang"

        try:
            self.GCp_values = [(zone.value, self.GCp["positive"][zone](A), self.GCp[negative][zone](A)) 
                               for zone in self.Zone]
        except:
            self.GCp_values = [(zone.value, self.GCp["positive"][zone](A), self.GCp[negative][zone](A, theta)) 
                               for zone in self.Zone]
 
class Figure_30_3__1(Figure):
    class Zone(str, Enum):
        _4 = 4
        _5 = 5

    GCp = {
        "positive": {
            zone.value: lambda A: limit(1.1766 - 0.1766 * log(A), 0.7, 1.0) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._4.value: lambda A: limit(-1.2766 + 0.1766 * log(A), -1.1, -0.8),
            Zone._5.value: lambda A: limit(-1.7532 + 0.3532 * log(A), -1.4, -0.8)
        }
    }

class Figure_30_3__2A(Figure):
    class Zone(str, Enum):
        _1_prime = '1\''
        _1 = 1
        _2 = 2
        _3 = 3

    GCp = {
        "positive": {
            zone.value: lambda A: limit(0.4000 - 0.1000 * log(A), 0.2, 0.3) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1_prime.value: lambda A: limit(-1.9000 + 0.5000 * log(A), -0.9, -0.4),
            Zone._1.value: lambda A: limit(-2.1110 + 0.4120 * log(A), -1.7, -1.0),
            Zone._2.value: lambda A: limit(-2.8297 + 0.5297 * log(A), -2.3, -1.4),
            Zone._3.value: lambda A: limit(-4.2595 + 1.0595 * log(A), -3.2, -1.4)
        },
        "negative_with_overhang": {
            Zone._1.value: lambda A: limit(-1.8000 + 0.1000 * log(A), -1.7, -1.0) if A < 100 else limit(-3.3168 +0.8584 * log(A), -1.7, -1.0),
            Zone._2.value: lambda A: limit(-3.0063 + 0.7063 * log(A), -2.3, -1.1),
            Zone._3.value: lambda A: limit(-4.4360 + 1.2360 * log(A), -3.2, -1.1)
        }
    }

    GCp["negative_with_overhang"][Zone._1_prime] = GCp["negative_with_overhang"][Zone._1]

class Figure_30_3__2B(Figure):
    class Zone(str, Enum):
        _1 = 'zone 1'
        _2e = 'zone 2e'
        _2n = 'zone 2n'
        _2r = 'zone 2r'
        _3e = 'zone 3e'
        _3r = 'zone 3r'

    GCp = {
        "positive": {
            zone.value: lambda A: limit(0.7709 - 0.2354 * log(A), 0.3, 0.7) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1.value: lambda A: limit(-4.7920 + 2.1460 * log(A), -2.0, -0.5),
            Zone._2n.value: lambda A: limit(-4.4307 + 1.4307 * log(A), -3.0, -1.0),
            Zone._3r.value: lambda A: limit(-5.4000 + 1.800 * log(A), -3.6, -1.8)
        },
        "negative_with_overhang": {
            Zone._1.value: lambda A: limit(-4.3614 + 1.4307 * log(A), -2.5, -1.5),
            Zone._2n.value: lambda A: limit(-4.5730 + 1.0730 * log(A), -3.5, -2.0),
            Zone._3e.value: lambda A: limit(-5.9599 + 1.8599 * log(A), -4.1, -1.5),
            Zone._3r.value: lambda A: limit(-7.1000 + 2.4000 * log(A), -4.7, -2.3)
        }
    }

    GCp["negative_without_overhang"][Zone._2e] = GCp["negative_without_overhang"][Zone._1]
    GCp["negative_without_overhang"][Zone._2r] = GCp["negative_without_overhang"][Zone._2n]
    GCp["negative_without_overhang"][Zone._3e] = GCp["negative_without_overhang"][Zone._2n]

    GCp["negative_with_overhang"][Zone._2e] = GCp["negative_with_overhang"][Zone._1]
    GCp["negative_with_overhang"][Zone._2r] = GCp["negative_with_overhang"][Zone._2n]

class Figure_30_3__2C(Figure):
    class Zone(str, Enum):
        _1 = 'zones_1'
        _2e = 'zones_2e'
        _2n = 'zones_2n'
        _2r = 'zones_2r'
        _3r = 'zones_3r'
        _3e = 'zones_3e'

    GCp = {
        "positive": {
            zone.value: lambda A: limit(0.7709 - 0.2354 * log(A), 0.3, 0.7) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1.value: lambda A: limit(-2.2744 + 0.5952 * log(A), -1.5, -0.8),
            Zone._2n.value: lambda A: limit(-3.6054 + 1.1054 * log(A), -2.5, -1.2),
            Zone._3e.value: lambda A: limit(-4.5880 + 1.6410 * log(A), -3.6, -1.8)
        },
        "negative_with_overhang": {
            Zone._1.value: lambda A: limit(-2.2212 + 0.1701 * log(A), -2.0, -1.8),
            Zone._2n.value: lambda A: limit(-3.6802 + 0.6802 * log(A), -3.0, -2.2),
            Zone._3r.value: lambda A: limit(-5.2155 + 1.6155 * log(A), -3.6, -1.7),
            Zone._3e.value: lambda A: limit(-6.0173 + 2.1880 * log(A), -4.7, -2.3)
        }
    }

    GCp["negative_without_overhang"][Zone._2e] = GCp["negative_without_overhang"][Zone._1]
    GCp["negative_without_overhang"][Zone._2r] = GCp["negative_without_overhang"][Zone._2n]
    GCp["negative_without_overhang"][Zone._3r] = GCp["negative_without_overhang"][Zone._2n]

    GCp["negative_with_overhang"][Zone._2e] = GCp["negative_with_overhang"][Zone._1]
    GCp["negative_with_overhang"][Zone._2r] = GCp["negative_with_overhang"][Zone._2n]

class Figure_30_3__2D(Figure):
    class Zone(str, Enum):
        _1 = 'zones_1'
        _2e = 'zones_2e'
        _2n = 'zones_2n'
        _2r = 'zones_2r'
        _3r = 'zones_3r'
        _3e = 'zones_3e'

    GCp = {
        "positive": {
            zone.value: lambda A: limit(1.3000 - 0.4000 * log(A), 0.5, 0.9) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1.value: lambda A: limit(-2.8000 + 1.0000 * log(A), -1.8, -0.8),
            Zone._2n.value: lambda A: limit(-2.7686 + 0.7686 * log(A), -2.0, -1.0),
            Zone._3e.value: lambda A: limit(-3.5043 + 1.0110 * log(A), -3.2, -1.0)
        },
        "negative_with_overhang": {
            Zone._1.value: lambda A: limit(-3.6000 + 1.0000 * log(A), -2.6, -1.6),
            Zone._2n.value: lambda A: limit(-3.5686 + 0.7686 * log(A), -2.8, -1.8),
            Zone._3e.value: lambda A: limit(-4.3043 + 1.0110 * log(A), -4.0, -1.8)
        }
    }

    GCp["negative_without_overhang"][Zone._2e] = GCp["negative_without_overhang"][Zone._1]
    GCp["negative_without_overhang"][Zone._2r] = GCp["negative_without_overhang"][Zone._1]
    GCp["negative_without_overhang"][Zone._3r] = GCp["negative_without_overhang"][Zone._2n]

    GCp["negative_with_overhang"][Zone._2e] = GCp["negative_with_overhang"][Zone._1]
    GCp["negative_with_overhang"][Zone._2r] = GCp["negative_with_overhang"][Zone._1]
    GCp["negative_with_overhang"][Zone._3r] = GCp["negative_with_overhang"][Zone._2n]

class Figure_30_3__2E(Figure):
    class Zone(str, Enum):
        _1 = 'zone_1'
        _2e = 'zones_2e'
        _2r = 'zone_2r'
        _3 = 'zones_3'

    GCp_hB_geq_08 = {
        "positive": {
            zone.value: lambda A: limit(1.1000 - 0.4000 * log(A), 0.3, 0.7) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1.value: lambda A: limit(-3.2891 + 1.1445 * log(A), -1.8, -1.0),
            Zone._2r.value: lambda A: limit(-3.2455 + 0.8455 * log(A), -2.4, -1.3),
            Zone._3.value: lambda A: limit(-3.5223 + 0.9223 * log(A), -2.6, -1.4)
        }
    }

    GCp_hB_geq_08["negative_without_overhang"][Zone._2e] = GCp_hB_geq_08["negative_without_overhang"][Zone._3]

    GCp_hB_leq_05 = {
        "positive": {
            zone.value: lambda A: limit(1.1000 - 0.4000 * log(A), 0.3, 0.7) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1.value: lambda A: limit(-1.8584 + 0.4292 * log(A), -1.3, -1.0),
            Zone._2r.value: lambda A: limit(-3.2455 + 0.8455 * log(A), -2.4, -1.3),
            Zone._3.value: lambda A: limit(-2.3380 + 0.5380 * log(A), -1.8, -1.1)
        }
    }

    GCp_hB_leq_05["negative_without_overhang"][Zone._2e] = GCp_hB_leq_05["negative_without_overhang"][Zone._3]

    def __init__(self, theta, A, h, B, with_overhang):
        if h/B >= 0.8: 
            self.GCp = self.GCp_hB_geq_08
        elif h/B <= 0.5:
            self.GCp = self.GCp_hB_leq_05
        else:
            pass
        super.__init__(theta, A, False)


class Figure_30_3__2F(Figure):
    class Zone(str, Enum):
        _1 = 'zone_1'
        _2e = 'zones_2e'
        _2r = 'zone_2r'
        _3 = 'zones_3'

    GCp_hB_geq_08 = {
        "negative_with_overhang": {
            Zone._1.value: lambda A: limit(-2.8584 + 0.4292 * log(A), -2.3, -2.0),
            Zone._2r.value: lambda A: limit(-3.3612 + 0.4612 * log(A), -2.9, -2.3),
            Zone._2e.value: lambda A: limit(-3.6380 + 0.5380 * log(A), -3.1, -2.4),
            Zone._3.value: lambda A: limit(-5.0835 + 1.3835 * log(A), -3.7, -1.9)
        }
    }

    GCp_hB_leq_05 = {
        "negative_with_overhang": {
            Zone._1.value: lambda A: limit(-1.4277 - 0.2861 * log(A), -1.8, -2.0),
            Zone._2r.value: lambda A: limit(-3.3612 + 0.4612 * log(A), -2.9, -2.3),
            Zone._2e.value: lambda A: limit(-2.4537 + 0.1537 * log(A), -2.3, -2.1),
            Zone._3.value: lambda A: limit(-3.8992 + 0.9992 * log(A), -2.9, -1.6)
        }
    }
    
    def __init__(self, theta, A, h, B, with_overhang):
        if h/B >= 0.8: 
            self.GCp = self.GCp_hB_geq_08
        elif h/B <= 0.5:
            self.GCp = self.GCp_hB_leq_05
        else:
            pass
        self.GCp["positive"] = Figure_30_3__2E.GCp["positive"]
        super.__init__(theta, A, True)


class Figure_30_3__2G(Figure):
    class Zone(str, Enum):
        _1 = 'zone_1'
        _2e = 'zones_2e'
        _2r = 'zone_2r'
        _3 = 'zones_3'

    GCp = {
        "positive": {
            zone.value: lambda A: limit(1.1000 - 0.4000 * log(A), 0.3, 0.7) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1.value: lambda A: limit(-2.0000 + 0.6000 * log(A), -1.4, -0.8),
            Zone._2e.value: lambda A: limit(-2.7686 + 0.7686 * log(A), -2.0, -1.0)
        },
        "negative_with_overhang": {
            Zone._1.value: lambda A: limit(-2.0000 + 0.1000 * log(A), -1.9, -1.8),
            Zone._2e.value: lambda A: limit(-2.8843 + 0.3843 * log(A), -2.5, -2.0),
            Zone._3.value: lambda A: limit(-4.3298 + 1.2298 * log(A), -3.1, -1.5)
        }
    }

    GCp["negative_without_overhang"][Zone._2r] = GCp["negative_without_overhang"][Zone._2e]
    GCp["negative_without_overhang"][Zone._3] = GCp["negative_without_overhang"][Zone._2e]
    GCp["negative_with_overhang"][Zone._2r] = GCp["negative_with_overhang"][Zone._2e]

class Figure_30_3__2H(Figure):
    class Zone(str, Enum):
        _1 = 'zone_1'
        _2e = 'zone_2e'
        _2r = 'zone_2r'
        _3 = 'zones_3'

    GCp = {
        "positive": {
            zone.value: lambda A: limit(1.0063 - 0.3532 * log(A), 0.3, 0.9) for zone in Zone
        },
        "negative_without_overhang": {
            Zone._1.value: lambda A, theta: limit(-1.0191 - 0.0250 * theta + (0.4016 + 0.0050 * theta) * log(A), \
                                                -0.6175 - 0.0200 * theta, -0.0950 - 0.0135 * theta),
            Zone._2e.value: lambda A, theta: limit(
                    -0.8000 + ((log(280 - 5 * theta) * (0.0670 * theta - 1)) / (0.301 - log(280 - 5 * theta))) + 
                    ((1 - 0.0670 * theta) / (0.3010 - log(280 - 5 * theta))) * log(A), -0.8, 0.2000 - 0.0670 * theta),
            Zone._2r.value: lambda A, theta: limit(2.0746 - 0.1261 * theta + (0.0630 * theta - 1.5373) * log(A), -1.0000, 1.0000 - 0.0820 * theta),
            Zone._3.value: lambda A, theta: limit(
                    ((0.1835 * theta - 3.8230) / (log(9 - 0.1350 * theta) - 1.6990)) - 1.0 + 
                    ((2.25 - 0.1080 * theta) / (log(9 - 0.1350 * theta) - 1.6990)) * log(A), -1.0000, 1.2500 - 0.1080 * theta)
        }
    }

class Figure_30_3__2I(Figure):
    class Zone(str, Enum):
        _1 = 'zone_1'
        _2e = 'zone_2e'
        _2r = 'zone_2r'
        _3 = 'zones_3'

    GCp = {
        "negative_with_overhang": {
            Zone._1.value: lambda A, theta: limit(-1.8191 - 0.0250 * theta + (0.4016 + 0.0050 * theta) * log(A), -1.4175 - 0.0200 * theta, -0.8950 - 0.0135 * theta),
            Zone._2e.value: lambda A, theta: limit(
                    -1.6000 + ((log(280 - 5 * theta) * (0.0670 * theta - 1)) / (0.301 - log(280 - 5 * theta))) + 
                    ((1 - 0.0670 * theta) / (0.301 - log(280 - 5 * theta))) * log(A), -1.6000, -0.6000 - 0.0670 * theta),
            Zone._2r.value: lambda A, theta: limit(1.2745 - 0.1261 * theta + (0.0630 * theta - 1.5373) * log(A), -1.8000, 0.2000 - 0.0820 * theta),
            Zone._3.value: lambda A, theta: limit(
                    ((0.1835 * theta - 3.823) / (log(9 - 0.135 * theta) - 1.699)) - 1.8 + 
                    ((2.25 - 0.108 * theta) / (log(9 - 0.135 * theta) - 1.699)) * log(A), -1.8000, 0.4500 - 0.1080 * theta)
        }
    }

#Todo other roofs figures

class BuildingType:
    WALL = 'wall'
    GABLE_ROOF = 'gable'
    HIP_ROOF = 'hip'
    STEPPED_ROOF = 'stepped'
    MULTISPAN_GABLE_ROOF = 'multispan_gable'
    MONOSLOPE_ROOF = 'monoslope'
    SAWTOOTH_ROOF = 'sawtooth'
    DOMED_ROOF = 'domed'

class WindPressureCoefficient:
    def __init__(self, theta: float, A: float, h: float, B: float, building_type: str, without_overhang: bool = True):
        self.building_type = building_type
        self.theta = theta
        self.A = A
        self.h = h
        self.B = B

        arg = {"theta": theta, "A": A, "without_overhang": without_overhang}

        if building_type == BuildingType.WALL:
            if 45 <= theta <= 90:
                self.fig = Figure_30_3__1(**arg)
            else:
                raise ValueError(f"Invalid angle {theta}. The angle must be between 45 and 90 degrees for Wall.")
        
        elif building_type == BuildingType.GABLE_ROOF:
            if theta <= 7:
                self.fig = Figure_30_3__2A(**arg)
                
            elif 7 < theta <= 20:
                self.fig = Figure_30_3__2B(**arg)
                
            elif 20 < theta <= 27:
                self.fig = Figure_30_3__2C(**arg)
                
            elif 27 < theta <= 45:
                self.fig = Figure_30_3__2D(**arg)
            else:
                raise ValueError(f"Invalid angle {theta}. The angle must be < 45 degrees for Gable.")
            
        elif building_type == BuildingType.HIP_ROOF:
            if theta <= 7:
                self.fig = Figure_30_3__2A(**arg)

            elif 7 < theta <= 20:
                arg["h"] = self.h
                arg["B"] = self.B
                self.fig = Figure_30_3__2E(**arg) if without_overhang else Figure_30_3__2F(**arg)
            
            elif 20 < theta <= 27:
                self.fig = Figure_30_3__2G(**arg)
            elif 27 < theta <= 45:
                self.fig = Figure_30_3__2H(**arg) if without_overhang else Figure_30_3__2I(**arg)
            else:
                raise ValueError("Invalid theta value. Theta must be < 45 degrees.")
            
def example():
    theta = 45
    A = 14.8148148148148
    h = 30
    B = 60

    wc = WindPressureCoefficient(theta, A, h, B, BuildingType.HIP_ROOF)

    print(wc.fig.GCp["positive"][wc.fig.Zone._1.value](2))
    print(wc.fig.GCp["positive"][wc.fig.Zone._1.value](100))
    
    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._1.value](10, theta))
    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._2r.value](5, theta))
    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._2e.value](2, theta))
    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._3.value](2.925, theta))

    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._1.value](200, theta))
    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._2r.value](100, theta))
    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._2e.value](55, theta))
    print(wc.fig.GCp["negative_without_overhang"][wc.fig.Zone._3.value](50, theta))


example()